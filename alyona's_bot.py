import telebot
from telebot import types
bot = telebot.TeleBot('5222741566:AAHVCvWepQD9zAiJencM-mltmoWlox1pKe0')


@bot.message_handler(content_types=['text'])
def main_question(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Сейчас мы предлагаем \n"
                                               "окунуться тебе в мир японского, \n"
                                               "китайского и корейского языков!")
        keyboard = types.InlineKeyboardMarkup()
        key_place1 = types.InlineKeyboardButton(text='Да!', callback_data='yes')
        keyboard.add(key_place1)
        key_place2 = types.InlineKeyboardButton(text='Конечно да!', callback_data='yes')
        keyboard.add(key_place2)
        bot.send_message(message.from_user.id, text='Ты готов?', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет! Чтобы запустить бота, напиши /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def second_question(call):
    chat_id = call.message.chat.id
    japan_img = open("static/img/japan/japan3.jpg", 'rb')
    bot.send_photo(chat_id, japan_img)
    korea_img = open("static/img/korea/korea3.jpg", 'rb')
    bot.send_photo(chat_id, korea_img)
    china_img = open("static/img/china/china1.jpg", 'rb')
    bot.send_photo(chat_id, china_img)
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Япония', callback_data='japan')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Корея', callback_data='korea')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Китай', callback_data='china')
    keyboard.add(key3)
    bot.send_message(call.message.chat.id, text='Выбери страну, язык которой хочешь изучить!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'japan')
def japanese(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Приветствие', callback_data='j_hi')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Краткие ответы', callback_data='j_answers')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Еда', callback_data='j_food')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Цвета', callback_data='j_colors')
    keyboard.add(key4)
    key5 = types.InlineKeyboardButton(text='Одежда', callback_data='j_garb')
    keyboard.add(key5)
    key6 = types.InlineKeyboardButton(text='Времена года', callback_data='j_seasons')
    keyboard.add(key6)
    key7 = types.InlineKeyboardButton(text='Места', callback_data='j_spots')
    keyboard.add(key7)
    bot.send_message(call.message.chat.id, text='Выберите словарь', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'korea')
def korean(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Приветствие', callback_data='k_hi')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Краткие ответы', callback_data='k_answers')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Еда', callback_data='k_food')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Цвета', callback_data='k_colors')
    keyboard.add(key4)
    key5 = types.InlineKeyboardButton(text='Одежда', callback_data='k_garb')
    keyboard.add(key5)
    key6 = types.InlineKeyboardButton(text='Времена года', callback_data='k_seasons')
    keyboard.add(key6)
    key7 = types.InlineKeyboardButton(text='Места', callback_data='k_spots')
    keyboard.add(key7)
    bot.send_message(call.message.chat.id, text='Выберите словарь', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'j_hi')
