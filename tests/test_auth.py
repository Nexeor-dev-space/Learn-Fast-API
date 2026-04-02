import pytest

@pytest.mark.asyncio
async def test_register_user(client):
    payload = {
        "username": "testuser",
        "fullname": "Test User",
        "password": "secret123"
    }
    resp = await client.post("/auth/register", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["username"] == "testuser"
    assert "id" in data

@pytest.mark.asyncio
async def test_login_user(client):
    await client.post("/auth/register", json={
        "username": "loginuser",
        "fullname": "Login User",
        "password": "secret123"
    })

    resp = await client.post("/auth/login", data={
        "username": "loginuser",
        "password": "secret123"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
