def test_login(client):
    # Make sure user exists
    client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "1234"
    })

    # Attempt login
    response = client.post("/login", json={
        "email": "test@example.com",
        "password": "1234"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
