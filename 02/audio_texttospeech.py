from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

speech_file_path = Path(__file__).parent / "deutsch.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="nova",
  input="Der Eiffelturm ist ein Wahrzeichen von Paris."
)

with open(speech_file_path, "wb") as f:
    f.write(response.content)