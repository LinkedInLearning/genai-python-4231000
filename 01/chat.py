from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPEN_API_KEY")
)

system_prompt = "Du bist ein hilfreicher Assistent."
messages = []
messages.append({"role": "system", "content": system_prompt})

def main():
    print("Der Chat ist gestartet. Drücke 'Ctrl+C' um den Chat zu beenden.")
    try:
        while True:
            user_input = input("Du: ")
            generate_response(user_input)
    except KeyboardInterrupt:
        print("\nChat wurde beendet.")

def generate_response(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=250,
    )
    message = response.choices[0].message
    messages.append(message)
    print("Assistent: " + message.content)

if __name__ == "__main__":
    main()
