from fastapi import APIRouter
from fastapi.responses import FileResponse
from generators.pdf_generator import generate_pdf

router = APIRouter()

@router.get("/export/pdf")
def export_pdf():
    path = generate_pdf()
    return FileResponse(path, media_type="application/pdf", filename="requirements.pdf")