from fastapi import APIRouter
from pydantic import BaseModel
from models.phishing_model import detect_phishing
from models.credential_detector import detect_credentials
from utils.risk_engine import calculate_risk

router = APIRouter(prefix="/analyze")

class TextRequest(BaseModel):
    text: str

@router.post("/text")
def analyze_text(req: TextRequest):

    phishing = detect_phishing(req.text)
    creds = detect_credentials(req.text)
    risk = calculate_risk(phishing, creds)

    explanation = []

    if phishing["is_phishing"]:
        explanation.append("Suspicious or urgent tone detected")

    if creds["credentials_found"]:
        explanation.append("Sensitive credential pattern found")

    if not explanation:
        explanation.append("No major threat indicators detected")

    return {
        "risk": risk,
        "phishing": phishing,
        "credentials": creds,
        "explanation": explanation
    }
