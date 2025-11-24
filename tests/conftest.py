import os
import sys
import pytest
from fastapi.testclient import TestClient

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

# Test DB URL from environment as required by Issue 10
TEST_DB_URL = os.getenv("TEST_DB_URL", "postgresql+asyncpg://admin:123456@localhost:5432/test_db")

# Override database settings to use TEST_DB_URL
import app.core.settings as settings
settings.ASYNC_DATABASE_URL = TEST_DB_URL

@pytest.fixture
def client():
    """Test client using FastAPI's TestClient"""
    with TestClient(app) as client:
        yield client