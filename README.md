# YouTube Transcript Tutor

An AI-powered Streamlit application that converts YouTube lecture transcripts into an interactive tutor.

Users can enter a YouTube video URL, process its transcript, and ask questions about the video using **Google Gemini, embeddings, FAISS, and Retrieval-Augmented Generation (RAG)**.

> **Learning Project:** This project was built while learning and practicing LLM, embeddings, vector search, and RAG concepts.

## Features

* Extracts available English transcripts from YouTube videos
* Splits transcripts into smaller overlapping chunks
* Generates embeddings using Google Gemini
* Stores embeddings using FAISS
* Retrieves relevant transcript content
* Generates answers using Gemini
* Simple Streamlit interface
* Handles common transcript errors

## How It Works

```text
YouTube URL
     ↓
Transcript Extraction
     ↓
Text Chunking
     ↓
Gemini Embeddings
     ↓
FAISS Vector Search
     ↓
Relevant Context
     ↓
Gemini LLM
     ↓
Answer
```

## Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini**
* **FAISS**
* **YouTube Transcript API**
* **Pytube**
* **python-dotenv**

## Project Structure

```text
youtube-transcript-tutor/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── transcript.txt
```

> `.env` and generated files such as `transcript.txt` should be excluded from Git.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/dineshraja-dr/youtube-transcript-tutor.git
cd youtube-transcript-tutor
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_api_key_here
```

**Never commit your actual API key to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

## Usage

1. Enter a YouTube video URL.
2. Click **Process Video**.
3. Wait for the transcript and vector index to be created.
4. Enter a question about the video.
5. The AI generates an answer using the relevant transcript content.

## Learning Outcomes

Through this project, I practiced:

* LLM API integration
* Prompt-based AI applications
* Text preprocessing and chunking
* Embeddings
* Vector similarity search
* FAISS
* Retrieval-Augmented Generation (RAG)
* LangChain
* Streamlit application development
* Environment variable and API-key management

## Attribution

This is a **learning project** developed by following and adapting concepts from a YouTube tutorial.

Original tutorial: **[Add the YouTube tutorial link here]**

The project was modified while learning and experimenting with the technologies used in the application.

## Future Improvements

* Support multiple transcript languages
* Add conversation memory
* Improve retrieval quality
* Add source references for answers
* Add a FastAPI backend
* Deploy the application to the cloud
* Add RAG evaluation

## License

No license has been selected for this learning project.
