# точка входа, запуск бота


import aiomax
import logging


bot = aiomax.Bot("TOKEN", default_format="markdown")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()