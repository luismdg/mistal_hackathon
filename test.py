import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
        "Content-Type": "application/json"
    },
    json={
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": "Say hello"}]
    }
)

print(response.json())