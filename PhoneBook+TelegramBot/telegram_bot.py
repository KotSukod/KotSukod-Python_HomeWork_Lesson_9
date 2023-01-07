from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ApplicationBuilder, MessageHandler,filters
import bot_command

index = 0

async def start_bot(update, context):
    keyboard = [
        [InlineKeyboardButton("Вывести список номеров", callback_data='1')],
        [InlineKeyboardButton("Записать номер", callback_data='2')],
        [InlineKeyboardButton("Найти номер", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id,text = 'Телефонный справочник V 1.2\n'
                                                                           'Выбирите действие:', reply_markup=reply_markup)

async  def button(update: Update, context):
    query = update.callback_query
    variant = query.data
    if variant == '1':
       await bot_command.base_view(update,context)
    elif variant == '2':
        await context.bot.send_message(chat_id=update.effective_chat.id, text=('Введите: Имя Фамилия Номер'))
        echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND),bot_command.great_number)
        app.add_handler(echo_handler)
    elif variant == '3':
        await context.bot.send_message(chat_id=update.effective_chat.id, text=('Введите номер для поиска:'))
        echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), bot_command.search_number)
        app.add_handler(echo_handler)


async def help_command(update, _):
    await update.message.reply_text("Используйте `/start` для тестирования.")


#if __name__ == '__main__':
app = ApplicationBuilder().token("5956367175:AAG51_Cw-PcFUxlgditAUfhyOH9M9jhVnyE").build()

app.add_handler(CommandHandler('start', start_bot))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(CommandHandler('help', help_command))

app.run_polling()