import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load token and channel ID from environment
BOT_TOKEN = ("7705120475:AAEX2-0g5aKjCOez7-GUsqWfRF6p_kI4Wcw")
CHANNEL_ID = os.getenv("-7368291347")  # e.g. @alphalegions or -1001234567890
WEBHOOK_URL = os.getenv("https://bot-7ynr.onrender.com/webhook")  # e.g. https://your-app.onrender.com

# Flask app
app = Flask(__name__)

# Telegram bot app
bot_app = ApplicationBuilder().token(BOT_TOKEN).build()

# Welcome message
WELCOME_MESSAGE = """🛡 *THE ALPHA LEGION HAS AWAKENED* 🛡
Where Wolves Hunt Wealth.

Welcome to the most elite crypto syndicate on Telegram.
We don’t follow trends, we create them.
🐺 Daily alpha
📈 Underground insiders
💰 Wealth-building strategies
🧠 Mindset of a Millionaire

💼 Join the pack. Get rich with precision.

💬 *Meme coins • Signals • Tactics • Brotherhood*

You either ride with the wolves… 🐺  
or get hunted by the pack. ☠️

👉 [START PRINTING MONEY NOW!!!](https://t.me/alphalegions)
"""

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode='Markdown')
    
    # Send message to channel
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text="🚀 A new recruit has joined The Alpha Legion!",
    )

bot_app.add_handler(CommandHandler("start", start))

# Flask webhook route
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    bot_app.update_queue.put_nowait(update)
    return "OK"

# Set webhook and run bot
if __name__ == "__main__":
    bot_app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 8443)),
        webhook_url=WEBHOOK_URL
    )
