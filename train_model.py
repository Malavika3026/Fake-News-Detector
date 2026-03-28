import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# -----------------------------
# 1. Load datasets
# -----------------------------
fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

# -----------------------------
# 2. Add labels
# -----------------------------
fake_df["label"] = 0   # FAKE
true_df["label"] = 1   # REAL

# -----------------------------
# 3. Combine datasets
# -----------------------------
data = pd.concat([fake_df, true_df], axis=0)

# Shuffle data
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# -----------------------------
# 4. Select features & labels
# -----------------------------
X = data["text"]
y = data["label"]

# -----------------------------
# 5. Vectorization (TF-IDF)
# -----------------------------
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# -----------------------------
# 6. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# -----------------------------
# 7. Train model
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# -----------------------------
# 8. Save model & vectorizer
# -----------------------------
pickle.dump(model, open("fake_news_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model training completed successfully.")
