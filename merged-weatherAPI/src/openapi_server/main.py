# coding: utf-8

"""
    Weather API

    A simple API for retrieving weather information.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from openapi_server.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="Weather API",
    description="A simple API for retrieving weather information.",
    version="1.0.0",
)

app.include_router(DefaultApiRouter)
