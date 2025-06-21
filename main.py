from agents.sentiment_analyzer import Article, SentimentAnalyzer
from agents.impact_forecaster import ImpactForecaster, ArticleMeta
from agents.volatility_estimator import VolatilityEstimator
from evaluation.test_articles import test_articles
from evaluation.metrics import accuracy, disagreement_rate, explainability_score

def infer_metadata(headline, content):
    text = headline.lower() + content.lower()

    if "small-cap" in text or "biotech" in text or "small" in text:
        company_size = "SmallCap"
    elif "regional" in text or "mid" in text:
        company_size = "MidCap"
    else:
        company_size = "LargeCap"

    if "earnings" in text or "q2" in text or "q3" in text:
        topic = "Earnings"
    elif "fda" in text or "regulatory" in text or "approval" in text:
        topic = "Regulation"
    elif "ai" in text or "artificial intelligence" in text:
        topic = "AI"
    elif "merger" in text or "acquisition" in text:
        topic = "M&A"
    else:
        topic = "Other"

    return company_size, topic

def run_all():
    analyzer = SentimentAnalyzer()
    forecaster = ImpactForecaster()

    sentiments = []
    impacts = []
    reasons = []

    for article in test_articles:
        print(f"\n📰 Article ID: {article['article_id']}")
        print(f"🧾 Headline: {article['headline']}")

        # Agent 1
        article_obj = Article(headline=article['headline'], content=article['content'])
        sentiment = analyzer.analyze(article_obj)
        print(f"💬 Sentiment: {sentiment.sentiment} — {sentiment.reasoning}")
        sentiments.append(sentiment.sentiment)
        reasons.append(sentiment.reasoning)

        # Metadata Inference
        company_size, topic = infer_metadata(article['headline'], article['content'])

        # Agent 2
        meta = ArticleMeta(company_size=company_size, topic=topic)
        impact = forecaster.forecast(sentiment, meta)
        print(f"📈 Impact: {impact.impact} — {impact.reasoning}")
        impacts.append(impact.impact)

        # Agent 3:
        volatility_estimator = VolatilityEstimator()
        volatility = volatility_estimator.estimate(sentiment, meta)
        print(f" Volatility: {volatility.volatility} — {volatility.reasoning}")


    print("\n📊 Evaluation Metrics:")
    print(f"• Disagreement Rate: {disagreement_rate(sentiments, impacts):.2f}")
    print(f"• Explainability Score: {explainability_score(reasons):.2f}")
    print(f"• Accuracy: N/A — (need labeled ground truths)")

if __name__ == "__main__":
    run_all()
