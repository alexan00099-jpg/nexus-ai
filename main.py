import asyncio
import os
from aiogram import Bot, Dispatcher
from aiohttp import web

BOT_TOKEN = "8760530404:AAFLyNrH637xnDo68ZevuffMGcBuzpUJACw"
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
    
    # Запуск опроса Telegram в фоновом режиме
    asyncio.create_task(dp.start_polling(bot))
    
    # Запуск веб-сервера для Render
    port = int(os.environ.get("PORT", 10000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    
    # Удерживаем приложение активным
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
