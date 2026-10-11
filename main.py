import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

# بيانات البوت مباشرة
BOT_TOKEN = "8425517768:AAF5iDn8rMmGqMVjRJf1gWFl-7tU64lGEcU"

MY_CHANNEL = '@test99sw'
KEYWORDS = ["TP", "SL", "Gold buy", "Gold sell"]
SOURCE_CHANNELS = [-1001234567890, -1009876543210] # يمكنك وضع آيدي القنوات أو معرفاتها إذا كانت عامة
# أو استخدام المعرفات النصية العامة هكذا:
SOURCE_CHANNEL_USERNAMES = ['ssww334455', 'NeymarGoldTrader', 'xauusdgoldsignalscn']

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.chat.username.in_(SOURCE_CHANNEL_USERNAMES))
async def handle_forwarded_messages(message: Message):
    message_text = message.text or message.caption or ""
    
    if any(word in message_text for word in KEYWORDS):
        try:
            # إضافة اسم القناة المصدر
            chat_title = message.chat.title or "غير معروف"
            message_text += f"\n\n📢 المصدر: {chat_title}"
            
            # إرسال الرسالة إلى قناتك المستقبلة مع ضمان ظهور الصوت
            await bot.send_message(
                chat_id=MY_CHANNEL,
                text=message_text,
                disable_notification=False  # لضمان ظهور الصوت
            )
            print("🟢 تم إرسال الرسالة بنجاح بواسطة البوت الرسمي وبصوت!")
        except Exception as e:
            print(f"❌ حدث خطأ أثناء الإرسال: {e}")

async def main():
    print("🟢 جاري تشغيل البوت الرسمي عبر aiogram بدون أي طلبات إدخال...")
    # بدء استقبال الرسائل
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
