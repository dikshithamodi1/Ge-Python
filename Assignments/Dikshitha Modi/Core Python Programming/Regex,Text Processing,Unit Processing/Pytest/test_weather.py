def test_get_temperature(monkeypatch):
    import weather 
    from weather import get_temperature
    class MockResponse:
        #Fake response class
        def json(self):
            return {"temperature":20}
    #Fake requests.get function
    def mock_get(url):
        return MockResponse()
    
    #setting temporary requests
    monkeypatch.setattr(weather.requests,"get",mock_get)
    assert weather.get_temperature("London")==20