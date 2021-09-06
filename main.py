import asyncio
import os
import sys

import dotenv
import pyromod.listen
from pyrogram import Client, idle

from gamebot.config import shared, Settings
from gamebot.utils import ADMINS


if os.path.isfile("env.list"):
    dotenv.load_dotenv("env.list")


async def main():
    print("Starting bot..." or pyromod)
    print("Setup database...", end="")
    shared.settings = Settings()
    bot = Client(
        session_name="gamebot",
        api_id=shared.settings.API_ID,
        api_hash=shared.settings.API_HASH,
        bot_token=shared.settings.BOT_TOKEN,
        plugins=dict(root="gamebot.plugins"),
        sleep_threshold=60 * 60 * 24,
        parse_mode="html",
    )
    print("\rBot has been started!")

    await bot.start()

    if shared.settings.ADMIN:
        ADMINS.add(shared.settings.ADMIN)
    return await idle()


sys.exit(asyncio.run(main()))
