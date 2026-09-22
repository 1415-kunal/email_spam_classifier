import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000/predict"


st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📧",
    layout="centered"
)


st.title("📧 Email Spam Classifier")

st.markdown(
    """
    Enter the content of an email below and the trained NLP model
    will classify it as **SPAM** or **HAM**.
    """
)


email_text = st.text_area(
    "Email Content",
    height=250,
    placeholder="Paste your email content here..."
)


col1, col2 = st.columns(2)


with col1:
    predict_button = st.button(
        "🔍 Predict",
        use_container_width=True
    )


with col2:
    clear_button = st.button(
        "🗑️ Clear",
        use_container_width=True
    )


if clear_button:
    st.rerun()


if predict_button:

    if not email_text.strip():

        st.warning(
            "Please enter an email before making a prediction."
        )

    else:

        try:
            with st.spinner("Analyzing email..."):

                response = requests.post(
                    API_URL,
                    json={"email": email_text},
                    timeout=10
                )

            if response.status_code == 200:

                result = response.json()
                prediction = result["prediction"]

                st.divider()

                if prediction == "SPAM":

                    st.error(
                        "🚨 This email is classified as SPAM."
                    )

                else:

                    st.success(
                        "✅ This email is classified as HAM."
                    )

            else:

                st.error(
                    f"API returned an error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to the FastAPI server. "
                "Please make sure the FastAPI server is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ The API request timed out. Please try again."
            )