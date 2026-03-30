import pytest


@pytest.mark.asyncio
async def test_register_user(client):
    res = await client.post(
        "auth/register",
        json={"username": "testuser", "fullname": "Test User", "password": "secret123"},
    )
    assert res.status_code == 201
    data = res.json()
    assert data["username"] == "testuser"
    assert "id" in data


@pytest.mark.asyncio
async def test_login_user(client):
    await client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "fullname": "Login User",
            "password": "secret123",
        },
    )
    res = await client.post(
        "/auth/login", json={"username": "loginuser", "password": "secret123"}
    )
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_task_create_and_list(client):
    await client.post(
        "/auth/register",
        json={"username": "taskuser", "fullname": "Task User", "password": "secret123"},
    )
    login = await client.post(
        "/auth/login", json={"username": "taskuser", "password": "secret123"}
    )
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    res = await client.post(
        "/tasks/",
        json={"title": "My Task", "description": "Test task"},
        headers=headers,
    )
    assert res.status_code == 201

    res = await client.get("/tasks/", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert len(data) >= 1
