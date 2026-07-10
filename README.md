<div align="center">

# 🎥 AI Video Assistant

### Transform Videos into Actionable Insights using AI

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit"/>
<img src="https://img.shields.io/badge/Whisper-Speech--to--Text-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/LangChain-RAG-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Mistral-AI-purple?style=for-the-badge"/>

</div>

---

## 📌 Overview

AI Video Assistant is an intelligent application that converts YouTube videos or local audio/video files into structured meeting insights.

It automatically transcribes speech, generates AI-powered summaries, extracts action items and key decisions, identifies open questions, and enables users to chat with the meeting transcript using Retrieval-Augmented Generation (RAG).

---

# ✨ Features

- 🎥 Analyze YouTube videos
- 📂 Upload local audio/video files
- 🎤 Speech-to-Text with OpenAI Whisper
- 📝 AI-generated Meeting Summary
- 📌 Automatic Meeting Title
- ✅ Extract Action Items
- 🔑 Detect Key Decisions
- ❓ Identify Open Questions
- 💬 Chat with Meeting using RAG
- 🌍 English & Hinglish Support
- ⚡ Interactive Streamlit Interface

---

# 🏗️ Architecture

```text
Video Input
      │
      ▼
Audio Extraction
      │
      ▼
Whisper Transcription
      │
      ▼
Mistral AI
 ├── Summary
 ├── Title
 ├── Action Items
 ├── Decisions
 └── Questions
      │
      ▼
Vector Database (Chroma)
      │
      ▼
RAG Chatbot
      │
      ▼
Streamlit UI
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| UI | Streamlit |
| Speech-to-Text | OpenAI Whisper |
| LLM | Mistral AI |
| Translation | Sarvam AI |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Embeddings | HuggingFace MiniLM |
| Audio Processing | FFmpeg, yt-dlp |
| Retrieval | RAG |

---

# 📂 Project Structure

```text
AI-Video-Assistant/
│
├── app.py
├── main.py
├── core/
├── utils/
├── downloads/
├── vector_db/
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

# 🚀 Installation

```bash
git clone <repository-url>

cd AI-Video-Assistant

pip install -r requirements.txt

streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
MISTRAL_API_KEY=YOUR_KEY
SARVAM_API_KEY=YOUR_KEY
WHISPER_MODEL=base
```

---

# 💡 Future Improvements

- Speaker Diarization
- Multi-language Support
- PDF Report Export
- Meeting Analytics Dashboard
- Cloud Deployment
- Real-time Meeting Assistant

---

# 👩‍💻 Author

**Stuti Jain**

B.Tech AIML Student | Python Developer | AI/ML Enthusiast

---

<div align="center">

⭐ If you like this project, consider giving it a star!

</div>