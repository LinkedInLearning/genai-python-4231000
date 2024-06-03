from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def clean_up(assistant_id, thread_id):
    """Assistenten/Thread löschen  """
    client.beta.assistants.delete(assistant_id)
    client.beta.threads.delete(thread_id)

# Assistent erstellen
assistant = client.beta.assistants.create(
  name="Mathe-Nachhilfelehrer",
  instructions="Du bist ein Mathe-Nachhilfelehrer. Schreibe Code und führe ihn aus, um mathematische Probleme zu lösen.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-3.5-turbo",
)

# Thread erstellen, repräsentiert eine Konversation zwischen User und Assistent
thread = client.beta.threads.create()

# Nachrichten zum Thread hinzufügen über ein Messages-Objekt
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="assistant",
  content = input("Welches mathematisches Problem möchtest du lösen? ")
)

# Einen Run erstellen und auf dessen Fertigstellung warten
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id
)

# Wenn der Run abgeschlossen ist, alle Nachrichten des Assistenten abrufen und ausgeben
thread_messages = client.beta.threads.messages.list(thread_id=thread.id)
assistant_messages = [msg for msg in thread_messages.data if msg.role == 'assistant']
assistant_messages.sort(key=lambda x: x.created_at)


# Run-Details ausgeben
run_steps = client.beta.threads.runs.steps.list(
    thread_id=thread.id,
    run_id=run.id
)

print("\nRun Steps:")
for step in run_steps.data:
    print(f"Step-ID: {step.id}, Typ: {step.type}, Status: {step.status}, Erstellungszeit: {step.created_at}")
    if hasattr(step.step_details, 'tool_calls'):
        for tool_call in step.step_details.tool_calls:
            print(f"Tool-Aufruf-ID: {tool_call.id}, Typ: {tool_call.type}")
            print(f"Eingabe: {tool_call.code_interpreter.input}")
            print(f"Ausgabe: {tool_call.code_interpreter.outputs[0].logs}")



for message in assistant_messages:
    text = message.content[0].text.value
    text = text.replace("\\(", "(").replace("\\)", ")")
    print(text)

# Aufräumen von Assistent und Thread
clean_up(assistant.id, thread.id)
