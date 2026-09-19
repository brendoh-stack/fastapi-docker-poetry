from fastapi import FastAPI
import os

app = FastAPI(title="FastAPI Containerizado")

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "mensagem": "FastAPI rodando dentro do Docker com Poetry com sucesso!",
        "ambiente": os.getenv("ENV", "Não definido")
    }
