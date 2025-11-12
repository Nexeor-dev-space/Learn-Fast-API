from passlib.context import CryptContext

# Define the hashing scheme
# bcrypt is the recommended scheme for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to get the hashed password
def get_password_hash(password: str) -> str:
    """Hashes a plain-text password."""
    return pwd_context.hash(password)

# Function to verify the password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain-text password against a stored hash."""
    return pwd_context.verify(plain_password, hashed_password)
