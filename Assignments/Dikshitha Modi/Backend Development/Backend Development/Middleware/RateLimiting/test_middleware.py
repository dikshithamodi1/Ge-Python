def test_rate_limiting(client):
    for _ in range(5):
        r = client.get("/")
        assert r.status_code == 200

    response = client.get("/")
    assert response.status_code == 429