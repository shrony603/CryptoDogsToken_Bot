from telebot import TeleBot, types

TOKEN = "8199006545:AAHHmZD2Tj2TOTNj7Ig2flD9agm_5rMuqBk"
bot = TeleBot(TOKEN)

# Replace this with your referral link
referral_url = "https://otieu.com/4/9431817"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    ref_id = message.text.split(" ")[1] if len(message.text.split()) > 1 else None

    if ref_id:
        bot.send_message(chat_id, f"👋 Welcome! You were referred by user ID: {ref_id}")
    else:
        bot.send_message(chat_id, "👋 Welcome to Crypto Dogs Token Bot!")

    msg = f"""🎯 Click here to earn tokens:
👉 {referral_url}

💰 Share your referral link and earn more!
📲 Your referral link: https://t.me/CryptoDogsEarningBot?start={chat_id}
"""
    bot.send_message(chat_id, msg)

bot.polling()
