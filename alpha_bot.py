import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Webhook
from flask import Flask, request

TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # e.g. https://your-app.onrender.com

app = Flask(__name__)

# Telegram bot setup
bot_app = ApplicationBuilder().token(TOKEN).build()

WELCOME = """🛡 *THE ALPHA LEGION HAS AWAKENED* 🛡
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

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME, parse_mode='Markdown')

bot_app.add_handler(CommandHandler('start', start))

# Flask route for Telegram webhook
@app.route('/', methods=['POST'])
def webhook_handler():
    bot_app.bot.process_update(Update.de_json(request.get_json(), bot_app.bot))
    return 'OK'

# After startup, set webhook
if __name__ == '__main__':
    bot_app.run_webhook(
        listen='0.0.0.0',
        port=int(os.environ.get('PORT', '8443')),
        webhook_url=WEBHOOK_URL
    )
