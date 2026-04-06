import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я бот.")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Доступные команды: /start, /help, /info")

async def info(update: Update, context: CallbackContext):
    await update.message.reply_text("Я был создан AI-генератором.")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text("Не понимаю :(")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()