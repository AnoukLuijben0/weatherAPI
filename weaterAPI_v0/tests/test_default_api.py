# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.weather_get200_response import WeatherGet200Response  # noqa: F401


def test_weather_get(client: TestClient):
    """Test case for weather_get

    Get current weather
    """
    params = [("city", 'city_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/weather",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

