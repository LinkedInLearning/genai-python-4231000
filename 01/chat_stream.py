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
        max_tokens=350,
        stream=True,  # Streaming aktivieren
    )
    # message = response.choices[0].message
    # messages.append(message)
    # print("Assistent: " + message.content)

    # flush-Parameter bestimmt, ob der Ausgabepuffer sofort geleert  wird.
    #  flush auf True: die Ausgabe erscheint direkt auf der Konsole 
    print(f"Assistent: ", end="", flush=True)
    response_text = ""
        # Über alle Teile der gestreamten Antwort iterieren
    for part in response:
        # delta statt message bei streaming responses
        # Text von dem aktuellen Teil extrahieren; fallback auf einen leeren String, wenn keiner vorhanden ist
        delta = part.choices[0].delta.content or ""

        # Test zusammenstellen 
        response_text += delta

        # Aktuellen Teil der Antwort ausgeben ohne neue Zeile hinzuzufügen
        print(delta, end="", flush=True)
    else:
        # Aktuelle Nachricht zur Konversation hinzufügen, damit die KI den Kontext in zukünftigen Interaktionen beibehalten kann
        messages.append({"role": "assistant", "content": response_text})

        # Neue Zeile ausgeben, sobald die gesamte Antwort gestreamt wurde
        print()

if __name__ == "__main__":
    main()
