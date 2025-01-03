from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
import os
env_var=os.environ
# Bot tokenini o'zgartiring
TOKEN = env_var['TOKEN']

async def handle_message(update: Update, context: CallbackContext):
    # Yuborilgan xabarni o'zingizga yo'naltirish
    chat_id = env_var['E']  # Sizning Telegram IDingiz
    await context.bot.forward_message(chat_id=chat_id, 
                                      from_chat_id=update.message.chat_id, 
                                      message_id=update.message.message_id)

# Application yaratish
application = Application.builder().token(TOKEN).build()

# Xabarlarni ushlash
message_handler = MessageHandler(filters.ALL, handle_message)
application.add_handler(message_handler)

# Botni ishga tushirish
application.run_polling()
