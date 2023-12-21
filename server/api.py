from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.tokenizer import Tokenizer

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    Tokenized = Tokenizer()
    Tokenized.tokenize_string("the THE theTheTHE")

    return {"message": f"{Tokenized.token_map}"}
