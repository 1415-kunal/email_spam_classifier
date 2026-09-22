import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📧",
    layout="centered"
)


st.title("📧 Email Spam Classifier")

st.write(
    "Enter an email below and our NLP model will classify it as "
    "SPAM or HAM."
)


email_text = st.text_area(
    "Enter Email",
    height=250,
    placeholder="Paste your email content here..."
)


if st.button("Predict", type="primary"):

    if not email_text.strip():
        st.warning("Please enter an email first.")

    else:
        try:
            response = requests.post(
                API_URL,
                json={"email": email_text}
            )

            if response.status_code == 200:

                result = response.json()
                prediction = result["prediction"]

                if prediction == "SPAM":
                    st.error("🚨 This email is classified as SPAM.")

                else:
                    st.success("✅ This email is classified as HAM.")

            else:
                st.error(
                    f"API Error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the FastAPI server. "
                "Make sure FastAPI is running."
            )