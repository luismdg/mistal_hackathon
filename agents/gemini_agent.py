from google import genai
from core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def clarify_prompt(prompt: str) -> dict:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"""
                    You are a requirements clarification assistant.

                    If the following project description is ambiguous,
                    ask ONE concise clarification question.

                    If it is clear enough to extract structured elements,
                    respond only with the word: CLEAR

                    Project description:
                    {prompt}
                """
    )

    text = response.text.strip()

    if "CLEAR" in text.upper():
        return {"needs_clarification": False}
    else:
        return {
            "needs_clarification": True,
            "question": text
        }