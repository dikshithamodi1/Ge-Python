def get_token(client):
    response = client.post("/login", json={
        "email": "test@example.com",
        "password": "1234"
    })
    return response.json()["access_token"]


def test_create_note(client):
    token = get_token(client)

    response = client.post(
        "/notes",
        json={"title": "Test Note", "content": "Hello"},
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200


def test_get_notes(client):
    token = get_token(client)

    response = client.get(
        "/notes",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
