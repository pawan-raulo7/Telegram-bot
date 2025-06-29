from django.core.management.base import BaseCommand
from core.telegram_utils import send_telegram_message

class Command(BaseCommand):
    help = "Send a test Telegram message"

    def handle(self, *args, **kwargs):
        chat_id = 6231531837  # Your chat ID
        message = "🚀 This is a test message from your Django project."
        send_telegram_message(chat_id=chat_id, text=message)
        self.stdout.write(self.style.SUCCESS("✅ Message sent successfully!"))
