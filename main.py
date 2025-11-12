# точка входа, запуск бота

import os
import aiomax
import logging
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("MAX_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Переменная окружения MAX_BOT_TOKEN не задана (проверьте файл .env)")

bot = aiomax.Bot(TOKEN, default_format="markdown")


@bot.on_bot_start()
async def info(pd: aiomax.BotStartPayload):
    await pd.send("👋 Привет! Я — ИИ-наставник для студентов направления «Прикладная информатика в экономике» (КемГУ).\n\nЭто MVP-версия: пока я просто отвечаю только на вопросы, связанные с вашим направлением, но функциональность будет постепенно расширяться! Задавай мне любые вопросы!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()