import asyncio
from fastapi import APIRouter, Depends
from fastapi.responses import PlainTextResponse, HTMLResponse
from shopen.models.schemas import UserCredentials

router = APIRouter()

@router.get("/readme", summary="Get readme", description="Get readme of the software under test")
async def service_readme():
    with open("devchallenge.md", 'r') as file:
        return PlainTextResponse(status_code=200, content=file.read())

@router.get("/about", summary="Get about", description="Get about of the software under test")
async def service_about():
    with open("about.html", 'r') as file:
        return HTMLResponse(status_code=200, content=file.read())
