# 🧠 Multi-Agent Architecture: Financial News Impact Analyzer

This system implements a modular multi-agent design to assess the **market sentiment**, **expected impact**, and **volatility** of financial news articles using the Pydantic AI framework.

---

## 🧱 Why Multi-Agent?

A single monolithic model can be opaque and hard to interpret. By using **specialized agents**, each with clear responsibilities, we achieve:
- Better modularity and maintainability
- Human-readable intermediate outputs (e.g., sentiment, reasoning)
- More transparent error tracing and decision rationale

---

## 🧠 Agent Overview

### 🔹 Agent 1: `SentimentAnalyzer`

- **Input:** `headline`, `content`
- **Output:**
  - `sentiment`: Bullish / Bearish / Neutral
  - `reasoning`: Explanation of the detected tone

**Role:**  
Analyzes financial tone using keywords like “crushes”, “approval”, “turbulent times”, etc.

---

### 🔹 Agent 2: `ImpactForecaster`

- **Input:** Output from Agent 1 + inferred metadata (`company_size`, `topic`)
- **Output:**
  - `impact`: Low / Medium / High
  - `reasoning`: Logic based on company type and topic

**Role:**  
Estimates market impact of the news — i.e., how *important* or *material* it is from a business perspective.

**Key Rules:**
- Bullish + SmallCap → High impact
- Bearish + Regulation → High impact
- Others → Medium

---

### 🔹 Agent 3: `VolatilityEstimator` (Advanced Add-on)

- **Input:** Sentiment + Metadata (from earlier steps)
- **Output:**
  - `volatility`: Low / Medium / High
  - `reasoning`: Prediction of how sharp the stock's price movement might be

**Role:**  
Distinguishes **impact** (importance) from **volatility** (intensity of market movement).

**Key Rules:**
- SmallCap + strong sentiment → High volatility
- Neutral sentiment → Low/Medium volatility depending on topic

---

## 🔄 Agent Coordination Flow

```
Raw Article
   ↓
SentimentAnalyzer
   ↓
inferred metadata (company size + topic)
   ↓
┌────────────────────┬────────────────────┐
│   ImpactForecaster │ VolatilityEstimator│
└────────────────────┴────────────────────┘
```

---

## 🧪 Prompt Iteration Examples

### 1st Attempt — Sentiment misclassified:
```
Input Headline: "Small biotech soars on FDA approval"
Output: Neutral
Issue: Didn't recognize "soars" or "FDA approval" as bullish cues
Fix: Added those terms to positive keyword list
```

### 2nd Attempt — Volatility missing nuance:
```
Input: LargeCap + Regulation + Neutral
Output: Medium volatility
Fix: Adjusted to return Low since large-cap regulatory noise is often priced in
```

---

## 🧠 Design Rationale

- **Separation of Concerns:** Each agent focuses on one subtask, making the system easier to reason about.
- **Transparency:** All agents return human-readable explanations — useful for debugging and user-facing outputs.
- **Scalability:** Future agents can be added (e.g., Risk Scorer, Urgency Estimator) without breaking the current system.

---

## 🔚 Final Note

This system is designed to reflect how real-world financial analytics firms might combine multiple perspectives (tone, impact, volatility) to inform trading or business decisions.

The modular design also sets the stage for future improvement using LLM prompting or fine-tuned models in place of rules.

