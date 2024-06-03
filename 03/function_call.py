from openai import OpenAI
import json
from weather import get_current_weather
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)
# Liste der verfügbaren Tools und deren Funktionen
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Wetter zu einem Ort ermitteln",
            "parameters": {
                "type": "object",
                "properties": {
                    "loc": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["loc", "unit"],
            },
        },
    }
]


messages = [{"role": "system", "content": "Du bist ein hilfreicher Assistent"}]

def generate_response(user_input):
    # Nachrichten und verfügbare Informationen an Modell senden
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=tools,
        tool_choice="auto", # default, aber hier explizit gesetzt
    )
    messages.append(
        response.choices[0].message
    )  
    # print (response)
    return response.choices[0].message


available_functions = {
    "get_current_weather": get_current_weather,
}  


def call_function(tool_calls):
    for tool_call in tool_calls:
        function_name = tool_call.function.name

        # Funktion ermitteln, die aufgerufen werden soll
        function_to_call = available_functions[function_name]

        # Argumente für die Funktion aus dem Tool-Call extrahieren
        function_args = json.loads(tool_call.function.arguments)

        # Aufruf der Funktion, speichern der Ergebnisse in function_response
        function_response = function_to_call(
            loc=function_args.get("loc"),
            unit=function_args.get("unit"),
        )
        messages.append(
             {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            }
        )  


def main():
    print("Der Chat ist gestartet. Drücke 'Ctrl+C' um den Chat zu beenden.")
    try:
        while True:
            user_input = input("Du: ")
            message_response = generate_response(user_input)

            if message_response.tool_calls is None:
                print("AssistentOhne: " + message_response.content)
                continue
            call_function(message_response.tool_calls)
            # Funktion wurde aufgerufen und in messages Liste integriert 
            # jetzt aktualisierte Antwort erhalten mit eingegangen Informationen. 
            second_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )  
            print("AssistentMit: " + second_response.choices[0].message.content)

    except KeyboardInterrupt:
            print("\nTschüss.")

if __name__ == "__main__":
    main()