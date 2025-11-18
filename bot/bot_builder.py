import aiomax
from aiomax import BotStartPayload
from bot.handlers.on_message import handle_user_query
from config import Config


def create_bot() -> aiomax.Bot:
    bot = aiomax.Bot(Config.MAX_BOT_TOKEN, default_format="markdown")

    @bot.on_bot_start()
    async def on_bot_start(payload: BotStartPayload):
        await payload.send(
            "👋 Привет! Я — ИИ-наставник для студентов направления «Прикладная информатика в экономике» (КемГУ).\n\n" +
            "Это MVP-версия: пока я отвечаю только на вопросы по вашему направлению," +
            "но функциональность будет постепенно расширяться! Задавай мне любые вопросы!"
        )

    @bot.on_message()
    async def on_msg(msg):
        await handle_user_query(msg)

    return bot