from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.tokenizer import Tokenizer
from server.predict import predict
from server.models.prediction import Prediction

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def tokenize(text: str) -> Prediction:
    Tokenized = Tokenizer()
    Tokenized.tokenize_string(text)
    dataframe = Tokenized.to_dataframe()

    return predict(dataframe)


@app.get("/")
async def root() -> dict:
    Tokenized = Tokenizer()
    Tokenized.tokenize_string("the THE theTheTHE")

    return {"message": f"{Tokenized.token_map}"}
