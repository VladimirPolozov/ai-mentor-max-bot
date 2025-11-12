import aiomax
from config import MAX_BOT_TOKEN
from external.deepseek_client import DeepSeekClient
from core.knowledge_service import KnowledgeService
from bot.handlers.on_start import send_welcome

def create_bot() -> aiomax.Bot:
    bot = aiomax.Bot(MAX_BOT_TOKEN, default_format="markdown")

    bot.on_bot_start()(send_welcome)

    @bot.on_message()
    
    async def on_msg(msg):
        await handle_user_message(msg, knowledge_service)

    return bot

