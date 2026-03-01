from fastapi import FastAPI
from api.routes import chat, diagrams, export, speech

app = FastAPI()

app.include_router(chat.router)
app.include_router(diagrams.router)
app.include_router(export.router)
app.include_router(speech.router)