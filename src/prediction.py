import joblib

from src.preprocessing import (
    lowercase_text,
    replace_urls,
    replace_email_addresses,
    remove_numbers,
    remove_punctuation,
    remove_stopwords
)


# Load trained model and TF-IDF vectorizer
vectorizer = joblib.load(
    "models/tfidf_vectorizer.pkl"
)

model = joblib.load(
    "models/spam_classifier.pkl"
)


def clean_text(text):
    """
    Apply the same preprocessing used during model training.
    """

    text = lowercase_text(text)
    text = replace_urls(text)
    text = replace_email_addresses(text)
    text = remove_numbers(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)

    return text


def predict_spam(email_text):
    """
    Predict whether an email is SPAM or HAM.
    """

    # Preprocess email
    cleaned_email = clean_text(email_text)

    # Convert email into TF-IDF features
    email_tfidf = vectorizer.transform([cleaned_email])

    # Make prediction
    prediction = model.predict(email_tfidf)[0]

    if prediction == 1:
        return "SPAM"

    return "HAM"