<div align="center">

## **A simple [FastAPI](https://github.com/tiangolo/fastapi) app to demonstrate the use with [coc.py](https://github.com/mathsman5133/coc.py)**

</div>

## Inroduction

This simple application uses the `coc.py` library to interact with `Clash of Clans` in game API and the `FastAPI` framework to server the data using `jinja2` templates.

## Features

- 📄 Jinja2 templates
- ✒️ Fully type-safe code (checked with [`Pyright`](https://github.com/microsoft/pyright)).
- 🚀 It actually works!

## Important Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [coc.py Documentation](https://cocpy.readthedocs.io/en/latest/)
- [Starlette's docs](https://www.starlette.io/templates/)

## Before you start

Please make sure that you have these requirements ready:

- Python **3.9+**
- Poetry, for dependency management. Follow the [installation instructions](https://python-poetry.org/docs/#installation) to install it.
- GIT, for version control and also to clone this repo. Follow [installation instructions](https://git-scm.com/) to install it.
- Nothing else but however basic knowledge of `Python` and `FastAPI`.

## Getting Started

1. Clone the project using `git clone https://github.com/r-priyam/fastapi-coc.py.git`
2. Run `poetry install` to install the dependencies.
3. Rename `.env.example` to `.env` and fill in the required values.
    - `COC_EMAIL`: Your email from `https://developer.clashofclans.com/`
    - `COC_PASSWORD`: Your password from `https://developer.clashofclans.com/`
    - `COC_KEY_NAME`: Name to create API key with.

All set now, turn the 💡 on by running - `poetry run task dev`. Once application started, visit - `http://127.0.0.1:8000/player/2pp` in your browser and done. Change player tag to whatever you want to and it will display that player information.

If you have any questions or suggestions, please feel free to open an issue [here](https://github.com/r-priyam/fastapi-coc.py/issues/new).
