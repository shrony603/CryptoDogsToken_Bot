import sqlite3
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, MONOTAG_AD_URL

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    balance INTEGER DEFAULT 0,
    referred_by INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS withdraws (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount INTEGER,
    status TEXT
)
""")
conn.commit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    referred_by = int(args[0]) if args else None

    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (user_id, referred_by) VALUES (?, ?)", (user_id, referred_by))
        if referred_by:
            cursor.execute("UPDATE users SET balance = balance + 10 WHERE user_id=?", (referred_by,))
        conn.commit()
        await update.message.reply_text("✅ Account created! Use /earn to start earning Crypto Dogs tokens!")
    else:
        await update.message.reply_text("You’re already registered. Use /earn to keep earning!")

async def earn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        msg = f"""🎯 Click here to earn tokens:
👉 https://otieu.com/4/9431817"""
bot.send_message(chat_id, msg)
{MONOTAG_AD_URL}

" +
        "✅ After viewing the ad, your balance will be updated automatically.",
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cursor.execute("SELECT balance FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    bal = result[0] if result else 0
    await update.message.reply_text(f"💰 Your current balance is: {bal} tokens")

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cursor.execute("SELECT balance FROM users WHERE user_id=?", (user_id,))
    bal = cursor.fetchone()[0]

    if bal < 50:
        await update.message.reply_text("❌ Minimum withdraw is 50 tokens.")
        return

    cursor.execute("INSERT INTO withdraws (user_id, amount, status) VALUES (?, ?, ?)", (user_id, bal, "pending"))
    cursor.execute("UPDATE users SET balance = 0 WHERE user_id=?", (user_id,))
    conn.commit()

    await update.message.reply_text("✅ Withdraw request submitted. You'll receive tokens soon.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("earn", earn))
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("withdraw", withdraw))

print("✅ Bot is running...")
app.run_polling()
