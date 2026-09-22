# 🚀 Email Spam Classifier

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)

![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn)

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)

![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)

![NLP](https://img.shields.io/badge/NLP-Text%20Classification-purple?style=for-the-badge)

**An End-to-End NLP and Machine Learning System for Classifying Emails as SPAM or HAM**

</div>

---

# 📌 Project Overview

Email spam is a common problem where unwanted or malicious messages can make it difficult to identify genuine emails.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to classify an email as either **SPAM** or **HAM (legitimate email)**.

The project focuses on understanding how different NLP preprocessing techniques and text vectorization methods affect machine learning performance.

The complete workflow includes:

- Data Exploration
- Text Preprocessing
- NLP Experiments
- Text Vectorization
- N-Gram Experiments
- Machine Learning
- Model Evaluation
- Error Analysis
- Final Model Selection
- FastAPI Backend
- Streamlit Frontend

---

# ✨ Features

- 📧 Email SPAM/HAM Classification
- 🧹 Text Preprocessing
- 🔤 Lowercasing
- 🔗 URL Replacement
- 📩 Email Address Replacement
- 🔢 Number Removal
- ✂️ Punctuation Removal
- 🚫 Stopword Removal
- 🌱 Stemming
- 🧠 Lemmatization
- 📊 Bag of Words
- 0️⃣ Binary Bag of Words
- 📈 TF-IDF Vectorization
- 🔤 Word N-Grams
- 🔡 Character N-Grams
- 🤖 Multiple ML Models
- 📊 Model Comparison
- 🔍 Error Analysis
- ⚡ FastAPI REST API
- 🖥️ Streamlit Web Interface

---

# 🖥️ Application

The project includes a web interface where users can enter an email message and classify it as:

**SPAM**

or

**HAM**

The Streamlit frontend communicates with the FastAPI backend through a REST API.

---

# 🏗️ Project Architecture

```text
                    User Email
                        │
                        ▼
                Streamlit Frontend
                        │
                  HTTP Request
                        │
                        ▼
                 FastAPI Backend
                        │
                        ▼
                Text Preprocessing
                        │
                        ├── Lowercase
                        ├── URL Replacement
                        ├── Email Replacement
                        ├── Number Removal
                        ├── Punctuation Removal
                        └── Stopword Removal
                        │
                        ▼
                  TF-IDF Vectorizer
                        │
                        ▼
                  LinearSVC Model
                        │
                        ▼
                  SPAM / HAM Result
```

---

# 📂 Project Structure

```text
email_spam_classifier/

│
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── frontend.py
│
├── src/
│   ├── preprocessing.py
│   └── prediction.py
│
├── models/
│   ├── tfidf_vectorizer.pkl
│   └── spam_classifier.pkl
│
├── data/
│   └── raw/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing_experiments.ipynb
│   ├── 03_vectorization_experiments.ipynb
│   ├── 04_controlled_experiments.ipynb
│   ├── 05_cleaned_modeling.ipynb
│   ├── 06_error_analysis.ipynb
│   └── 07_final_model.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📊 Dataset

Dataset Used:

**NLP - SPAM/HAM Email Classification**

The dataset contains email text along with its corresponding class label.

| Label | Description |
|-------|-------------|
| 0 | HAM |
| 1 | SPAM |

### Dataset Statistics

- Total Emails: **5,728**
- HAM: **4,360**
- SPAM: **1,368**
- HAM Percentage: **76.12%**
- SPAM Percentage: **23.88%**

The dataset contains both legitimate and spam email messages with different writing styles, URLs, email addresses, promotional content and other textual patterns.

---

# ⚙️ Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Exploration
   │
   ▼
Text Preprocessing
   │
   ├── Lowercasing
   ├── URL Replacement
   ├── Email Replacement
   ├── Number Removal
   ├── Punctuation Removal
   └── Stopword Removal
   │
   ▼
Vectorization
   │
   ├── Bag of Words
   ├── Binary Bag of Words
   ├── TF-IDF
   ├── Word N-Grams
   └── Character N-Grams
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Error Analysis
   │
   ▼
Final Model
```

---

# 🧹 Text Preprocessing

Different preprocessing techniques were studied independently instead of assuming that every preprocessing step improves performance.

### Techniques Explored

- Lowercasing
- Punctuation removal
- Number removal
- URL replacement
- Email address replacement
- Stopword removal
- Tokenization
- Porter Stemming
- spaCy Lemmatization

### Example

```text
Original:
Congratulations! Visit http : / / www . example . com today.

Processed:
congratulations visit URL_TOKEN today
```

URLs and email addresses were replaced with tokens so that their presence could still provide useful information to the model.

---

# 🔢 Text Vectorization

Several text representation techniques were experimented with.

### Bag of Words

Represents text using word occurrence counts.

### Binary Bag of Words

Represents whether a word is present or absent instead of storing its frequency.

### TF-IDF

Assigns higher importance to words that are useful for distinguishing documents.

### Word N-Grams

Experiments were performed with:

- Unigrams
- Bigrams
- Unigram + Bigram
- Unigram + Bigram + Trigram

### Character N-Grams

Character-level TF-IDF features were also explored.

These experiments helped understand how the choice of text representation affects classification performance.

---

# 🤖 Models Evaluated

The following machine learning algorithms were tested:

- Naive Bayes
- Logistic Regression
- Linear Support Vector Classifier
- Random Forest

Different combinations of:

- Preprocessing
- Vectorization
- N-Grams
- Classification algorithms

were compared using the same train-test split.

---

# 📈 Model Comparison

Some important experimental results are shown below.

| Preprocessing | Vectorizer | Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---:|---:|---:|---:|
| Clean A | TF-IDF | LinearSVC | **0.9956** | **0.9927** | **0.9891** | **0.9909** |
| Clean C | TF-IDF | LinearSVC | 0.9930 | 0.986? | 0.984? | **0.9854** |
| Clean A | Binary BoW | Naive Bayes | 0.9930 | — | — | **0.9853** |
| Clean A | Word 1-2 TF-IDF | LinearSVC | 0.9921 | — | — | 0.9834 |
| Clean A | BoW | Logistic Regression | 0.9913 | — | — | 0.9818 |
| Clean B | TF-IDF | LinearSVC | 0.9913 | — | — | 0.9817 |
| Clean A | Character 3-5 TF-IDF | LinearSVC | 0.9904 | — | — | 0.9799 |

The experiments showed that the preprocessing and vectorization strategy can have a significant effect on model performance.

---

# 🏆 Final Model

The final selected configuration was:

```text
Preprocessing:
Clean A

Vectorization:
TF-IDF

Classifier:
LinearSVC
```

### Final Performance

| Metric | Score |
|---|---:|
| Accuracy | **99.56%** |
| Precision | **99.27%** |
| Recall | **98.91%** |
| F1 Score | **99.09%** |

The final model was trained using:

```python
LinearSVC(
    max_iter=5000,
    random_state=42
)
```

The trained classifier and TF-IDF vectorizer were saved using Joblib.

---

# 🔍 Error Analysis

The final model was evaluated on **1,146 test emails**.

### Confusion Matrix

```text
                 Predicted
               HAM      SPAM

Actual HAM     870       2

Actual SPAM      3     271
```

### Results

- True Negatives: **870**
- False Positives: **2**
- False Negatives: **3**
- True Positives: **271**
- Total Errors: **5**

### False Positives

The false positives were legitimate newsletter/business emails containing patterns commonly associated with spam, such as:

- Multiple URLs
- Email addresses
- Promotional language
- Subscription information

### False Negatives

The false negatives were mostly short or unusual spam messages.

Short emails provide fewer textual features, which can make classification more difficult.

---

# 🚀 API Endpoints

The project provides a FastAPI REST API.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API Home |
| GET | `/health` | Health Check |
| POST | `/predict` | Classify an Email |

### Example Request

```json
{
    "email": "Congratulations! You have won a free prize. Click here to claim."
}
```

### Example Response

```json
{
    "prediction": "SPAM",
    "message": "Email classified as SPAM."
}
```

---

# ⚡ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Move into the Project

```bash
cd email_spam_classifier
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

# ▶️ Running the Application

### Start FastAPI

```bash
uvicorn app.main:app --reload
```

FastAPI documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

### Start Streamlit

Open another terminal and run:

```bash
streamlit run app/frontend.py
```

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- LinearSVC
- Logistic Regression
- Naive Bayes
- Random Forest

### NLP

- NLTK
- spaCy
- Porter Stemmer
- TF-IDF
- Bag of Words
- N-Grams

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- Streamlit

### Data Processing

- Pandas
- NumPy

### Model Storage

- Joblib

---

# 📚 Project Learning Focus

This project was designed not only to build a spam classifier, but also to understand the complete NLP workflow.

The main learning areas include:

- How raw email text is processed
- How URLs and email addresses can be handled
- How stopwords affect text representation
- Difference between stemming and lemmatization
- Difference between BoW and TF-IDF
- Binary feature representation
- Word and character N-Grams
- Sparse matrices
- Feature explosion
- Train-test vectorization without data leakage
- Model comparison
- Error analysis
- Saving and loading trained ML models
- Serving an ML model through FastAPI
- Building a frontend using Streamlit

---

# 🔮 Future Improvements

- Improve handling of very short spam emails
- Experiment with advanced NLP models
- Add probability/confidence estimation
- Add batch email prediction
- Add more real-world spam datasets
- Add model explainability
- Improve frontend features
- Deploy the application to the cloud
- Add automated testing
- Add CI/CD pipeline

---

# 👨‍💻 Author

## Kunal Walunj

Machine Learning & AI Enthusiast

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps support the project and encourages further development.