import requests
from core.config import MISTRAL_API_KEY

def transform_to_structure(prompt: str) -> dict:
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-medium",
        "messages": [
            {
                "role": "system",
                "content": "Extract actors, entities, and relationships in strict JSON format."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    content = data["choices"][0]["message"]["content"]

    try:
        return eval(content)
    except:
        return {
            "actors": [],
            "entities": [],
            "relationships": []
        }