import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
# erst ab Tier 1 verfügbar
# https://platform.openai.com/docs/guides/rate-limits/usage-tiers?context=tier-free

url = "https://upload.wikimedia.org/wikipedia/commons/f/f0/Ophiopteris_antipodum.JPG"
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Was für ein Tier ist im Bild?"},
        {"type": "image_url", "image_url": {"url": url}}
      ]
    }
  ]
)
print(response.choices[0].message.content)