from fastapi import FastAPI, HTTPException
from app.schemas import NewsRequest, NewsResponse
from app.ml_model import predict_news, is_factual_statement
from app.credibility import get_source_credibility
from app.explain import generate_explanation

app = FastAPI(title="Fake News Detector API")


@app.post("/analyze", response_model=NewsResponse)
def analyze_news(request: NewsRequest):

    if request.text.strip() == "":
        raise HTTPException(status_code=400, detail="News text cannot be empty")

    # Factual statement handling
    if is_factual_statement(request.text):
        return NewsResponse(
            final_result="FACTUAL STATEMENT",
            ml_prediction="N/A",
            ml_confidence=0.0,
            source_credibility=0.0,
            final_score=0.0,
            explanation=(
                "This input is a short factual statement and not a full news article. "
                "Fake news detection models require complete news content."
            )
        )

    # ---------------- ML Prediction ----------------
    ml_label, ml_confidence, raw_prediction = predict_news(request.text)

    # ---------------- Source Credibility ----------------
    source_score = get_source_credibility(request.source_url)

    # ---------------- Corrected Hybrid Scoring ----------------
    if raw_prediction == 1:  # REAL
        ml_score = ml_confidence
    else:  # FAKE
        ml_score = 1 - ml_confidence

    final_score = (0.7 * ml_score) + (0.3 * source_score)

    final_result = "REAL NEWS" if final_score > 0.6 else "FAKE NEWS"

    # ---------------- Return Response ----------------
    return NewsResponse(
        final_result=final_result,
        ml_prediction=ml_label,
        ml_confidence=round(ml_confidence, 2),
        source_credibility=round(source_score, 2),
        final_score=round(final_score, 2),
        explanation=generate_explanation(raw_prediction)
    )