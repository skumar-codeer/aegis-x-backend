def calculate_risk(phishing, creds):

    risk = 0

    if phishing["is_phishing"]:
        risk += phishing["confidence"] * 0.7

    if creds["credentials_found"]:
        risk += 30

    return min(100, round(risk))
