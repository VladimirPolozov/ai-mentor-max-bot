# точка входа, запуск бота

import asyncio
import logging
from bot.bot_builder import create_bot

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot = create_bot()
    asyncio.run(bot.run())