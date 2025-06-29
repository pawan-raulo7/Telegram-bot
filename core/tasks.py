import time
import httpx
from celery import shared_task
from django.conf import settings
from celery import shared_task
from core.telegram_utils import send_telegram_message

@shared_task
def send_delayed_message(chat_id: int):
    time.sleep(5)  # Simulate long processing
    message = "✅ Your background task is complete!"

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    response = httpx.post(url, data=data)
    return response.status_code



@shared_task
def send_telegram_notification(chat_id: int, text: str) -> None:
    send_telegram_message(chat_id, text)
