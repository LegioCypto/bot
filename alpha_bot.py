from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Your bot token
BOT_TOKEN = '7705120475:AAEX2-0g5aKjCOez7-GUsqWfRF6p_kI4Wcw'

# Welcome message
WELCOME_MESSAGE = """🛡 *THE ALPHA LEGION HAS AWAKENED* 🛡

Welcome to the shadows — where ⚔️ power, 🧠 knowledge, and 🎯 strategy collide.

This is not just a community... it's a *movement*.

If you're ready to lead, not follow — to conquer, not comply —
then join us where the real war is fought:

👉 [Enter the Main Legion Command](https://t.me/alphalegions)

💬 *Meme coins • Signals • Tactics • Brotherhood*

You either ride with the wolves… 🐺  
or get hunted by the pack. ☠️

🔗 The Alpha Legion is waiting. Don’t keep us waiting.
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
