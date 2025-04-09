import os
import asyncio
from datetime import datetime
from telegram import Bot
import pytz
import schedule
import time

# === Environment Variables ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = int(os.getenv("TELEGRAM_USER_ID"))

# === Timezone (IST) ===
TIMEZONE = pytz.timezone('Asia/Kolkata')

# === Telegram Bot Instance ===
bot = Bot(token=BOT_TOKEN)

# === Reminder Message Logic ===
async def send_reminder():
    now = datetime.now(TIMEZONE).strftime('%d-%b %I:%M %p')
    message = f"🧠 Hey boss, it’s {now} IST.\nDon't forget to submit on LeetCode and keep the streak alive! 🔥"
    await bot.send_message(chat_id=USER_ID, text=message)

# === Synchronous Job Wrapper ===
def job():
    try:
        asyncio.run(send_reminder())
    except Exception as e:
        print(f"Error sending reminder: {e}")

# === Daily Schedule at 8:45 PM IST ===
schedule.every().day.at("20:45").do(job)

print("✅ Jarvis is now running and monitoring your LeetCode streak, boss...")

# === Main Loop ===
while True:
    schedule.run_pending()
    time.sleep(1)
