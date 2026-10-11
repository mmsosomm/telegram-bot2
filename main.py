import os
import asyncio

from telethon import TelegramClient, events
from telethon.sessions import StringSession

# بيانات الحساب الشخصي والبوت
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
STRING_SESSION = os.environ["STRING_SESSION"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

# القناة المستقبلة
MY_CHANNEL = "@test99sw"

# الكلمات المفتاحية
KEYWORDS = ["TP", "SL", "Gold buy", "Gold sell"]

# القنوات المراقبة
SOURCE_CHANNELS = [
    "@ssww334455",
    "@NeymarGoldTrader",
    "@xauusdgoldsignalscn",
]

# العميل الأول: حسابك الشخصي لمراقبة القنوات
user_client = TelegramClient(
    StringSession(STRING_SESSION),
    API_ID,
    API_HASH
)

# العميل الثاني: البوت لإرسال الرسائل
bot_client = TelegramClient(
    "bot_session",
    API_ID,
    API_HASH
)


@user_client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def my_event_handler(event):
    message_text = event.raw_text or ""

    # التحقق من الكلمات المفتاحية دون حساسية لحالة الأحرف
    if not any(word.lower() in message_text.lower() for word in KEYWORDS):
        return

    try:
        # الحصول على اسم القناة المصدرية
        try:
            chat = await event.get_chat()
            channel_name = getattr(chat, "title", None) or "غير معروف"
        except Exception:
            channel_name = "غير معروف"

        # إضافة اسم المصدر إلى الرسالة
        message_text += f"\n\n📢 المصدر: {channel_name}"

        # النشر بواسطة البوت بدل الحساب الشخصي
        await bot_client.send_message(
            MY_CHANNEL,
            message_text,
            silent=False
        )

        print(
            f"🟢 تم نشر الرسالة من {channel_name} "
            "بواسطة البوت بنجاح!"
        )

    except Exception as e:
        print(f"❌ حدث خطأ أثناء معالجة الرسالة: {e}")


async def main():
    try:
        # الاتصال بالحساب الشخصي باستخدام الجلسة المحفوظة
        await user_client.start()
        print("🟢 تم الاتصال بالحساب الشخصي.")

        # تشغيل البوت مباشرة باستخدام التوكن
        await bot_client.start(bot_token=BOT_TOKEN)
        print("🟢 تم الاتصال بالبوت بنجاح.")

        print("👀 بدأت مراقبة القنوات المصدرية.")

        # إبقاء العميلين متصلين
        await asyncio.gather(
            user_client.run_until_disconnected(),
            bot_client.run_until_disconnected()
        )

    except Exception as e:
        print(f"❌ خطأ في تشغيل النظام: {e}")
        raise

    finally:
        await user_client.disconnect()
        await bot_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
