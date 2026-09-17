from fastapi import FastAPI

from app.schemas import EmailRequest, PredictionResponse
from src.prediction import predict_spam


app = FastAPI(
    title="Email Spam Classifier API",
    description="API for classifying emails as SPAM or HAM using NLP and Machine Learning",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Email Spam Classifier API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_email(request: EmailRequest):

    prediction = predict_spam(request.email)

    return PredictionResponse(
        prediction=prediction,
        message=f"Email classified as {prediction}."
    )