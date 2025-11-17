from passlib.context import CryptContext

# Update the schemes from "bcrypt" to "sha256_crypt"
pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    # This call failed previously, switching the scheme should fix it.
    return pwd_context.hash(password)