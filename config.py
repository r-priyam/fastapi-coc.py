from __future__ import annotations

from pydantic import BaseSettings


class Config(BaseSettings):
    COC_EMAIL: str
    COC_PASSWORD: str
    COC_KEY_NAME: str

    class Config:
        env_file = ".env"
        case_sensitive = True


config = Config()
