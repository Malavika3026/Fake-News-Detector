import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detector")
st.write("Streamlit UI → FastAPI → ML")

news_text = st.text_area("📝 Enter News Text", height=200)
news_url = st.text_input("🔗 News Source URL")

if st.button("Analyze News"):
    if news_text.strip() == "":
        st.warning("Please enter news text.")
    else:
        payload = {
            "text": news_text,
            "source_url": news_url
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.subheader("✅ Result")
            st.write(f"**Final Decision:** {result['final_result']}")
            st.write(f"**ML Prediction:** {result['ml_prediction']}")
            st.write(f"**ML Confidence:** {result['ml_confidence']}")
            st.write(f"**Source Credibility:** {result['source_credibility']}")
            st.write(f"**Final Score:** {result['final_score']}")

            st.subheader("🧠 Analysis")
            st.info(result["explanation"])
        else:
            st.error("Error connecting to API")
