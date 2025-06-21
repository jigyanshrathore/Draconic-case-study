from pydantic import BaseModel
from typing import Literal
from agents.sentiment_analyzer import SentimentResponse
from agents.impact_forecaster import ArticleMeta

class VolatilityResponse(BaseModel):
    volatility: Literal["Low", "Medium", "High"]
    reasoning: str

class VolatilityEstimator:
    def estimate(self, sentiment: SentimentResponse, meta: ArticleMeta) -> VolatilityResponse:
        if sentiment.sentiment != "Neutral" and meta.company_size == "SmallCap":
            return VolatilityResponse(
                volatility="High",
                reasoning="Small-cap stocks tend to show high volatility in reaction to sentiment-driven news."
            )
        elif meta.topic == "Earnings" and sentiment.sentiment == "Neutral":
            return VolatilityResponse(
                volatility="Medium",
                reasoning="Neutral sentiment in earnings reports typically results in mild fluctuations."
            )
        else:
            return VolatilityResponse(
                volatility="Low",
                reasoning="The news is unlikely to trigger strong market movements."
            )
