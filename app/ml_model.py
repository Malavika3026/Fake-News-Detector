import pickle

# Load trained model and vectorizer
model = pickle.load(open("fake_news_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def is_factual_statement(text: str) -> bool:
    """
    Detect short factual statements (not news articles)
    """
    return len(text.split()) < 8


def predict_news(text: str):
    """
    Predict fake or real news
    """
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)[0]
    confidence = model.predict_proba(vectorized_text)[0].max()

    label = "REAL" if prediction == 1 else "FAKE"
    return label, confidence, prediction
