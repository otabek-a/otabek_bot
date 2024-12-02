from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Bot tokenini o'zgartiring
TOKEN = '7386230325:AAFxpvPEXJCM_rIVaKFY45tW5ndhU7RPZw8'

async def handle_message(update: Update, context: CallbackContext):
    # Yuborilgan xabarni o'zingizga yo'naltirish
    chat_id = 6723268646  # Sizning Telegram IDingiz
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
