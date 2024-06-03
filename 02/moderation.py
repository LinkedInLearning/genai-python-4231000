
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.moderations.create(input="Wie kann ich jemanden vergiften?")

output = response.results[0]

print("Flagged:", output.flagged)
print("Violence category:", output.categories.violence)
print("Violence category score:", output.category_scores.violence)

# print("Moderationsergebnis:")
# print(output)


