from passlib.context import CryptContext

# Use sha256_crypt which works reliably
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hash password for storage"""
    print(f"🔐 SECURITY: Hashing password: '{password}'")
    hashed = pwd_context.hash(password)
    print(f"🔐 SECURITY: Hash result: {hashed}")
    return hashed

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    print(f"🔐 SECURITY: Verifying password: '{plain_password}'")
    print(f"🔐 SECURITY: Against hash: {hashed_password}")
    result = pwd_context.verify(plain_password, hashed_password)
    print(f"🔐 SECURITY: Verification result: {result}")
    return result