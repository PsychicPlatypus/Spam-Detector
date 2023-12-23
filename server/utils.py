import pickle
import pandas as pd
from server.models.prediction import Prediction
from pydantic import BaseModel, Field


class DefaultRequest(BaseModel):
    text: str = Field(
        examples=[
            "\nSubject: enron methanol ;\nmeter # : 988291\r\n\nthis is a follow up to the note i gave you on monday, 4 / 3 / 00 { preliminary\r\n\nflow data provided by daren } .\r\n\nplease override pop ' s daily volume { presently zero } to reflect daily\r\n\nactivity you can obtain from gas control .\r\n\nthis change is needed asap for economics purposes .\n            "
        ]
    )


def predict(df: pd.DataFrame) -> Prediction:
    model = pickle.load(open(f"models/clf.sav", "rb"))
    prediction = model.predict(df)

    return Prediction(
        prediction=prediction[0],
        confidence=model.predict_proba(df).max(),
        model="Stacking Classifier(RF, SVC, GB -> LR)",
        created_at="2023-12-23 00:00:00",
        updated_at="2021-12-23 00:00:00",
    )
