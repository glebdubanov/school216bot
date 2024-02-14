import telebot
from telebot import types


bot = telebot.TeleBot('6364983863:AAGJbYfSfmGOBGRXdIaaCS7Q2WPx468l0I4')


@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Справка')
    item2 = types.KeyboardButton('Электронный дневник')
    item3 = types.KeyboardButton('Сайт школы')
    item4 = types.KeyboardButton('Группа ВКонтакте')
    item5 = types.KeyboardButton('О форме')
    item6 = types.KeyboardButton('Как поговорить с директором')
    item7 = types.KeyboardButton('Расписание')

    markup.add(item1, item2, item3, item4, item5, item6, item7)
    file1 = open('./school216.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo=file1, caption='Здравствуйте, {0.first_name}, вы попали в школьный телеграм-бот МАОУ СОШ №216' .format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['photo', 'video', 'audio', 'files'])
def get_photo(message):
    bot.reply_to(message,'Нельзя отправлять фото, видео и аудиофайлы.')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help information')

@bot.message_handler(commands=['spravka'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='http://sch216nsk.edu54.ru/spravki'))
    bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти на сайт"', reply_markup=markup)



@bot.message_handler(commands=['dnevnik'])
def main(message):
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton('Перейти в электронный дневник', url='https://school.nso.ru'))
     bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти в электронный дневник"', reply_markup=markup)

@bot.message_handler(commands=['site'])
def main(message):
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url='http://sch216nsk.edu54.ru/'))
     bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти на сайт школы"', reply_markup=markup)

@bot.message_handler(commands=['vkontakte'])
def main(message):
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton('Перейти в группу ВКонтакте', url='https://vk.com/maousosh216'))
     bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти в группу ВКонтакте"', reply_markup=markup)

@bot.message_handler(commands=['forma'])
def main(message):
     file2 = open('./forma.jpeg', 'rb')
     bot.send_photo(message.chat.id, photo=file2, caption='По уставу МАОУ СОШ №216 все учащиеся обязаны носить школьную форму установленного образца. '
                                       'Школьная форма подразделяется на парадную, повседневную и спортивную. '
                                       'Необходимую информацию можно найти в Положении о требованиях к форме обучающих: '
                                       'http://sch216nsk.edu54.ru/uploads/oo/doc/polozhenie_o_trebovanii_k_forme_obuchayushyihsya.pdf')

@bot.message_handler(commands=['direktor'])
def main(message):
    bot.send_message(message.chat.id,
                          'Как поговорить с директором? У вас имеется просьба, претензия или пожелание лично для директора, необходимо с ним связаться? Личный приём директора ведется по понедельникам, с 17.00 до 19.00. Записаться на прием можно по телефону 246-09-01. Также можно написать обращение на сайт школы, на школьную почту и в наше сообщество ВКонтакте.')


@bot.message_handler(commands=['youtube'])
def main(message):
     markup = types.InlineKeyboardMarkup()
     markup.add(types.InlineKeyboardButton('Перейти на YouTube-канал школы', url='https://www.youtube.com/@No-eg8qq'))
     bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти на YouTube-канал школы"', reply_markup=markup)

@bot.message_handler(commands=['raspisanie'])
def main(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton('1 класс')
     btn2 = types.KeyboardButton('2 класс')
     btn3 = types.KeyboardButton('3 класс')
     btn4 = types.KeyboardButton('4 класс')
     btn5 = types.KeyboardButton('5 класс')
     btn6 = types.KeyboardButton('6 класс')
     btn7 = types.KeyboardButton('7 класс')
     btn8 = types.KeyboardButton('8 класс')
     btn9 = types.KeyboardButton('9 класс')
     btn10 = types.KeyboardButton('10 класс')
     btn11 = types.KeyboardButton('11 класс')
     markup.row(btn1,
                btn2,
                btn3,
                btn4,
                btn5,
                btn6,
                btn7,
                btn8,
                btn9,
                btn10,
                btn11)

     bot.send_message(message.chat.id, 'Выберите свой класс из списка:', reply_markup=markup)




     back = types.KeyboardButton('Назад')
     markup.row(btn1, back)
     bot.send_message(message.chat.id, 'Выберите свой класс из списка:', reply_markup=markup)

     bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == '8 класс':
        bot.send_message(message.chat.id, 'Расписание 8М класса:')
        file = open('./raspisanie_8m.jpeg', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Справка')
            item2 = types.KeyboardButton('Электронный дневник')
            item3 = types.KeyboardButton('Сайт школы')
            item4 = types.KeyboardButton('Группа ВКонтакте')
            item5 = types.KeyboardButton('О форме')
            item6 = types.KeyboardButton('Как поговорить с директором')
            item7 = types.KeyboardButton('Расписание')

            markup.add(item1, item2, item3, item4, item5, item6, item7)

            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)

        elif message.text == 'Справка':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на сайт', url='http://sch216nsk.edu54.ru/spravki'))
            bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти на сайт"', reply_markup=markup)

        elif message.text == 'Электронный дневник':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти в электронный дневник', url='https://school.nso.ru'))
            bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти в электронный дневник"', reply_markup=markup)

        elif message.text == 'Сайт школы':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url='http://sch216nsk.edu54.ru/'))
            bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти на сайт школы"', reply_markup=markup)

        elif message.text == 'Группа ВКонтакте':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти в группу ВКонтакте', url='https://vk.com/maousosh216'))
            bot.send_message(message.chat.id, 'Ниже нажмите на кнопку "Перейти в группу ВКонтакте"', reply_markup=markup)

        elif message.text == 'О форме':
            file2 = open('./forma.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo=file2,
                           caption='По уставу МАОУ СОШ №216 все учащиеся обязаны носить школьную форму установленного образца. '
                                   'Школьная форма подразделяется на парадную, повседневную и спортивную. '
                                   'Необходимую информацию можно найти в Положении о требованиях к форме обучающих: '
                                   'http://sch216nsk.edu54.ru/uploads/oo/doc/polozhenie_o_trebovanii_k_forme_obuchayushyihsya.pdf')

        elif message.text == 'Как поговорить с директором':
            bot.send_message(message.chat.id,'Как поговорить с директором? У вас имеется просьба, претензия или пожелание лично для директора, необходимо с ним связаться? Личный приём директора ведется по понедельникам, с 17.00 до 19.00. Записаться на прием можно по телефону 246-09-01. Также можно написать обращение на сайт школы, на школьную почту и в наше сообщество ВКонтакте.')

        elif message.text == 'Расписание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            btn1 = types.KeyboardButton('8М класс')
            back = types.KeyboardButton('Назад')
            markup.row(btn1, back)
            bot.send_message(message.chat.id, 'Выберите свой класс из списка:', reply_markup=markup)

            bot.register_next_step_handler(message, on_click)

def on_click(message):
            if message.text == '8М класс':
                file = open('./raspisanie_8m.jpeg', 'rb')
                bot.send_photo(message.chat.id, photo=file, caption='Расписание 8М класса:')


bot.polling(none_stop=True)

