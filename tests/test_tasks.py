

def test_create_task(client):
    payload = {"title": "Study FastAPI", "description": "Learn routing", "estimated_time": 60}
    response = client.post("/api/v1/tasks/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Study FastAPI"
    assert data["completed"] is False
    assert data["estimated_time"] == 60
    assert "id" in data
    assert "created_at" in data


def test_list_tasks(client):
    client.post("/api/v1/tasks/", json={"title": "Task 1", "estimated_time": 30})
    client.post("/api/v1/tasks/", json={"title": "Task 2", "estimated_time": 45})
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_get_task(client):
    create = client.post("/api/v1/tasks/", json={"title": "My Task", "estimated_time": 20})
    task_id = create.json()["id"]
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "My Task"


def test_update_task(client):
    create = client.post("/api/v1/tasks/", json={"title": "Old Title", "estimated_time": 10})
    task_id = create.json()["id"]
    response = client.put(f"/api/v1/tasks/{task_id}", json={"title": "New Title"})
    assert response.status_code == 200
    assert response.json()["title"] == "New Title"


def test_complete_task(client):
    create = client.post("/api/v1/tasks/", json={"title": "Finish me", "estimated_time": 15})
    task_id = create.json()["id"]
    response = client.patch(f"/api/v1/tasks/{task_id}/complete")
    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task(client):
    create = client.post("/api/v1/tasks/", json={"title": "Delete me", "estimated_time": 5})
    task_id = create.json()["id"]
    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 204
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 404


def test_task_not_found(client):
    response = client.get("/api/v1/tasks/9999")
    assert response.status_code == 404


def test_invalid_task_empty_title(client):
    response = client.post("/api/v1/tasks/", json={"title": "", "estimated_time": 10})
    assert response.status_code == 422


def test_invalid_task_blank_title(client):
    response = client.post("/api/v1/tasks/", json={"title": "   ", "estimated_time": 10})
    assert response.status_code == 422


def test_task_stats(client):
    client.post("/api/v1/tasks/", json={"title": "T1", "estimated_time": 30})
    task2 = client.post("/api/v1/tasks/", json={"title": "T2", "estimated_time": 60})
    client.patch(f"/api/v1/tasks/{task2.json()['id']}/complete")

    response = client.get("/api/v1/tasks/stats")
    assert response.status_code == 200
    stats = response.json()
    assert stats["total"] == 2
    assert stats["completed"] == 1
    assert stats["pending"] == 1
    assert stats["total_estimated_time"] == 90
    assert stats["completion_rate"] == 50.0
