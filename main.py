import os
import tempfile
import wave
import pyaudio
import threading
import pyperclip
from groq import Groq


# Initialize Groq client (Replace API key with your actual key)
client = Groq(api_key="your_key")


def record_audio(sample_rate=16000, channels=1, chunk=1024):
    """
    Record audio until user presses ENTER to stop.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk)

    print("\nPress ENTER to start recording...") 
    input() 
    print("Recording... (Press ENTER again to stop)")

    frames = []
    stop_recording = threading.Event()

    def wait_for_stop():
        input()  
        stop_recording.set()

    stopper = threading.Thread(target=wait_for_stop)
    stopper.start()

    while not stop_recording.is_set():
        try:
            data = stream.read(chunk, exception_on_overflow=False)
            frames.append(data)
        except Exception as e:
            print("Error during recording:", e)
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames, sample_rate

def save_audio(frames, sample_rate):
    """
    Save recorded audio to a temporary WAV file.
    """
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        wav_file = temp_audio.name

    with wave.open(wav_file, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  
        wf.setframerate(sample_rate)
        wf.writeframes(b"".join(frames))

    return wav_file

def transcribe_audio(audio_file_path):
    """
    Transcribe the recorded audio using Groq's Whisper API.
    """
    try:
        with open(audio_file_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(os.path.basename(audio_file_path), file.read()),
                model="whisper-large-v3",
                prompt="Transcribe everything clearly and accurately.",
                response_format="text",
                language="en",
            )
        return transcription
    except Exception as e:
        print(f"Transcription error: {e}")
        return None

def copy_to_clipboard(text):
    """
    Copy the transcribed text to the clipboard.
    """
    pyperclip.copy(text)
    print("✅ Transcription copied to clipboard. Paste it anywhere.")

def main():
    while True:
        # Record Audio
        frames, sample_rate = record_audio()

        # Save Audio to Temp File
        temp_audio_file = save_audio(frames, sample_rate)

        # Transcribe Audio
        print("Transcribing audio...")
        transcription = transcribe_audio(temp_audio_file)

        if transcription:
            print("\nTranscription:\n")
            print(transcription)
            copy_to_clipboard(transcription)
        else:
            print("❌ Transcription failed.")

        # Clean up temporary audio file
        os.unlink(temp_audio_file)

        print("\nReady for the next recording. Press ENTER to start.")

if __name__ == "__main__":
    main()
