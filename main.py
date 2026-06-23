import telebot
import os

# قراءة التوكن من إعدادات Render
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

# 1. رد الترحيب البسيط
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت الحماية الخاص بك.\nأنا هنا لحماية المجموعة من الروابط غير المرغوب فيها.")

# 2. مسح الروابط (الوظيفة الأساسية)
@bot.message_handler(func=lambda message: True)
def delete_links(message):
    if message.text and ('http' in message.text or 'www.' in message.text):
        try:
            bot.delete_message(message.chat.id, message.message_id)
            user_name = message.from_user.first_name
            bot.send_message(message.chat.id, f"عذراً يا {user_name}، ممنوع إرسال روابط في هذه المجموعة!")
        except Exception as e:
            print(f"حدث خطأ: {e}")

# تشغيل البوت
if __name__ == "__main__":
    bot.infinity_polling()
