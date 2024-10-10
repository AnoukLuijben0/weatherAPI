# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from services.weather_servicesv0 import get_weather_for_city
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
from openapi_server.models.weather_get200_response import WeatherGet200Response


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


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
    # Added 
    return get_weather_for_city(city)
    """Retrieve the current weather data for a specific city."""
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().weather_get(city)
