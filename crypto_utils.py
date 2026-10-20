import hashlib

def generate_audit_token(seed: str) -> str:
    return hashlib.sha256(seed.encode()).hexdigest()[:32].upper()
