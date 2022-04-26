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

log = logging.getLogger()
log.setLevel(logging.INFO)
dt_fmt = "%d-%m-%Y %H:%M:%S"
fmt = logging.Formatter("[{asctime}] [{levelname:<7}] {name}: {message}", dt_fmt, style="{")

app = typer.Typer()


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@app.command()
@coro
async def runserver(host: str = "127.0.0.1", debug: bool = False):
    if debug:
        # import coloredlogs here because I don't install
        # dev dependencies during production
        import coloredlogs

        coloredlogs.install(level="INFO", fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt=dt_fmt)
    else:
        handler = handlers.TimedRotatingFileHandler(filename="app.log", encoding="utf-8", when="M", interval=1)
        handler.setFormatter(fmt)
        log.addHandler(handler)

    server_config = Config("app.main:app", host=host, workers=1)
    server = Server(config=server_config)
    await server.serve()


if __name__ == "__main__":
    app()
