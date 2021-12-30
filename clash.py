from __future__ import annotations

import coc

from config import config


client = coc.Client(key_names=config.COC_KEY_NAME)


async def setup_coc():
    try:
        await client.login(email=config.COC_EMAIL, password=config.COC_PASSWORD)
    except Exception as Exc:
        print(f"Failed to setup clash api connection {Exc}")
        exit(1)