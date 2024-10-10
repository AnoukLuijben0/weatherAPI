# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.forecast_get200_response import ForecastGet200Response
from openapi_server.models.weather_get200_response import WeatherGet200Response


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/forecast",
    responses={
        200: {"model": ForecastGet200Response, "description": "A JSON object containing the 5-day weather forecast."},
        400: {"description": "Invalid city name provided."},
        500: {"description": "Internal server error."},
    },
    tags=["default"],
    summary="Get 5-day weather forecast",
    response_model_by_alias=True,
)
async def forecast_get(
    city: str = Query(None, description="Name of the city to retrieve the forecast for.", alias="city"),
) -> ForecastGet200Response:
    """Retrieve the 5-day weather forecast data for a specific city."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().forecast_get(city)


@router.get(
    "/weather",
    responses={
        200: {"model": WeatherGet200Response, "description": "A JSON object containing the current weather."},
        400: {"description": "Invalid city name provided."},
        500: {"description": "Internal server error."},
    },
    tags=["default"],
    summary="Get current weather",
    response_model_by_alias=True,
)
async def weather_get(
    city: str = Query(None, description="Name of the city to retrieve weather for.", alias="city"),
) -> WeatherGet200Response:
    """Retrieve the current weather data for a specific city."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().weather_get(city)
