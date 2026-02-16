from urllib.request import Request
from fastapi import FastAPI
from pydantic import BaseModel
from rag import ask_law_question
app = FastAPI()
class Question(BaseModel):
    question: str
@app.post("/ask")
def ask_question(query: Question):
    print("1.")
    answer = ask_law_question(query.question)
    return {"answer": answer}