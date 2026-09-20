import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_classic.chains import RetrievalQA
from pytube import YouTube
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled, 
    NoTranscriptFound,
    VideoUnavailable,                                                                                                        CouldNotRetrieveTranscript
)
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if gemini_api_key:
    os.environ["GOOGLE_API_KEY"] = gemini_api_key

def get_youtube_transcript(url):
    try:
        video_id = YouTube(url).video_id
        transcript_api = YouTubeTranscriptApi()
        transcript_list = transcript_api.list(video_id)
        transcript = transcript_list.find_transcript(["en"])
        transcript_data = transcript.fetch()
        text = " ".join([item.text for item in transcript_data])
        return text
    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        st.error("No transcript found for this video.")
    except VideoUnavailable:
        st.error("This video is unavailable.")
    except CouldNotRetrieveTranscript:
        st.error("Could not retrieve transcript. It may not be available in your region.")
    except Exception as e:
        st.error(f"Unexpected error getting transcript: {e}")
    return ""

def save_transcript_to_file(text, filename="transcript.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

st.title("AI-Powered Tutor")
st.write("Ask questions from YouTube lecture transcripts.")

video_url = st.text_input("Enter YouTube Video URL")

if st.button("Process Video"):
    if video_url:
        transcript_text = get_youtube_transcript(video_url)
        if transcript_text:
            save_transcript_to_file(transcript_text)

            loader = TextLoader("transcript.txt", encoding="utf-8")
            documents = loader.load()

            splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            docs = splitter.split_documents(documents)

            embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
            vectorstore = FAISS.from_documents(docs, embeddings)
            retriever = vectorstore.as_retriever()
            qa_chain = RetrievalQA.from_chain_type(
                llm=ChatGoogleGenerativeAI(model="gemini-3.6-flash"),
                retriever=retriever,
            )

            st.session_state.qa_chain = qa_chain
            st.success("Transcript processed successfully! You can now ask questions.")
    else:
        st.warning("Please enter a valid YouTube URL.")

if "qa_chain" in st.session_state:
    user_question = st.text_input("Ask a question from the video transcript")
    if user_question:
        answer = st.session_state.qa_chain.run(user_question)
        st.write("**Answer:**", answer)