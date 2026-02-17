import re

SUSPICIOUS_KEYWORDS = [
    "urgent",
    "verify",
    "account suspended",
    "click here",
    "immediately",
    "password",
    "bank",
    "otp",
]

def detect_phishing(text: str):

    score = 0
    found = []

    for word in SUSPICIOUS_KEYWORDS:
        if re.search(word, text, re.IGNORECASE):
            score += 15
            found.append(word)

    is_phishing = score >= 30

    return {
        "is_phishing": is_phishing,
        "confidence": min(score, 100),
        "keywords": found
    }
