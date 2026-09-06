import asyncio
import os
from aiogram import Bot, Dispatcher
from aiohttp import web

BOT_TOKEN = "7718097003:AAEj39pAnq_X9X-s-21f4sXJ0z_54Y-w18k"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def start_handler(message):
    if message.text == "/start":
        await message.answer("Привет! Бот успешно работает на Render!")

async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
