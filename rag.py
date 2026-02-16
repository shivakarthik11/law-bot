from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import ollama
read=PdfReader("data/constitution.pdf")
fulltext=""
for page in read.pages:
    text = page.extract_text()
    if text:
        fulltext=fulltext+text+"\n"

chunks=[]
chunksize=1000
for i in range(0,len(fulltext),chunksize):
    chunk=fulltext[i:i+chunksize]
    chunks.append(chunk)



model=SentenceTransformer("all-MiniLM-L6-v2")
embeddings=model.encode(chunks)



client=chromadb.Client()
collection = client.get_or_create_collection(name="constitution")
for i in range(len(chunks)):
    collection.add(
        ids=[str(i)],
        embeddings=[embeddings[i]],
        documents=[chunks[i]],
    )



def ask_law_question(question: str):
    print("2.")

    question_embedding = model.encode(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3,
    )
    print("3.")

    retriveddata = "\n\n".join(results["documents"][0])
    promt = f"""
Give a detailed answer based on the give information provided.
do not use any poetry.
context : {retriveddata}
question : {question}
"""
    print("4.")

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {"role": "user", "content": promt}
        ]
    )
    return response["message"]["content"]