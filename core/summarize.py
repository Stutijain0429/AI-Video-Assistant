from core.analyzer import analyze_transcript

def summarize(transcript: str) -> str:
    return analyze_transcript(transcript)["summary"]

def generate_title(transcript: str) -> str:
    return analyze_transcript(transcript)["title"]