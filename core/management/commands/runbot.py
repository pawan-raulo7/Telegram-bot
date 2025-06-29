from django.core.management.base import BaseCommand
from core.telegram_bot.bot import main as run_telegram_bot
import asyncio
import nest_asyncio

class Command(BaseCommand):
    help = "Starts the Telegram bot"

    def handle(self, *args, **options):
        print("Starting Telegram bot...")

        # Patch the running loop so it can be reused
        nest_asyncio.apply()

        try:
            asyncio.run(run_telegram_bot())
        except KeyboardInterrupt:
            print("\nBot stopped by user.")
