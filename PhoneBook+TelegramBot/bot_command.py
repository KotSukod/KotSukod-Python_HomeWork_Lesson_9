from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import main
import phone_base


async def base_view(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    base = phone_base.base_open()
    for element in base:
        data = phone_base.elem(element)
        await context.bot.send_message(chat_id=update.effective_chat.id,text=(f'Имя: {data[0]}\n'
                                                                              f'Фамилия: {data[1]}\n'
                                                                              f'Телефон: {data[2]}'))

async def great_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split(' ')
    proverka = phone_base.search_for_duplicates(items[2])
    if proverka == 1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=(f'Такой номер уже существует'))
    else:
        phone_base.great(items[0],items[1],items[2])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=(f'Запись сделана\n'
                                                                           f'Имя: {items[0]}\n'
                                                                           f'Фамилия: {items[1]}\n'
                                                                           f'Телефон: {items[2]}'))

async def search_number(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    number,index = phone_base.search_number(items[0])
    if number == None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=(f'Номер не найден'))
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=(f'Имя: {number[0]}\n'
                                                                               f'Фамилия: {number[1]}\n'
                                                                               f'Телефон: {number[2]}\n'))













