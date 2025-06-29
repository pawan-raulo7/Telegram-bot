from telegram import Update
from telegram.ext import ContextTypes
from asgiref.sync import sync_to_async
from core.models import TelegramUser

@sync_to_async
def save_telegram_user(telegram_id, username):
    TelegramUser.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={"username": username}
    )

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user:
        telegram_id = user.id
        username = user.username or "NoUsername"

        # Save user using sync-safe function
        await save_telegram_user(telegram_id, username)

    await update.message.reply_text("✅ Hello! Your bot is working!")
