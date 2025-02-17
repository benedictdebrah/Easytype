
# 🎙️ EasyType

EasyType is a **lightweight speech-to-text tool** that records your voice, transcribes it using **Groq Whisper**, and **copies the text to your clipboard** so you can paste it anywhere.  

"The motivation behind this project was to get a tool that can transcribe everything that I'm saying to a text format. This time I was writing an essay and I felt lazy to write everything down just from my end. I think the best way for me was just to say something and it will transcribe it to a text. I'll paste it and I'll just make changes to it. That was the whole motivation behind this project. Yeah." ~ **Transcribed using this tool**

## 🚀 Features  
✔ **Hands-free recording** – Press **ENTER to start**, **ENTER again to stop**  
✔ **High-quality transcription** using **Groq Whisper**  
✔ **Automatic clipboard copy** – Just paste it anywhere  
✔ **Simple setup** – Works on **macOS & Linux**  

## 🛠️ Installation  

### 1️⃣ Install Python (If Not Installed)  
Make sure you have **Python 3.13+** installed. Check by running:  
```bash
python3 --version
```
If not installed, download Python from [python.org](https://www.python.org/downloads/).  

### 2️⃣ Install `uv` Package Manager (If Not Installed)  
Your project uses `uv` instead of `pip`. If you haven’t installed `uv`, run:  
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3️⃣ Install Dependencies  
Run:  
```bash
uv venv .venv  
source .venv/bin/activate  # macOS/Linux  
uv pip install -r requirements.txt  
```

If using `pyproject.toml`:  
```bash
uv pip install  
```

### 4️⃣ API Key Setup  
1. Get a **Groq API key** from [Groq’s website](https://groq.com/).  
2. Open the script and replace:  
   ```python
   client = Groq(api_key="your_actual_api_key_here")
   ```
   with your actual API key.

---

## 🎤 Usage  
1️⃣ **Run the script**  
```bash
python3 main.py
```

2️⃣ **Press ENTER to start recording.**  
3️⃣ **Speak while recording.**  
4️⃣ **Press ENTER again to stop.**  
5️⃣ **Your transcribed text is copied to your clipboard.**  
6️⃣ **Paste it anywhere!** (Cmd + V on Mac, Ctrl + V on Windows/Linux)  

---

## 🔧 Troubleshooting  
### ❌ **Permission Error (`OSError: Error 13`)**  
**Fix:** Run the script **without sudo** because `pyperclip` and `pyaudio` don’t need admin access.  

### ❌ **PyAudio Installation Issues on macOS**  
If you see a PyAudio error, install it via Homebrew:  
```bash
brew install portaudio  
uv pip install pyaudio  
```

### ❌ **Groq API Issues**  
If transcription fails:  
- Check your **API key**  
- Ensure you're using **model="whisper-large-v3"**  

---

## 📜 License  
MIT License – Free to use and modify! 🚀  

---
