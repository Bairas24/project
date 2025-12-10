# app/core/security.py

import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

def _sha256(password: str) -> str:
    """Предварительное хэширование для защиты длинных паролей."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def hash_password(password: str) -> str:
    """SHA256 → bcrypt."""
    sha = _sha256(password)
    return pwd_context.hash(sha)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Верификация: SHA256 → bcrypt.verify."""
    sha = _sha256(plain_password)
    return pwd_context.verify(sha, hashed_password)
