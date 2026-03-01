from agents.gemini_agent import clarify_prompt
from agents.mistral_transformer import transform_to_structure
from domain.model_state import model_state

def process_message(message: str):
    clarification = clarify_prompt(message)

    if clarification["needs_clarification"]:
        return {
            "type": "clarification",
            "content": clarification["question"]
        }

    structured = transform_to_structure(message)

    model_state.add_story(message)
    model_state.update_from_extraction(structured)

    return {
        "type": "success",
        "stories": model_state.user_stories,
        "actors": model_state.actors,
        "entities": model_state.entities,
        "relationships": model_state.relationships
    }