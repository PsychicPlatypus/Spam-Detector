from pydantic import BaseModel, Field


class Prediction(BaseModel):
    prediction: int = Field(...)
    confidence: float = Field(...)
    model: str = Field(...)
    version: str = Field(default="1.0.0")
    created_at: str = Field(...)
    updated_at: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "prediction": 0,
                "confidence": 0.9824223750137148,
                "model": "Stacking Classifier(RF, SVC, GB -> LR)",
                "version": "1.0.0",
                "created_at": "2023-12-23 00:00:00",
                "updated_at": "2021-12-23 00:00:00",
            }
        }
