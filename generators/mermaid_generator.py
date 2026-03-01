from domain.model_state import model_state

def generate_mermaid():
    diagram = "classDiagram\n"

    for entity in model_state.entities:
        diagram += f"class {entity}\n"

    for rel in model_state.relationships:
        diagram += f"{rel['from']} --> {rel['to']} : {rel['type']}\n"

    return diagram