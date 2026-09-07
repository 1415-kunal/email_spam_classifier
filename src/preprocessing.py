import re
import string

import spacy
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# ============================================================
# Stopwords
# ============================================================

STOP_WORDS = set(stopwords.words("english"))


# ============================================================
# Stemming
# ============================================================

stemmer = PorterStemmer()


# ============================================================
# spaCy
# ============================================================

nlp = spacy.load("en_core_web_sm")


# ============================================================
# Basic Text Preprocessing
# ============================================================

def lowercase_text(text):
    """Convert text to lowercase."""
    return text.lower()


def remove_punctuation(text):
    """Remove punctuation characters from text."""
    return text.translate(
        str.maketrans("", "", string.punctuation)
    )


def remove_numbers(text):
    """Remove numeric characters from text."""
    return re.sub(r"\d+", "", text)


# ============================================================
# URL Handling
# ============================================================

URL_PATTERN = (
    r'https?\s*:\s*/\s*/\s*(?:www\s*\.\s*)?'
    r'[\w.-]+(?:\s*\.\s*[\w.-]+)+'
    r'|www\s*\.\s*[\w.-]+'
    r'(?:\s*\.\s*[\w.-]+)+'
)


def replace_urls(text):
    """Replace URLs with URL_TOKEN."""
    return re.sub(
        URL_PATTERN,
        "URL_TOKEN",
        text
    )


# ============================================================
# Email Address Handling
# ============================================================

EMAIL_PATTERN = (
    r'\b[\w.-]+\s*@\s*[\w.-]+'
    r'(?:\s*\.\s*[\w.-]+)+\b'
)


def replace_email_addresses(text):
    """Replace email addresses with EMAIL_TOKEN."""
    return re.sub(
        EMAIL_PATTERN,
        "EMAIL_TOKEN",
        text
    )


# ============================================================
# Stopword Handling
# ============================================================

def remove_stopwords(text):
    """Remove English stopwords from text."""
    words = text.split()

    filtered_words = [
        word
        for word in words
        if word.lower() not in STOP_WORDS
    ]

    return " ".join(filtered_words)


# ============================================================
# Tokenization
# ============================================================

def tokenize_text(text):
    """Tokenize text using spaCy."""
    doc = nlp(text)

    return [token.text for token in doc]


# ============================================================
# Stemming
# ============================================================

def stem_tokens(tokens):
    """Apply Porter stemming to a list of tokens."""
    return [
        stemmer.stem(token)
        for token in tokens
    ]


# ============================================================
# Lemmatization
# ============================================================

def lemmatize_text(text):
    """Return lemmatized tokens using spaCy."""
    doc = nlp(text)

    return [
        token.lemma_
        for token in doc
    ]