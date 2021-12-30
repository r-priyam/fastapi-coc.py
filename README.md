<h1 align="center">
Quick example to show how to use <a href="https://github.com/tiangolo/fastapi" target="_blank">FastApi</a> with <a href="https://github.com/mathsman5133/coc.py" target="_blank">coc.py</a>
</h1>

### Getting Started

Follow the below steps to setup for the intial phase.

```bash
# 1. Clone the repo
$ git clone https://github.com/r-priyam/fastapi-coc.py.git

# 2. Change directory
$ cd fastapi-coc.py

# 3. Create virtual enviroment
$ python -m venv .venv

# 4. Activate virtual enviroment
$ .venv/Scripts/Activate

# 5. Install dependencies
$ pip install -r requirements.txt
```

As a next step, rename `.env.example` to `.env` and pass the required variables.

- `COC_EMAIL`: Your email from `https://developer.clashofclans.com/`
- `COC_PASSWORD`: Your password from `https://developer.clashofclans.com/`
- `COC_KEY_NAME`: Name to create API key with.

All set now, turn the 💡 on by running - `uvicorn main:app --reload`

As a next step visit - `http://127.0.0.1:8000/player/2pp` and done. Change player tag to whatever you want to.

To read more about templates use in FastApi please visit [FastApi docs](https://fastapi.tiangolo.com/advanced/templates/) or [Starlette's docs](https://www.starlette.io/templates/) on template.
