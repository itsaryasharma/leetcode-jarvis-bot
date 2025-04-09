import asyncio
from datetime import datetime, time, timedelta
from telegram import Bot
import pytz
import schedule

# Your credentials
BOT_TOKEN = '7742371511:AAF2sADGo5VO9OX92TWfZYx9JzjuMHGNXNc'
USER_ID = 845682054  # Your Telegram user ID
TIMEZONE = pytz.timezone('Asia/Kolkata')  # IST

# Create bot instance
bot = Bot(token=BOT_TOKEN)

# Define the reminder message
async def send_reminder():
    now = datetime.now(TIMEZONE).strftime('%d-%b %I:%M %p')
    message = f"🧠 Hey boss, it’s {now} IST.\nDon't forget to submit on LeetCode and keep the streak alive! 🔥"
    await bot.send_message(chat_id=USER_ID, text=message)

# Wrapper for schedule to work with async
def job():
    asyncio.run(send_reminder())

# Schedule the job
schedule.every().day.at("20:45").do(job)  # 8:45 PM IST

print("✅ Jarvis is now running and monitoring your LeetCode streak, boss...")

# Keep the script running
while True:
    schedule.run_pending()
    asyncio.sleep(1)
