# AI Voice Support Agent

An AI-powered voice assistant that listens to customer queries, retrieves relevant information using a language model, and responds with natural speech. Designed to help automate the first layer of customer service workflows through voice interaction.

---

## 🎯 Project Goal

This project demonstrates how to combine voice interaction, document-based retrieval, and language models to create a customer service assistant that can speak and understand real human queries — ideal To automate the initial layer of call center interactions 


---

## ✨ Features

- 🎙️ Voice input using speech recognition
- 🔍 Intelligent answer retrieval with vector embeddings
- 🧠 Uses Groq + LLaMA 3.3 70B for fast, accurate responses
- 🗣️ Speaks responses with natural-sounding TTS

---

## 🧰 Tech Stack

| Layer              | Tool/Library                  |
|--------------------|-------------------------------|
| Voice Input        | `speechrecognition`           |
| Text-to-Speech     | `pyttsx3`                     |
| LLM                | `langchain`, `langchain-groq` |
| Embeddings         | `HuggingFaceEmbeddings`       |
| Vector Store       | `FAISS`                       |
| PDF Loader         | `PyPDFLoader`                 |
| Env Management     | `python-dotenv`               |

---

## 🗂️ Project Structure
```bash
ai-voice-support-agent/
├── main.py              # Main script: voice interaction loop
├── config.py            # Environment variables and PDF path
├── voice_utils.py       # Handles speech-to-text and text-to-speech
├── document_utils.py    # Loads and vectorizes documents
├── ai_utils.py          # Sets up LLM and handles Q&A
├── requirements.txt     # All required Python packages
├── .env                 # (Ignored) Stores your GROQ_API_KEY
├── README.md            # Project documentation
```
---

## ⚙️ Installation

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/SIDHARTH-PATTALI/ai-voice-support-agent.git
cd ai-voice-support-agent
```

### 2. 📦 Install Dependencies

Ensure you have Python 3.8 or higher installed.

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

### Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Set the path to your PDF in `config.py`:

```python
PDF_PATH = "C:/Users/yourname/Documents/your_file.pdf"
```

---

## 🚀 Running the Assistant

Start the assistant by running:

```bash
python main.py
```

Then speak your question into the microphone. The assistant will respond using voice. Say **"exit"** anytime to quit the program.

---



---

## 💡 Customization Ideas

- ☎️ Integrate with Twilio for phone support  
- 🧭 Route based on topics (billing, tech, etc.)  
- 🗣️ Replace pyttsx3 with a more natural TTS engine (e.g. ElevenLabs)

---



