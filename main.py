import telebot
from telebot import types

bot = telebot.TeleBot('5307088386:AAE02cc2FQNs50cK9edBpQs2KV-resrdMoE')

@bot.message_handler(commands=['start'])

def start(message):
    mess = f'Привіт! {message.from_user.first_name}\n' f'Я твій особистий Фармацевт у Кишені\n''Моя головна ціль - допомогти з підбором лікування та покращити твоє самопочуття!\n' '\n' \
    'Не знаєш, де знаходиться найближча доступна аптека?  — Натисни на кнопку «Аптека‼» та без проблем знайдеш те, що шукаєш.\n' \
    '\n''Щось турбує? — Обери свій симптом зі списку та отримай рекомендацію щодо лікування.\n' \
     '\n''Натиснувши на кнопку «SOS» зможеш побачити номери найважливіших служб, які можна забути у складній ситуації.\n'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton('Аптека‼️')
    item_2 = types.KeyboardButton('Щось турбує?😰')
    item_3 = types.KeyboardButton('Ваша аптечка💊')
    item_4 = types.KeyboardButton('🆘')
    markup.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler(content_types=['text'])

def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Ваша аптечка💊':
            mess_2 = '❓ЩО ПОВИННО БУТИ В АПТЕЧЦІ🔊\n' '💊Від болю м’язового та суглобового: ібупрофен, диклофенак\n''💊Жарознижувальний засіб: парацетамол, ібупрофен\n' \
                     '🩸Для обробки рани та зупинки кровотечі: перекис водню/хлоргекседин\n''🩹Антисептичний засіб: розчин йоду\n' '💊Мазь з антибактеріальним ефектом: Левомеколь\n' \
                     '💉Рукавички, бинти, еластичний бинт, джгут, шприц\n''💊Серцеві засоби: Нітрогліцерин, валідол\n''💊Від діареї: лоперамід\n''💊Сорбент: вугілля активоване, ентеросгель, атоксил\n' \
                     'ЗБЕРІГАЙТЕ СПОКІЙ ТА БЕРЕЖІТЬ СЕБЕ!!!\n''🇺🇦СЛАВА УКРАЇНІ🇺🇦\n'
            bot.send_message(message.chat.id, mess_2)

        elif message.text == '🇺🇦':
            mess_3 = '🇺🇦СЛАВА УКРАЇНІ!!!🇺🇦'
            bot.send_message(message.chat.id, mess_3)

        elif message.text == 'Аптека‼️':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Аптека поруч з Вами!', url='https://www.google.com.ua/maps/search/%D0%B0%D0%BF%D1%82%D0%B5%D0%BA%D0%B0/@49.5963348,36.525971,14z?hl=ru&authuser=0'))
            bot.send_message(message.chat.id, 'Google Maps',  reply_markup=markup)

        elif message.text == '⬅Повернутись у меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Аптека‼️')
            item_2 = types.KeyboardButton('Щось турбує?😰')
            item_3 = types.KeyboardButton('Ваша аптечка💊')
            item_4 = types.KeyboardButton('🆘')
            markup.add(item_1, item_2, item_3, item_4)
            bot.send_message(message.chat.id, 'Меню', reply_markup=markup)

        elif message.text == '🆘':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Швидка допомога🚑')
            item_2 = types.KeyboardButton('Поліція🚓')
            item_3 = types.KeyboardButton('Пожежники🚒')
            item_4 = types.KeyboardButton('⬅Повернутись у меню')
            markup.add(item_1, item_2, item_3, item_4)
            bot.send_message(message.chat.id, '🆘', reply_markup=markup)

        elif message.text == 'Швидка допомога🚑':
            mess_4 = '☎ 103'
            bot.send_message(message.chat.id, mess_4)

        elif message.text == 'Поліція🚓':
            mess_5 = '☎ 102'
            bot.send_message(message.chat.id, mess_5)

        elif message.text == 'Пожежники🚒':
            mess_6 = '☎ 101'
            bot.send_message(message.chat.id, mess_6)

        elif message.text == 'Щось турбує?😰':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Головний біль')
            item_2 = types.KeyboardButton('Підвищений тиск')
            item_3 = types.KeyboardButton('Знижений тиск')
            item_4 = types.KeyboardButton('Зубний біль')
            item_5 = types.KeyboardButton('⬅Повернутись у меню')
            item_6 = types.KeyboardButton('Далі➡️')
            markup.add(item_1, item_2, item_3, item_4, item_5, item_6)
            bot.send_message(message.chat.id, 'Виберіть, що Вас турбує', reply_markup=markup)

        elif message.text == 'Далі➡️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Біль у горлі')
            item_2 = types.KeyboardButton('Застуда')
            item_3 = types.KeyboardButton('⬅Повернутись на першу сторінку')
            markup.add(item_1, item_2, item_3)
            bot.send_message(message.chat.id, 'Друга стрінка', reply_markup=markup)

        elif message.text == '⬅Повернутись на першу сторінку':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Головний біль')
            item_2 = types.KeyboardButton('Підвищений тиск')
            item_3 = types.KeyboardButton('Знижений тиск')
            item_4 = types.KeyboardButton('Зубний біль')
            item_5 = types.KeyboardButton('⬅Повернутись у меню')
            item_6 = types.KeyboardButton('Далі➡️')
            markup.add(item_1, item_2, item_3, item_4, item_5, item_6)
            bot.send_message(message.chat.id, 'Перша сторінка', reply_markup=markup)

bot.polling(none_stop=True)