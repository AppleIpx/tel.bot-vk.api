import telebot
from telebot import types
from find_info_users_vk import getData
from telebot.types import Message
import re

bot = telebot.TeleBot()


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


users = {}


@bot.message_handler(commands=['start'])
def start(message: Message):
    users[message.from_user.id] = {'id': False}
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}, более подробную информацию обо мне  можешь узнать по команде /help ')


@bot.message_handler(commands=['help'])
def help(message: Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Что я умею', callback_data='get_info'))
    markup.add(types.InlineKeyboardButton(text='Твой телеграм ID', callback_data='get_my_tgId'))
    markup.add(types.InlineKeyboardButton(text='Узнать информацию по VK ID', callback_data='get_Name'))
    bot.send_message(message.chat.id, 'Вот мои возможности', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'get_info':
        bot.send_message(call.message.chat.id,
                         'Меня зовут Бот - Артем,  я умею добывать информацию о пользователях из вконтакта по их ID, также могу сказать тебе твой персональный ID в телеграм.')
    if call.data == 'get_my_tgId':
        bot.send_message(call.message.chat.id, f'Твой телеграм ID: {call.message.from_user.id}')
    if call.data == 'get_Name':
        msg = bot.send_message(call.message.chat.id, 'Введите id пользователя из вконтакте')
        users[call.message.from_user.id] = {'id': True}
        bot.register_next_step_handler(msg, user_answer)


def user_answer(message):
    if has_cyrillic(message.text) == True:
        bot.send_message(message.chat.id,
                         'Извини, твой введенный адрес содержит русские буквы, попробуй повторить попытку')
    else:
        answer = (message.chat.id, f'{message.text}')
        bot.send_message(message.chat.id, getData(answer[1]))
        users[message.from_user.id] = {'id': False}


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Привет' or message.text == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет')
    elif message.text == 'Как дела?' or message.text == 'как дела?' or message.text == 'Какие дела?' or message.text == 'какие дела?' or message.text == 'как дела' or message.text == 'какие дела' or message.text == 'Как дела' or message.text == 'Какие дела':
        bot.send_message(message.chat.id, 'Все хорошо, твои как?')
    else:
        bot.send_message(message.chat.id,
                         'Извини, я пока не знаю, что тебе ответить(, введи команду /help и познакомься со мной')


bot.polling(none_stop=True)
