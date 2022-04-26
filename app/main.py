from __future__ import annotations

import logging

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.clash import client, setup_coc

log = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
async def startup_event():
    await setup_coc()
    log.info("App started and coc connection established successfully")


@app.get("/player/{tag}", response_class=HTMLResponse)
async def player_info(request: Request, tag: str):
    try:
        player = await client.get_player(tag)
    except Exception:
        return  # handle exception how ever you want

    return templates.TemplateResponse("player.html", {"request": request, "player": player})
