import os
import logging
import asyncio
import nest_asyncio
from datetime import timedelta

# ✅ Set DJANGO_SETTINGS_MODULE to your actual settings location
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from django.conf import settings

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"🔔 Chat ID is: {update.effective_chat.id}")
    await update.message.reply_text("✅ Hello! Your bot is working!")


async def scheduled_job(context: ContextTypes.DEFAULT_TYPE):
    logger.info("⏰ Scheduled job executed.")


async def main():
    logger.info("🔥 Starting Telegram bot…")

    # ✅ Build app using your bot token from Django settings
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # ✅ Add command handler
    app.add_handler(CommandHandler("start", start_handler))

    # ✅ Schedule a repeating job every 10 seconds
    app.job_queue.run_repeating(scheduled_job, interval=timedelta(seconds=10), first=10)

    logger.info("✅ Bot is polling. Send /start to test.")
    await app.run_polling()


if __name__ == "__main__":
    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    logger.info(f"👤 Chat ID: {chat_id}")
    await update.message.reply_text("✅ Hello! Your bot is working!")
