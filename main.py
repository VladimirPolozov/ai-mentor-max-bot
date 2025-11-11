# точка входа, запуск бота


import aiomax
import logging
from dotenv import load_dotenv


load_dotenv()


bot = aiomax.Bot("MAX_BOT_TOKEN", default_format="markdown")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()