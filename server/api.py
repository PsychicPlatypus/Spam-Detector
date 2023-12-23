from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.tokenizer import Tokenizer
from server.utils import predict, DefaultRequest
from server.models.prediction import Prediction

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
async def tokenize(request: DefaultRequest) -> Prediction:
    Tokenized = Tokenizer()
    Tokenized.tokenize_string(request.text)
    dataframe = Tokenized.to_dataframe()

    return predict(dataframe)
