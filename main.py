from telebot import TeleBot, types

# BotFather থেকে নেওয়া Token
TOKEN = "8199006545:AAHHmZD2Tj2TOTNj7Ig2flD9agm_5rMuqBk"
bot = TeleBot(TOKEN)

# Monotag / Shortener লিঙ্ক
referral_url = "https://otieu.com/4/9431817"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    # রেফারার আইডি চেক
    args = message.text.split()
    if len(args) > 1:
        ref_id = args[1]
        bot.send_message(chat_id, f"👋 Welcome! You were referred by user ID: {ref_id}")
    else:
        bot.send_message(chat_id, "👋 Welcome to Crypto Dogs Token Bot!")

    # মেসেজ পাঠানো হচ্ছে রেফারেল লিংকসহ
    msg = f"""🎯 Click here to earn tokens:
👉 {referral_url}

💰 Share your referral link and earn more!
📲 Your referral link:
https://t.me/CryptoDogsEarningBot?start={chat_id}
"""
    bot.send_message(chat_id, msg)

bot.polling()
