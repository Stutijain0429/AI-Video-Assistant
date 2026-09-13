import os
import json
import time
import hashlib
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tenacity import retry, wait_exponential, stop_after_attempt

load_dotenv()

_cache = {}  # avoids re-calling Mistral if same transcript asked again

def get_llm():
    return ChatGroq(model="openai/gpt-oss-20b", groq_api_key=os.getenv("GROQ_API_KEY"), temperature=0.2)

def split_transcript(transcript: str) -> list:
    splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=200)
    return splitter.split_text(transcript)

@retry(wait=wait_exponential(multiplier=1.5, min=2, max=15), stop=stop_after_attempt(5), reraise=True,)
def _safe_invoke(chain, payload):
    return chain.invoke(payload)

def _condense_long_transcript(transcript: str, llm) -> str:
    """Only used for LONG transcripts — summarizes chunks first with a small
    delay between calls so we never burst past the rate limit."""
    map_prompt = ChatPromptTemplate.from_messages([
        ("system", "Summarize this portion of a meeting transcript concisely."),
        ("human", "{text}"),
    ])
    map_chain = map_prompt | llm | StrOutputParser()

    chunks = split_transcript(transcript)
    chunk_summaries = []
    for chunk in chunks:
        chunk_summaries.append(_safe_invoke(map_chain, {"text": chunk}))
        time.sleep(2)  # gap between chunk calls

    return "\n\n".join(chunk_summaries)

def analyze_transcript(transcript: str) -> dict:
    """ONE Mistral call returns title + summary + action_items +
    key_decisions + open_questions together, instead of 5 separate calls."""

    cache_key = hashlib.md5(transcript.encode("utf-8")).hexdigest()
    if cache_key in _cache:
        return _cache[cache_key]

    llm = get_llm()

    working_text = transcript
    if len(transcript) > 6000:
        working_text = _condense_long_transcript(transcript, llm)

    system_prompt = (
        "You are an expert meeting analyst. Based on the meeting transcript "
        "below, return ONLY a valid JSON object (no markdown fences, no extra "
        "text) with exactly these keys:\n"
        '- "title": short professional meeting title (max 8 words)\n'
        '- "summary": professional meeting summary in bullet points\n'
        '- "action_items": numbered list (as one string) of task, owner '
        "(or 'Not specified'), deadline (or 'Not specified'). If none, "
        "'No action items found.'\n"
        '- "key_decisions": numbered list (as one string). If none, '
        "'No key decisions found.'\n"
        '- "open_questions": numbered list (as one string). If none, '
        "'No open questions found.'"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{text}"),
    ])
    chain = prompt | llm | StrOutputParser()

    raw = _safe_invoke(chain, {"text": working_text})

    cleaned = raw.strip().strip("`")
    if cleaned.lower().startswith("json"):
        cleaned = cleaned[4:].strip()

    try:
        result = json.loads(cleaned)
    except json.JSONDecodeError:
        result = {
            "title": "Meeting Summary",
            "summary": raw,
            "action_items": "Could not parse action items.",
            "key_decisions": "Could not parse key decisions.",
            "open_questions": "Could not parse open questions.",
        }

    _cache[cache_key] = result
    return result