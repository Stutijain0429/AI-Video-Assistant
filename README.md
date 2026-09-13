# 🎥 AI Video Assistant

### Transform Videos into Actionable Insights using AI

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Whisper](https://img.shields.io/badge/Whisper-Speech--to--Text-green?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-purple?style=for-the-badge)

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
```
Video Input
│
▼
Audio Extraction (yt-dlp + FFmpeg)
│
▼
Whisper Transcription
│
▼
Groq (LLaMA / GPT-OSS)
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

| Category         | Technology         |
| ---------------- | ------------------ |
| Language         | Python             |
| UI               | Streamlit          |
| Speech-to-Text   | OpenAI Whisper     |
| LLM              | Groq API           |
| Framework        | LangChain          |
| Vector DB        | ChromaDB           |
| Embeddings       | HuggingFace MiniLM (Sentence Transformers) |
| Audio Processing | FFmpeg, yt-dlp     |
| Retrieval        | RAG                |

---

# 📂 Project Structure
```
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

### 1. Clone the repository
```bash
git clone https://github.com/Stutijain0429/AI-Video-Assistant.git
cd AI-Video-Assistant
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg (required for audio processing)
FFmpeg must be installed system-wide (not just via pip):
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org) and add to PATH
- **Mac**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

### 5. Set up YouTube cookies (required to avoid bot-detection errors)
YouTube sometimes blocks automated downloads with a "Sign in to confirm you're not a bot" error. To fix this:
1. Install the **"Get cookies.txt LOCALLY"** browser extension
2. Log into YouTube in your browser
3. Export cookies and save them as `cookies.txt` in the project root
4. This file is git-ignored and never uploaded — it stays local to your machine

### 6. Run the app
```bash
streamlit run app.py
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

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

⭐ If you like this project, consider giving it a star!