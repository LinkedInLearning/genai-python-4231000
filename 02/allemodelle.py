from openai import OpenAI
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPEN_API_KEY")
)

models = client.models.list()
for model in models:
    created_at = datetime.fromtimestamp(model.created)
    print("Model ID:", model.id)
    print("Model Created At:", created_at.strftime("%Y-%m-%d %H:%M:%S"))
    print("owned_by:", model.owned_by)
    print("-----")