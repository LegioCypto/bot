from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your bot token
BOT_TOKEN = '7705120475:AAEX2-0g5aKjCOez7-GUsqWfRF6p_kI4Wcw'

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

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode='Markdown')

# Main bot application
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print("✅ Bot is running...")
    app.run_polling()
