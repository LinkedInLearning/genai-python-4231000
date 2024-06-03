from base64 import b64decode
from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.images.generate(
  model="dall-e-2",
  prompt="ein blühender Flieder",
  size="1024x1024",
  quality="standard",
  response_format= "b64_json",
  n=1,
)

image = b64decode(response.data[0].b64_json)
with open("flieder.jpg", "wb") as file:
  file.write(image)