def japanese_hi(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Доброе утро', callback_data='j_hi_1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Здравствуйте', callback_data='j_hi_2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Добрый вечер', callback_data='j_hi_3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Давно не виделись', callback_data='j_hi_4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери фразу!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'j_answers')
def japanese_answers(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Да', callback_data='j_a1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Нет', callback_data='j_a2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Спасибо', callback_data='j_a3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Не за что', callback_data='j_a4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери фразу!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'j_food')
def japanese_food(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Вареный рис', callback_data='j_f1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Яйцо', callback_data='j_f2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Тофу', callback_data='j_f3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Креветка', callback_data='j_f4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Что будете заказывать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'j_colors')
def japanese_colors(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Черный', callback_data='j_col1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Белый', callback_data='j_col2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Красный', callback_data='j_col3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Синий', callback_data='j_col4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'j_garb')
def japanese_garb(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Платье', callback_data='j_g1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Носки', callback_data='j_g2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Обувь', callback_data='j_g3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Пальто', callback_data='j_g4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'j_seasons')
def japanese_seasons(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Весна', callback_data='j_s1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Осень', callback_data='j_s2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Лето', callback_data='j_s3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Зима', callback_data='j_s4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'j_spots')
def japanese_spots(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Университет', callback_data='j_sp1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Банк', callback_data='j_sp2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Школа', callback_data='j_sp3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Больница', callback_data='j_sp4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Куда направляешься?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_hi')
def korean_hi(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Здравствуйте', callback_data='k_hi_1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Доброе утро', callback_data='k_hi_2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='До свидания (тому, кто уходит)', callback_data='k_hi_3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='До свидания (тому, кто остается)', callback_data='k_hi_4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери фразу!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_answers')
def korean_answers(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Да', callback_data='k_a1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Нет', callback_data='k_a2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Спасибо', callback_data='k_a3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Не за что', callback_data='k_a4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери фразу!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_food')
def korean_food(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Рис', callback_data='k_f1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Овощи', callback_data='k_f2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Картошка', callback_data='k_f3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Морковь', callback_data='k_f4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Что будете заказывать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_colors')
def korean_colors(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Голубой', callback_data='k_col1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Красный', callback_data='k_col2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Черный', callback_data='k_col3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Зеленый', callback_data='k_col4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_garb')
def korean_garb(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Платье', callback_data='k_g1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Футболка', callback_data='k_g2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Штаны', callback_data='k_g3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Пальто', callback_data='k_g4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_seasons')
def korean_seasons(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Весна', callback_data='k_s1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Осень', callback_data='k_s2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Лето', callback_data='k_s3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Зима', callback_data='k_s4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_spots')
def korean_spots(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Столица', callback_data='k_sp1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Круглосуточный магазин', callback_data='k_sp2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Салон красоты', callback_data='k_sp3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Аптека', callback_data='k_sp4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Куда направляешься?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'china')
def chinese(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Приветствие', callback_data='c_hi')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Краткие ответы', callback_data='c_answers')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Еда', callback_data='c_food')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Цвета', callback_data='c_colors')
    keyboard.add(key4)
    key5 = types.InlineKeyboardButton(text='Одежда', callback_data='c_garb')
    keyboard.add(key5)
    key6 = types.InlineKeyboardButton(text='Времена года', callback_data='c_seasons')
    keyboard.add(key6)
    key7 = types.InlineKeyboardButton(text='Места', callback_data='c_spots')
    keyboard.add(key7)
    bot.send_message(call.message.chat.id, text='Выберите словарь', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'c_hi')
def china_hi(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Привет', callback_data='c_hi_1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Доброе утро', callback_data='c_hi_2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Добрый вечер', callback_data='c_hi_3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='До свидания', callback_data='c_hi_4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери фразу!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'c_answers')
def china_answers(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Да', callback_data='c_a1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Нет', callback_data='c_a2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Спасибо', callback_data='c_a3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Не за что', callback_data='c_a4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери фразу!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'c_food')
def china_food(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Bареный рис', callback_data='c_f1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Лапша', callback_data='c_f2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Тофу', callback_data='c_f3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Рыба', callback_data='c_f4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Что будете заказывать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'c_colors')
def china_colors(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Черный', callback_data='c_col1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Синий', callback_data='c_col2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Зеленый', callback_data='c_col3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Красный', callback_data='c_col4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'c_garb')
def china_garb(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Юбка', callback_data='c_g1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Рубашка', callback_data='c_g2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Костюм', callback_data='c_g3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Джинсы', callback_data='c_g4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'c_seasons')
def china_seasons(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Весна', callback_data='c_s1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Осень', callback_data='c_s2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Лето', callback_data='c_s3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Зима', callback_data='c_s4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Выбери слово!', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'c_spots')
def china_spots(call):
    keyboard = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Библиотека', callback_data='c_sp1')
    keyboard.add(key1)
    key2 = types.InlineKeyboardButton(text='Бар', callback_data='c_sp2')
    keyboard.add(key2)
    key3 = types.InlineKeyboardButton(text='Торговый центр', callback_data='c_sp3')
    keyboard.add(key3)
    key4 = types.InlineKeyboardButton(text='Парк', callback_data='c_sp4')
    keyboard.add(key4)
    bot.send_message(call.message.chat.id, text='Куда направляешься?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'k_hi_1')
@bot.callback_query_handler(func=lambda call: call.data == 'k_hi_2')
@bot.callback_query_handler(func=lambda call: call.data == 'k_hi_3')
@bot.callback_query_handler(func=lambda call: call.data == 'k_hi_4')
def korean_words_1(call):
    if call.data == 'k_hi_1':
        msg = '안녕하세요 (annyeonghaseyo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_hi_2':
        msg = '좋은 아침이에요 (joeun achimieyo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_hi_3':
        msg = '안녕히 가세요 (annyeonghi gaseyo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_hi_4':
        msg = '안녕히 계세요 (annyeonghi gyeseyo)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'k_a1')
@bot.callback_query_handler(func=lambda call: call.data == 'k_a2')
@bot.callback_query_handler(func=lambda call: call.data == 'k_a3')
@bot.callback_query_handler(func=lambda call: call.data == 'k_a4')
def korean_words_2(call):
    if call.data == 'k_a1':
        msg = '네 (ne)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_a2':
        msg = '아니요 (aniyo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_a3':
        msg = '감사합니다 (gamsahamnida)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_a4':
        msg = '천만에요 (cheonmaneyo)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'k_f1')
@bot.callback_query_handler(func=lambda call: call.data == 'k_f2')
@bot.callback_query_handler(func=lambda call: call.data == 'k_f3')
@bot.callback_query_handler(func=lambda call: call.data == 'k_f4')
def korean_words_3(call):
    if call.data == 'k_f1':
        msg = '밥 (bab)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_f2':
        msg = '야채 (yachae)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_f3':
        msg = '감자 (gamja)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_f4':
        msg = '당근 (danggeun)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'k_col1')
@bot.callback_query_handler(func=lambda call: call.data == 'k_col2')
@bot.callback_query_handler(func=lambda call: call.data == 'k_col3')
@bot.callback_query_handler(func=lambda call: call.data == 'k_col4')
def korean_words_4(call):
    if call.data == 'k_col1':
        msg = '파란색 (paransaek)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_col2':
        msg = '빨간색 (bbalgansaek)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_col3':
        msg = '검정색 (geomjeongsaek)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_col4':
        msg = '초록색 (choroksaek)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'k_g1')
@bot.callback_query_handler(func=lambda call: call.data == 'k_g2')
@bot.callback_query_handler(func=lambda call: call.data == 'k_g3')
@bot.callback_query_handler(func=lambda call: call.data == 'k_g4')
def korean_words_5(call):
    if call.data == 'k_g1':
        msg = '드레스 (deureseu)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_g2':
        msg = '티셔츠 (teeshyeocheu)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_g3':
        msg = '바지 (baji)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_g4':
        msg = '코트 (koteu)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'k_s1')
@bot.callback_query_handler(func=lambda call: call.data == 'k_s2')
@bot.callback_query_handler(func=lambda call: call.data == 'k_s3')
@bot.callback_query_handler(func=lambda call: call.data == 'k_s4')
def korean_words_6(call):
    if call.data == 'k_s1':
        msg = '봄 (bom)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_s2':
        msg = '가을 (gaeul)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_s3':
        msg = '여름 (yeoreum)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_s4':
        msg = '겨울 (gyeoul)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'k_sp1')
@bot.callback_query_handler(func=lambda call: call.data == 'k_sp2')
@bot.callback_query_handler(func=lambda call: call.data == 'k_sp3')
@bot.callback_query_handler(func=lambda call: call.data == 'k_sp4')
def korean_words_7(call):
    if call.data == 'k_sp1':
        msg = '수도 (sudo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_sp2':
        msg = '편의점 (pyeonuijeom)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_sp3':
        msg = '미장원 (mijangwon)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'k_sp4':
        msg = '약국 (yakguk)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'j_hi_1')
@bot.callback_query_handler(func=lambda call: call.data == 'j_hi_2')
@bot.callback_query_handler(func=lambda call: call.data == 'j_hi_3')
@bot.callback_query_handler(func=lambda call: call.data == 'j_hi_4')
def japanese_words_1(call):
    if call.data == 'j_hi_1':
        msg = 'おはようございます (ohayo: gozaimas)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_hi_2':
        msg = 'こんにちは (konnichiwa)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_hi_3':
        msg = 'こんばんは (konbanwa)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_hi_4':
        msg = 'お久しぶりですね (ohisashiburi desne)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'j_a1')
@bot.callback_query_handler(func=lambda call: call.data == 'j_a2')
@bot.callback_query_handler(func=lambda call: call.data == 'j_a3')
@bot.callback_query_handler(func=lambda call: call.data == 'j_a4')
def japanese_words_2(call):
    if call.data == 'j_a1':
        msg = 'はい (hai)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_a2':
        msg = 'いいえ (iie)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_a3':
        msg = 'ありがとうございます (arigato: gozaimas)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_a4':
        msg = 'どういたしまして (do: itashimashite)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'j_f1')
@bot.callback_query_handler(func=lambda call: call.data == 'j_f2')
@bot.callback_query_handler(func=lambda call: call.data == 'j_f3')
@bot.callback_query_handler(func=lambda call: call.data == 'j_f4')
def japanese_words_3(call):
    if call.data == 'j_f1':
        msg = 'ごはん (gohan)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_f2':
        msg = 'たまご (tamago)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_f3':
        msg = 'とうふ (to:fu)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_f4':
        msg = 'えび (ebi)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'j_col1')
@bot.callback_query_handler(func=lambda call: call.data == 'j_col2')
@bot.callback_query_handler(func=lambda call: call.data == 'j_col3')
@bot.callback_query_handler(func=lambda call: call.data == 'j_col4')
def japanese_words_4(call):
    if call.data == 'j_col1':
        msg = 'くろい (kuroi)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_col2':
        msg = 'しろい (shiroi)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_col3':
        msg = 'あかい (akai)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_col4':
        msg = 'あおい (aoi)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'j_g1')
@bot.callback_query_handler(func=lambda call: call.data == 'j_g2')
@bot.callback_query_handler(func=lambda call: call.data == 'j_g3')
@bot.callback_query_handler(func=lambda call: call.data == 'j_g4')
def japan_words_5(call):
    if call.data == 'j_g1':
        msg = 'ドレス (doresu)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_g2':
        msg = 'くつした (kutsushita)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_g3':
        msg = 'くつ (kutsu)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_g4':
        msg = 'コート (ko:to)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'j_s1')
@bot.callback_query_handler(func=lambda call: call.data == 'j_s2')
@bot.callback_query_handler(func=lambda call: call.data == 'j_s3')
@bot.callback_query_handler(func=lambda call: call.data == 'j_s4')
def japanese_words_6(call):
    if call.data == 'j_s1':
        msg = 'はる (haru)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_s2':
        msg = 'あき (aki)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_s3':
        msg = 'なつ (natsu)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_s4':
        msg = 'ふゆ (fuyu)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'j_sp1')
@bot.callback_query_handler(func=lambda call: call.data == 'j_sp2')
@bot.callback_query_handler(func=lambda call: call.data == 'j_sp3')
@bot.callback_query_handler(func=lambda call: call.data == 'j_sp4')
def china_words_7(call):
    if call.data == 'j_sp1':
        msg = 'だいがく(daigaku)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_sp2':
        msg = 'ぎんこう (ginko:)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_sp3':
        msg = 'がっこう (gakko:)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'j_sp4':
        msg = 'びょういん (byo:in)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'c_hi_1')
@bot.callback_query_handler(func=lambda call: call.data == 'c_hi_2')
@bot.callback_query_handler(func=lambda call: call.data == 'c_hi_3')
@bot.callback_query_handler(func=lambda call: call.data == 'c_hi_4')
def china_words_1(call):
    if call.data == 'c_hi_1':
        msg = '你好 (nǐhǎo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_hi_2':
        msg = '早上好 (zǎoshànghǎo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_hi_3':
        msg = '晚上好 (wǎnshànghǎo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_hi_4':
        msg = '再见 (zàijiàn)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'c_a1')
@bot.callback_query_handler(func=lambda call: call.data == 'c_a2')
@bot.callback_query_handler(func=lambda call: call.data == 'c_a3')
@bot.callback_query_handler(func=lambda call: call.data == 'c_a4')
def china_words_2(call):
    if call.data == 'c_a1':
        msg = '是 (shì)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_a2':
        msg = '不 (bù)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_a3':
        msg = '谢谢 (xièxie)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_a4':
        msg = '不用谢 (bùkèqì)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'c_f1')
@bot.callback_query_handler(func=lambda call: call.data == 'c_f2')
@bot.callback_query_handler(func=lambda call: call.data == 'c_f3')
@bot.callback_query_handler(func=lambda call: call.data == 'c_f4')
def china_words_3(call):
    if call.data == 'c_f1':
        msg = '米饭 (mǐfàn)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_f2':
        msg = '面条 (miàntiáo)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_f3':
        msg = '豆腐 (dòufu)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_f4':
        msg = '鱼 (yú)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'c_col1')
@bot.callback_query_handler(func=lambda call: call.data == 'c_col2')
@bot.callback_query_handler(func=lambda call: call.data == 'c_col3')
@bot.callback_query_handler(func=lambda call: call.data == 'c_col4')
def china_words_4(call):
    if call.data == 'c_col1':
        msg = '黑色 (hēisè)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_col2':
        msg = '蓝色 (lánsè)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_col3':
        msg = '绿色 (lǜsè)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_col4':
        msg = '红色 (hóngsè)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'c_g1')
@bot.callback_query_handler(func=lambda call: call.data == 'c_g2')
@bot.callback_query_handler(func=lambda call: call.data == 'c_g3')
@bot.callback_query_handler(func=lambda call: call.data == 'c_g4')
def china_words_5(call):
    if call.data == 'c_g1':
        msg = '裙子 (qúnzi)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_g2':
        msg = '衬衫 (chènshān)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_g3':
        msg = '西装 (xīzhuāng)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_g4':
        msg = '牛仔裤 (niúzǎikù)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'c_s1')
@bot.callback_query_handler(func=lambda call: call.data == 'c_s2')
@bot.callback_query_handler(func=lambda call: call.data == 'c_s3')
@bot.callback_query_handler(func=lambda call: call.data == 'c_s4')
def china_words_6(call):
    if call.data == 'c_s1':
        msg = '春天 (chūntiān)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_s2':
        msg = '秋天 (qiūtiān)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_s3':
        msg = '夏天 (xiàtiān)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_s4':
        msg = '冬天 (dōngtiān)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


@bot.callback_query_handler(func=lambda call: call.data == 'c_sp1')
@bot.callback_query_handler(func=lambda call: call.data == 'c_sp2')
@bot.callback_query_handler(func=lambda call: call.data == 'c_sp3')
@bot.callback_query_handler(func=lambda call: call.data == 'c_sp4')
def china_words_7(call):
    if call.data == 'c_sp1':
        msg = '图书馆 (túshūguǎn)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_sp2':
        msg = '酒吧 (jiǔbā)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_sp3':
        msg = '商场 (shāngchǎng)'
        bot.send_message(call.message.chat.id, msg)
    if call.data == 'c_sp4':
        msg = '公园 (gōngyuán)'
        bot.send_message(call.message.chat.id, msg)
    bot.send_message(call.message.chat.id, 'Для перезапуска бота нажмите /start')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)