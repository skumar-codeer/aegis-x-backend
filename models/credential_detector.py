import re

PATTERNS = [
    r"password\s*[:=]",
    r"otp\s*[:=]",
    r"ssn",
    r"cvv",
    r"account\s*number",
    r"verify\s*your\s*account"
]

def detect_credentials(text: str):

    matches = []

    for pattern in PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            matches.append(pattern)

    return {
        "credentials_found": len(matches) > 0,
        "matches": matches
    }
