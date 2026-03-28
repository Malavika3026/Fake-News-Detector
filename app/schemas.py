from pydantic import BaseModel

from typing import Optional

class NewsRequest(BaseModel):
    text: str
    source_url: Optional[str] = None



class NewsResponse(BaseModel):
    final_result: str
    ml_prediction: str
    ml_confidence: float
    source_credibility: float
    final_score: float
    explanation: str
