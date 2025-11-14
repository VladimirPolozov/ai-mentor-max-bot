import aiomax
from bot.handlers.on_start import send_welcome
from bot.handlers.on_message import handle_user_query
from config import Config


def create_bot() -> aiomax.Bot:
    bot = aiomax.Bot(Config.MAX_BOT_TOKEN, default_format="markdown")

    bot.on_bot_start()(send_welcome)

    @bot.on_message()
    async def on_msg(msg):
        await handle_user_query(msg)

    return bot