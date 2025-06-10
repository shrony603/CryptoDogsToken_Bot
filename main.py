from telebot import TeleBot

# Replace with your BotFather token
TOKEN = "8199006545:AAHHmZD2Tj2TOTNj7Ig2flD9agm_5rMuqBk"
bot = TeleBot(TOKEN)

# Monotag / Shortener referral URL
referral_url = "https://otieu.com/4/9431817"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    # Optional: Referral tracking
    args = message.text.split()
    if len(args) > 1:
        ref_id = args[1]
        bot.send_message(chat_id, f"👋 Welcome! You were referred by user ID: {ref_id}")
    else:
        bot.send_message(chat_id, "👋 Welcome to Crypto Dogs Token Bot!")

    # Send earnings message with referral link
    msg = (
        f"\n🎯 Click here to earn tokens:\n👉 {referral_url}\n\n"
        f"💰 Share your referral link and earn more!\n"
        f"📲 Your referral link:\nhttps://t.me/CryptoDogsEarningBot?start={chat_id}"
    )
    bot.send_message(chat_id, msg)

# Start the bot
bot.polling()
