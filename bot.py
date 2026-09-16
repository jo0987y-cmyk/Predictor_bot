import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Hello!\n\n"
        "Mera Telegram bot successfully online hai ✅\n\n"
        "Commands:\n"
        "/start - Start bot\n"
        "/status - Check status\n"
        "/help - Help"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 BOT STATUS: ONLINE\n"
        "📡 Telegram connection working."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Available commands:\n\n"
        "/start\n"
        "/status\n"
        "/help"
    )


def main():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN environment variable missing!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 Bot started successfully...")
    app.run_polling()


if __name__ == "__main__":
    main()
