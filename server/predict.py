import pickle
import pandas as pd
from server.models.prediction import Prediction


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
