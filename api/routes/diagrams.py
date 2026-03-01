from fastapi import APIRouter
from generators.mermaid_generator import generate_mermaid

router = APIRouter()

@router.get("/diagram")
def get_diagram():
    return {"mermaid": generate_mermaid()}