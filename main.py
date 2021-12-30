from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from clash import setup_coc, client


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    await setup_coc()
    print("App started and coc connection established successfully")


@app.get("/player/{tag}", response_class=HTMLResponse)
async def read_item(request: Request, tag: str):
    try:
        player = await client.get_player(tag)
    except:
        return  # handle exception how ever you want

    return templates.TemplateResponse("player.html", {"request": request, "player": player})
