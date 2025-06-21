from pydantic import BaseModel
from typing import Literal

class Article(BaseModel):
    headline: str
    content: str

class SentimentResponse(BaseModel):
    sentiment: Literal["Bullish", "Bearish", "Neutral"]
    reasoning: str

class SentimentAnalyzer:
    def analyze(self, article: Article) -> SentimentResponse:
        headline = article.headline.lower()
        content = article.content.lower()
        combined = headline + " " + content

        if any(word in combined for word in ["crushes", "beats", "soars", "record profits", "stellar growth", "approval", "record earnings"]):
            sentiment = "Bullish"
            reason = "Positive financial or regulatory language found in text."
        elif any(word in combined for word in ["warns", "massive cost", "turbulent times", "remain skeptical", "regulatory clouds", "loss", "plummet"]):
            sentiment = "Bearish"
            reason = "Negative or uncertain terms detected in text."
        else:
            sentiment = "Neutral"
            reason = "No strong positive or negative signals found."

        return SentimentResponse(
            sentiment=sentiment,
            reasoning=reason
        )

