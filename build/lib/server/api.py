from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.utils import Tokenizer
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": f"{Tokenizer().token_map}"}
