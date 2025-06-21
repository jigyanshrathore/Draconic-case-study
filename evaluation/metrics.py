def accuracy(predictions, ground_truths):
    correct = sum([pred == actual for pred, actual in zip(predictions, ground_truths)])
    return correct / len(predictions)

def disagreement_rate(sentiments, impacts):
    disagree_count = sum([
        1 for s, i in zip(sentiments, impacts)
        if (s == "Bullish" and i == "Low")
        or (s == "Bearish" and i == "High")
        or (s == "Neutral" and i != "Medium")  # assumes Neutral = Medium impact expectation
    ])
    return disagree_count / len(sentiments)


def explainability_score(reasons):
    return sum([1 for r in reasons if len(r.split()) > 10]) / len(reasons)
