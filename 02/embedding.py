from openai import OpenAI
from numpy import dot
from numpy.linalg import norm
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPEN_API_KEY")
)

input1 = "Ich mag Bananen"
input2 = "Ich esse gerne Bananen"
input3 = "Die Katze jagt die Maus."

# Erstelle Embeddings für jeden Text
result1 = client.embeddings.create(model="text-embedding-3-small", input=input1)
result2 = client.embeddings.create(model="text-embedding-3-small", input=input2)
result3 = client.embeddings.create(model="text-embedding-3-small", input=input3)

# Extrahiere die Embeddings aus den Ergebnissen
embedding1 = result1.data[0].embedding
embedding2 = result2.data[0].embedding
embedding3 = result3.data[0].embedding

# Embeddings vergleichen
def compare_two_embeddings(a, b):
  cos_sim = dot(a, b)/(norm(a)*norm(b))
  return cos_sim

# Berechne die Ähnlichkeit der Embeddings
similarity_1_2 = compare_two_embeddings(embedding1, embedding2) 
similarity_1_3 = compare_two_embeddings(embedding1, embedding3) 
similarity_2_3 = compare_two_embeddings(embedding2, embedding3) 

print("Ähnlichkeit zwischen Text 1 und Text 2:", similarity_1_2)
print("Ähnlichkeit zwischen Text 1 und Text 3:", similarity_1_3)
print("Ähnlichkeit zwischen Text 2 und Text 3:", similarity_2_3)