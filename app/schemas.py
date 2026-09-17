from pydantic import BaseModel, Field


class EmailRequest(BaseModel):
    email: str = Field(
        ...,
        min_length=1,
        description="Email text to classify"
    )


class PredictionResponse(BaseModel):
    prediction: str
    message: str