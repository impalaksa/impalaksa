import telebot
import openai

TELEGRAM_TOKEN = "1250767040:AAFpFGcWwUdJb9zR1R4C7JI3lSWA2ywfdbE"
OPENAI_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response['choices'][0]['message']['content']
        bot.reply_to(message, reply)
    except Exception as e:
        # ما في رسالة خطأ للمستخدم
        pass

bot.polling()
