from pydantic import BaseModel
from typing import Literal
from agents.sentiment_analyzer import SentimentResponse

class ArticleMeta(BaseModel):
    company_size: Literal["SmallCap", "MidCap", "LargeCap"]
    topic: Literal["Earnings", "Regulation", "M&A", "AI", "Other"]

class ImpactResponse(BaseModel):
    impact: Literal["Low", "Medium", "High"]
    reasoning: str

class ImpactForecaster:
    def forecast(self, sentiment: SentimentResponse, meta: ArticleMeta) -> ImpactResponse:
        if sentiment.sentiment == "Bullish" and meta.company_size == "SmallCap":
            return ImpactResponse(
                impact="High",
                reasoning="Small-cap companies tend to react more strongly to positive news."
            )
        elif sentiment.sentiment == "Bearish" and meta.topic == "Regulation":
            return ImpactResponse(
                impact="High",
                reasoning="Regulatory news usually triggers sharp movements."
            )
        else:
            return ImpactResponse(
                impact="Medium",
                reasoning="Moderate sentiment or company size implies medium expected impact."
            )
