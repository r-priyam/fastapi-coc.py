from __future__ import annotations

import logging

import coc

from app.core import config

log = logging.getLogger('coc')

client = coc.Client(key_names=config.COC_KEY_NAME)


async def setup_coc():
    try:
        await client.login(email=config.COC_EMAIL, password=config.COC_PASSWORD)
    except Exception as exc:
        log.error(f"Failed to setup clash api connection. Exiting! {exc}")
        exit(1)
