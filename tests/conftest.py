import os
import sys
import pytest
from fastapi.testclient import TestClient

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

@pytest.fixture
def client():
    """Test client using FastAPI's TestClient"""
    with TestClient(app) as client:
        yield client