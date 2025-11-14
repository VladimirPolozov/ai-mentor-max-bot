import aiohttp
from aiomax import Message
from config import Config


async def handle_user_query(message: Message):
    # Обрабатывает вопрос пользователя через внешний RAG-API.

    question = message.text.strip()

    if not question:
        return

    url = "http://localhost:8000/query"
    headers = {
        "X-API-Key": Config.API_KEY,
        "Content-Type": "application/json"
    }
    data = {"question": question, "top_k": 3}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    answer = result.get("content", "Не удалось получить ответ на ваш вопрос.")
                    await message.reply(answer)
                else:
                    error_text = await resp.text()
                    await message.reply(
                        f"Ошибка сервера: {resp.status} - {error_text[:200]}"
                    )

    except Exception as e:
        await message.reply(
            "Извините, временно не могу ответить. Попробуйте позже."
        )