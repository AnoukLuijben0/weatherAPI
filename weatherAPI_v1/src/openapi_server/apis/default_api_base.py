# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.forecast_get200_response import ForecastGet200Response
from openapi_server.models.weather_get200_response import WeatherGet200Response


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def forecast_get(
        self,
        city: str,
    ) -> ForecastGet200Response:
        """Retrieve the 5-day weather forecast data for a specific city."""
        ...


    async def weather_get(
        self,
        city: str,
    ) -> WeatherGet200Response:
        """Retrieve the current weather data for a specific city."""
        ...
