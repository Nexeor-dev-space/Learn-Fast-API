import pytest

@pytest.mark.asyncio
async def test_create_and_list_tasks(client):
    await client.post("/auth/register", json={
        "username": "taskuser",
        "fullname": "Task User",
        "password": "secret123"
    })

    login = await client.post("/auth/login", data={
        "username": "taskuser",
        "password": "secret123"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    resp = await client.post("/tasks/", json={
        "title": "Test Task",
        "description": "Test Description",
        "completed": False
    }, headers=headers)
    assert resp.status_code == 201

    resp = await client.get("/tasks/", headers=headers)
    assert resp.status_code == 200
    tasks = resp.json()
    assert len(tasks) >= 1
