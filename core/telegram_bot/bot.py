import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from django.conf import settings
from core.telegram_bot.handle import start_handler  # Matches your file name: handle.py

async def main():
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Register /start handler
    application.add_handler(CommandHandler("start", start_handler))

    print("🤖 Bot is running... Press Ctrl+C to stop.")
    await application.run_polling()
