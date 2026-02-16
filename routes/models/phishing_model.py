from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def detect_phishing(text: str):

    result = classifier(text)[0]

    score = result["score"] * 100
    label = result["label"]

    is_phishing = label == "NEGATIVE"

    return {
        "is_phishing": is_phishing,
        "confidence": round(score, 2)
    }
