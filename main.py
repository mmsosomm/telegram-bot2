import sys
from telethon import TelegramClient, events

# بيانات البوت مباشرة
BOT_TOKEN = "8425517768:AAF5iDn8rMmGqMVjRJf1gWFl-7tU64lGEcU"
API_ID = 12662093
API_HASH = "1BJWap1wBu7rGsfspCrUp4ZCWJicCSG_WdpRxBhI71Wq0rVRdeDBe1mVe_4SCjJBQPEh-RD62XJjPg48ytBmTuo6lV8GYqXQt6tFgcGWMsKvgDqM7xBxAUOQtwKP_P0_t5N7JiejKOQI-Ok6L2O5U_vzUv5ZPegnwK7-tkO4bXjz1d9BtC1Do4Bqf1iB9pYKp5F8KWQsU3SLX32rmiUQremo-vL4bpA-lq5it1zbi7ZDenO57DDKHe4wyPzUacKX5D4ZF4yNHf2kXqd0ZaD5RoB42wLtqlX6UhSUs7qRMIUyRYvEiuzubq_-78JMu8voNTOmizI8obpJwTkbhIkoetLDs4cFmh84="  # ضع الـ api_hash الخاص بك هنا

MY_CHANNEL = '@test99sw'
KEYWORDS = ["TP", "SL", "Gold buy", "Gold sell"]
SOURCE_CHANNELS = ['@ssww334455', '@NeymarGoldTrader', '@xauusdgoldsignalscn']

print("🟢 جاري تشغيل بوت التليجرام الرسمي...")

# استخدام اسم جلسة جديد كلياً ومختص بالبوت لتجنب تداخل البيانات القديمة
client = TelegramClient('official_bot_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def my_event_handler(event):
    message_text = event.raw_text

    if any(word in message_text for word in KEYWORDS):
        try:
            if event.message.forward:
                try:
                    chat = await event.message.forward.get_chat()
                    channel_name = getattr(chat, 'title', 'غير معروف')
                    message_text += f"\n\n📢 المصدر الأصلي: {channel_name}"
                except Exception:
                    pass
            else:
                try:
                    chat = await event.get_chat()
                    channel_name = getattr(chat, 'title', 'غير معروف')
                    message_text += f"\n\n📢 المصدر: {channel_name}"
                except Exception:
                    pass

            await client.send_message(MY_CHANNEL, message_text, silent=False)
            print("🟢 تم إرسال الرسالة بنجاح وبصوت!")
        except Exception as e:
            print(f"❌ حدث خطأ أثناء الإرسال: {e}")

with client:
    # بدء البوت مباشرة باستخدام التوكن دون الحاجة لدوال معقدة
    client.start(bot_token=BOT_TOKEN)
    print("🟢 البوت متصل الآن ويزعم المراقبة بنجاح...")
    client.run_until_disconnected()
