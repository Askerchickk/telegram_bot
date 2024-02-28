import telebot
from telebot import types
import random

# Токен, который выдает @botfather
bot = telebot.TeleBot('Ваш токен')

bot.delete_webhook()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('Курсы валют')
    item2 = types.KeyboardButton('Погода')
    item3 = types.KeyboardButton('Календарь')
    item4 = types.KeyboardButton('Игра')
    item5 = types.KeyboardButton('Новости')
    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_links(message):
    if (message.text == 'Курсы валют'):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='Курсы валют', url='https://www.banki.ru/products/currency/cb/')
        markup.add(item1)
        bot.send_message(message.chat.id, "Курсы валют", reply_markup=markup)
    elif (message.text == 'Погода'):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='Яндекс.Погода', url='https://yandex.ru/pogoda/')
        markup.add(item1)
        bot.send_message(message.chat.id, "Сайт с погодой", reply_markup=markup)
    elif (message.text == 'Календарь'):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='Календарь', url='https://calendar555.ru/')
        markup.add(item1)
        bot.send_message(message.chat.id, "Календарь", reply_markup=markup)
    elif (message.text == 'Игра'):
        bot.send_message(message.chat.id, 'Угадай число от 1 до 10')

        number = random.randint(1, 10)

        bot.register_next_step_handler(message, check_answer, number)
    elif (message.text == 'Новости'):
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton(text='Dzen', url='https://dzen.ru/?utm_referer=yandex.ru')
        markup.add(item1)
        bot.send_message(message.chat.id, "Новости", reply_markup=markup)


def check_answer(message, number):
    try:
        guess = int(message.text)

        if guess == number:
            bot.send_message(message.chat.id, 'Поздравляю, вы угадали число!')
        elif guess < number:
            bot.send_message(message.chat.id, 'Загаданное число больше')
            bot.register_next_step_handler(message, check_answer, number)
        else:
            bot.send_message(message.chat.id, 'Загаданное число меньше')
            bot.register_next_step_handler(message, check_answer, number)
    except ValueError:
        bot.send_message(message.chat.id, 'Некорректный ввод. Попробуйте снова.')
        bot.register_next_step_handler(message, check_answer, number)

bot.polling()
