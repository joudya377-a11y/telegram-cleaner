import telebot
import os

# التوكن الخاص بك (تأكدي من وضعه هنا)
TOKEN = '8803208419:AAGzaQkjqs1YbB4hIsFz3Fn9IJUAW1QHZfY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def delete_links(message):
    # نتحقق إذا كان النص يحتوي على روابط
    if message.text and ('http' in message.text or 'www.' in message.text):
        try:
            # مسح الرسالة
            bot.delete_message(message.chat.id, message.message_id)
            
            # إرسال تحذير باسم المستخدم
            user_name = message.from_user.first_name
            warning_text = f"عذراً يا {user_name}، ممنوع إرسال روابط في المجموعة!"
            bot.send_message(message.chat.id, warning_text)
        except Exception as e:
            print(f"Error: {e}")

# لتشغيل البوت
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()


