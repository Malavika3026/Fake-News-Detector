# 📰 Fake News Detector using Machine Learning

## Overview
The rapid spread of misinformation across digital platforms has made automated fake news detection a critical problem.  
This project presents a machine learning-based system to classify news articles as **Fake** or **Real** using natural language processing techniques.

The solution combines **TF-IDF feature extraction** with a **Logistic Regression classifier**, achieving high accuracy while remaining lightweight and efficient.  
The project is implemented as a complete pipeline with both backend and frontend components for real-time prediction.

---

## 🚀 Key Features
- Text preprocessing (cleaning, tokenization, stopword removal)
- TF-IDF vectorization for feature extraction
- Logistic Regression for binary classification
- Model evaluation using Accuracy, AUC, ROC, and Confusion Matrix
- FastAPI backend for real-time inference
- Streamlit interface for interactive user input
- Lightweight and scalable architecture

---

## 🧠 Model Details
- **Algorithm:** Logistic Regression  
- **Feature Extraction:** TF-IDF (max_features = 5000)  
- **Dataset:** Fake.csv & True.csv  
- **Task:** Binary Classification (Fake vs Real)

---

## 📊 Results
| Metric        | Value       |
|---------------|-------------|
| Accuracy      | 98.93%      |
| AUC Score     | 0.999       |
| Log Loss      | 0.058       |
| Training Time | 0.36 sec    |

The model demonstrates strong class separation and reliable performance on high-dimensional textual data.

---

## 🏗️ System Architecture
User Input → Preprocessing → TF-IDF → Logistic Regression → FastAPI → Streamlit UI
- **Frontend:** Streamlit (user interaction)
- **Backend:** FastAPI (model inference)
- **Model:** Scikit-learn

---

## 🛠️ Tech Stack
- Python  
- Scikit-learn  
- Pandas, NumPy  
- Matplotlib  
- FastAPI  
- Streamlit  

---

## 📂 Project Structure
FakeNews/
│
├── app/ # FastAPI backend
│ ├── main.py # API endpoints
│ ├── ml_model.py # Model inference logic
│ ├── credibility.py # Source credibility scoring
│ ├── explain.py # Prediction explanation
│ ├── schemas.py # Request/response models
│ └── __init__.py
│
├── app.py # Streamlit frontend (UI)
├── train_model.py # Model training script
├── fake_news_model.pkl # Trained Logistic Regression model
├── vectorizer.pkl # TF-IDF vectorizer
├── Fake.csv # Fake news dataset
├── True.csv # Real news dataset
├── requirements.txt # Dependencies
└── README.md

---

## ▶️ How to Run
### 1. Clone the Repository
git clone https://github.com/Malavika3026/Fake-News-Detector.git
cd Fake-News-Detector

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Application

#### FastAPI Backend :- uvicorn app.main:app --reload
#### Streamlit Frontend :- streamlit run app.py

---

## 📌 Key Insights
- Logistic Regression performs exceptionally well on TF-IDF features for text classification.
- The model achieves near-perfect AUC, indicating strong discriminative capability.
- Lightweight machine learning models can outperform complex architectures in structured NLP tasks.

---

## 🔮 Future Improvements
- Integrate transformer-based models (BERT, RoBERTa)
- Add multilingual fake news detection
- Extend to multimodal detection (text + images + metadata)
- Deploy as a cloud-based application

---

## 📎 Acknowledgment
Developed as part of academic coursework in **Machine Learning**, focusing on practical implementation and deployment of NLP-based classification systems.
