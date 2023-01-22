import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from gpt import gpt_request


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    print(update.message.text)


async def gpt_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_text = update.message.text
    print(f'question: {input_text}')
    output_text = gpt_request(input_text)
    print(f'answer: {output_text}')
    print(update.message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=output_text)


if __name__ == '__main__':
    load_dotenv()
    gpt_api_key = os.environ['GPT_API_key']
    application = ApplicationBuilder().token(os.environ['TELEGRAM_token']).build()
    start_handler = CommandHandler('start', start)
    gpt_message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), gpt_message)

    application.add_handler(start_handler)
    application.add_handler(gpt_message_handler)
    application.run_polling()


