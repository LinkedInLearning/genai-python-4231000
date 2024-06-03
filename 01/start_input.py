import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))
user_input = input("Du: ")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Du bist eine schlecht gelaunte, mürrische Katze."},
    {"role": "user", "content": user_input},
  ]
)

print(completion.choices[0].message.content)