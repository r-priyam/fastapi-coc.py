from __future__ import annotations

import asyncio
import logging
import logging.handlers as handlers
from functools import wraps

import typer
from uvicorn import Config, Server

try:
    import uvloop  # type: ignore
except ModuleNotFoundError:
    loop = asyncio.new_event_loop()
else:
    loop = uvloop.new_event_loop()

app = typer.Typer()


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@app.command()
@coro
async def runserver(host: str = "127.0.0.1", debug: bool = False):
    logging.getLogger("coc").setLevel(logging.ERROR)
    logging.getLogger("coc.events").setLevel(logging.ERROR)
    logging.getLogger("coc.http").setLevel(logging.ERROR)

    global_log = logging.getLogger()
    global_log.setLevel(logging.INFO)
    dt_fmt = "%d-%m-%Y %H:%M:%S"
    fmt = logging.Formatter("[{asctime}] [{levelname:<7}] {name}: {message}", dt_fmt, style="{")
    handler = logging.FileHandler(filename="app.log", encoding="utf-8", mode="w")
    handler.setLevel(logging.INFO)
    handler.setFormatter(fmt)
    global_log.addHandler(handler)

    if debug:
        # import coloredlogs here because I don't install
        # dev dependencies during production
        import coloredlogs

        level_styles = {
            "critical": {"bold": True, "color": "red"},
            "debug": {"color": "green"},
            "error": {"bold": True, "color": "red"},
            "info": {"color": 209},
            "notice": {"color": "magenta"},
            "spam": {"color": "green", "faint": True},
            "success": {"bold": True, "color": "green"},
            "verbose": {"color": "blue"},
            "warning": {"bold": True, "color": "yellow"},
        }
        field_styles = {
            "asctime": {"color": "green", "bright": True},
            "hostname": {"color": "magenta"},
            "levelname": {"bold": True, "color": 39},
            "name": {"color": 44, "bright": True},
            "programname": {"color": "cyan"},
            "username": {"color": "yellow"},
        }
        coloredlogs.install(
            level="INFO",
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            level_styles=level_styles,
            datefmt=dt_fmt,
            field_styles=field_styles,
        )

    server_config = Config("app.main:app", host=host, workers=1)
    server = Server(config=server_config)
    await server.serve()


if __name__ == "__main__":
    app()
