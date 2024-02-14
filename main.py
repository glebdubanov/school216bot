import telebot
from telebot import types


bot = telebot.TeleBot('token', parse_mode='HTML')
School_site='http://sch216nsk.edu54.ru/'
School_spravka='http://sch216nsk.edu54.ru/spravki'
School_dnevnik='https://school.nso.ru'
School_vkontakte='https://vk.com/maousosh216'
School_forma='http://sch216nsk.edu54.ru/uploads/oo/doc/polozhenie_o_trebovanii_k_forme_obuchayushyihsya.pdf'
School_obrashenie_gragdan='https://forms.yandex.ru/u/5e55d8b5a9a45e0a0ef27d06/'

@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Меню кнопок
    item1 = types.KeyboardButton('Форма')
    item2 = types.KeyboardButton('Наши соц.сети')
    item3 = types.KeyboardButton('Расписания')
    item4 = types.KeyboardButton('Как попасть...')
    item6 = types.KeyboardButton('Подготовка к 1 классу')
    item7 = types.KeyboardButton('Справка')
    item8 = types.KeyboardButton('Конс. часы')
    item9 = types.KeyboardButton('Навигатор ДО')
    item10 = types.KeyboardButton('Эл.дневник')
    item11 = types.KeyboardButton('Библиотека')
    item12 = types.KeyboardButton('Доп.образование')
    item13 = types.KeyboardButton('Микроучастки')
    item14 = types.KeyboardButton('Как попасть в 1 класс')

    markup.add(item1, item2, item3, item4, item6, item7, item8, item9, item10, item11, item12, item13, item14)  # Добавление кнопок
    file1 = open('./school216.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo=file1,
                   caption='Здравствуйте, {0.first_name}, вы попали в школьный чат-бот <b>МАОУ СОШ № 216 г. Новосибирска</b>\n''\nЭтот бот предназначен для быстрого получения информации, касающейся учебного процесса <b>МАОУ СОШ №216.</b>'.format(
                       message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['photo', 'video', 'audio', 'files'])
def get_photo(message):
    bot.reply_to(message, 'Нельзя отправлять фото, видео и аудиофайлы. Пожалуйста, выберите интересующую вас информацию из кнопок ниже.')


@bot.message_handler(commands=['spravka'])  # Команда Справка, и что появляется после команды
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url=School_spravka))
    bot.send_message(message.chat.id, '📄 Для заказа справки <b>перейдите на сайт школы.</b>\n' '\nЗаполните данные о своем ребенке, и на следующий день ваша справка окажется на вахте.', reply_markup=markup)


@bot.message_handler(commands=['dnevnik'])  # Команда Дневник, и что появляется после команды
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти в электронный дневник', url=School_dnevnik))
    bot.send_message(message.chat.id, '📔 Ниже нажмите на кнопку <b>"Перейти в электронный дневник"</b>',
                     reply_markup=markup)


@bot.message_handler(commands=['site'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url=School_site))
    bot.send_message(message.chat.id, '⚪️ Ниже нажмите на кнопку <b>"Перейти на сайт школы"</b>', reply_markup=markup)


@bot.message_handler(commands=['vkontakte'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти в госпаблик ВКонтакте', url=School_vkontakte))
    bot.send_message(message.chat.id, '🔵 Ниже нажмите на кнопку <b>"Перейти в госпаблик ВКонтакте"</b>',
                     reply_markup=markup)


@bot.message_handler(commands=['forma'])
def main(message):
    file2 = open('./forma.jpeg', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Положение о требованиях к форме обучающихся',
                                          url=School_forma))
    bot.send_photo(message.chat.id, photo=file2, caption='👔 <b>О форме</b>\n'
                                                         '\nПо уставу МАОУ СОШ №216 все учащиеся обязаны носить школьную форму установленного образца.\n'
                                                         '\nШкольная форма подразделяется на парадную, повседневную и спортивную.\n'
                                                         '\n📑 Необходимую информацию можно найти в Положении о требованиях к форме обучающих.\n'
                                                         '\nНиже нажмите на кнопку <b>"Положение о требованиях к форме обучающихся"</b>\n',
                   reply_markup=markup)

@bot.message_handler(commands=['direktor'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                          url=School_vkontakte))
    markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                          url=School_obrashenie_gragdan))
    bot.send_message(message.chat.id,
                     '️🤵🏻‍️<b>Как поговорить с директором?</b>\n' '\nУ вас имеется просьба, претензия или пожелание лично для директора, необходимо с ним связаться?\n' '\n🕒 Личный приём директора ведется по понедельникам, с 17.00 до 19.00.\n'
                     '📞 Записаться на прием можно по телефону 246-09-01.\n' '\nТакже обращение можно оставить на сайте школы, либо написать на электронную почту s_216@edu54.ru и в наше сообщество (госпаблик) в социальной сети "ВКонтакте".\n', reply_markup=markup)


@bot.message_handler(commands=['youtube'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на YouTube - канал школы', url='https://www.youtube.com/@No-eg8qq'))
    bot.send_message(message.chat.id, '🔴 Ниже нажмите на кнопку <b>"Перейти на YouTube - канал школы"</b>',
                     reply_markup=markup)

@bot.message_handler(commands=['rutube'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на Rutube - канал школы', url='https://rutube.ru/channel/25383693/'))
    bot.send_message(message.chat.id, '⚫️Ниже нажмите на кнопку <b>"Перейти на Rutube - канал школы"</b>',
                     reply_markup=markup)


@bot.message_handler(commands=['futbolki'])  # Команда Футболки, и что появляется после команды
def main(message):
    file3 = open('./futbolki.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=file3,
                   caption='<b>К вопросу о цвете футболок для уроков физической культуры:</b>\n'
                           '1 класс  -  🟠 оранжевый;\n'
                           '2 класс  -  🟢 зеленый;\n'
                           '3 класс  -  🟡 желтый;\n'
                           '4 класс  -  🔵 голубой / синий;\n'
                           '5 класс  -  🔴 красный;\n'
                           '6 класс  -  🟠 оранжевый;\n'
                           '7 класс  -  🟢 зеленый;\n'
                           '8 класс  -  🟡 желтый;\n'
                           '9 класс  -  🔵 голубой / синий;\n'
                           '10 класс - ⚪️ белый;\n'
                           '11 класс - ⚪ белый.\n')


@bot.message_handler(commands=['zvonki'])
def main(message):
    bot.send_message(message.chat.id, '<b>Расписание</b> <b>звонков:</b>\n'
                                      '<b>1-е, 4-е, 5-е и 10-е и 5С, 6М, 7М, 8М классы</b>\n'
                                      '1 урок: 8:00 - 8:40\n'
                                      '2 урок: 8:50 - 9:30\n'
                                      '3 урок: 9:40 - 10:20\n'
                                      '4 урок: 10:35 - 11:15\n'
                                      '5 урок: 11:35 - 12:15\n'
                                      '6 урок: 12:35 - 13:15\n'
                                      '7 урок: 13:30 - 14:10\n'
                                      '8 урок: 14:30 - 15:10\n'
                                      '\n<b>2-е, 3-е, 6-е, 7-е, 8-е классы </b>\n'
                                      '0 урок: 13:30 - 14:10\n'
                                      '1 урок: 14:30 - 15:10\n'
                                      '2 урок: 15:30 - 16:10\n'
                                      '3 урок: 16:25 - 17:05\n'
                                      '4 урок: 17:15 - 17:55\n'
                                      '5 урок: 18:05 - 18:45\n'
                                      '6 урок: 18:55 - 19:35\n'
                                      '\n<b>9-е и 11-е классы </b>\n'
                                      '1 урок: 8:50 - 9:30\n'
                                      '2 урок: 9:40 - 10:20\n'
                                      '3 урок: 10:35 - 11:15\n'
                                      '4 урок: 11:35 - 12:15\n'
                                      '5 урок: 12:35 - 13:15\n'
                                      '6 урок: 13:30 - 14:10\n'
                                      '7 урок: 14:30 - 15:10\n'
                                      '8 урок: 15:30 - 16:10\n')


@bot.message_handler(commands=['kanikuli'])
def main(message):
    bot.send_message(message.chat.id, '<b>Расписание</b> <b>каникул:</b>\n'
                                      'с 28.10.2023 по 06.11.2023,\n'
                                      'с 30.12.2023 по 08.01.2024,\n'
                                      'с 23.03.2024 по 31.03.2024,\n'
                                      'с 29.05.2024 — летние каникулы\n')


@bot.message_handler(commands=['navigator'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Как зарегистрироваться в Навигаторе ДО (видео)',
                                          url='https://www.youtube.com/watch?v=G2Q1FDU4N1M'))
    bot.send_message(message.chat.id, 'Ниже нажмите на кнопку <b>"Как зарегистрироваться в Навигаторе ДО (видео)"</b>',
                     reply_markup=markup)


@bot.message_handler(commands=['konschasdlyarodit'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Конс. час для родителей',
                                          url='http://www.sch216nsk.edu54.ru/uploads/parents/graph_consult_s_rodit_2023_2024.pdf'))
    bot.send_message(message.chat.id, '👨‍👩‍👧‍👦 Ниже нажмите на кнопку <b>"Конс. час для родителей"</b>', reply_markup=markup)


@bot.message_handler(commands=['konschasdlyadetey'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Конс. час для детей',
                                          url='http://sch216nsk.edu54.ru/uploads/parents/graph_consult_s_uchashimi_2023_2024.pdf'))
    bot.send_message(message.chat.id, '👶🏻 Ниже нажмите на кнопку <b>"Конс. час для детей"</b>', reply_markup=markup)


@bot.message_handler(commands=['medblok'])
def main(message):
    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('Информированное добровольное согласие',
                                           url='https://vk.com/doc3128348_602877156?hash=iEu45Utfv9CxsDDXuhg800UQTOvz4FwOllgKsZujI1s&dl=O151cIeCvQ2NUzIusPzUq0oQv2WYN9WNxrj750bjR0o'))
    bot.send_message(message.chat.id,
                     '🏥 <b>Расписание мед.блока:</b>\n' '\nПонедельник - пятница: <b>с 8:00 до 19:00</b>\n' 'Обеденный перерыв: <b>с 12:30 до 16:00</b>\n' '\n🦷 <b>Стоматолог</b>\n' '\nПонедельник - пятница: <b>с 8:30 до 15:00</b>\n' '3-я суббота месяца: <b>с 9:00 до 14:30</b>\n' '\n<b>👩‍⚕️Зубной врач</b> - Переверзева Людмила Петровна\n' '\nПрием пациентов осуществляется при наличии заполненного, распечатанного и подписанного родителем (законным представителем) ребенка <b>добровольного информированного согласия</b>, с которым можно ознакомиться ниже.' '\nТакже добровольное информированное согласие можно заполнить в кабинете врача.\n' '\n<b>Записаться на прием</b> можно по т. 8-923-109-4098.''\n\nТелефон медиков: 246-09-03', reply_markup=markup1)



@bot.message_handler(commands=['zavuch'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                          url=School_vkontakte))
    markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                          url=School_obrashenie_gragdan))
    bot.send_message(message.chat.id, '<b>️🤵🏼‍♀ ️Как поговорить с завучем?</b>\n' '\nЕсли у вас просьба, пожелание или вопрос к одному из заместителей директора, связаться с ним можно согласно нижеследующему графику дежурств:\n'
'\nВторник - <b>Кардаш Яна Александровна</b> (по вопросам ОВЗ и профориентации)\n'
'\nСреда - <b>Ольховик Ольга Константиновна</b> (по вопросам, связанным с уроками и индивидуальным обучением)\n'
'\nЧетверг - <b>Велетень Ольга Сергеевна</b> (по вопросам олимпиад и математических классов)\n'
'\nПятница - <b>Володина Елена Георгиевна</b> (по вопросам воспитания и школьных мероприятий)\n'
'\n📞 Записаться на прием <b>можно по телефону 246-09-01</b> (звонить в рабочее время).'
'\nТакже обращение можно оставить на сайте школы, либо написать на электронную почту s_216@edu54.ru и в наше сообщество (госпаблик) в социальной сети "ВКонтакте".', reply_markup=markup)


@bot.message_handler(commands=['podgotovishka'])
def main(message):
    file4 = open('./podgotovishka.jpg', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Заявление от родителей',
                                          url='https://vk.com/doc3128348_670791114?hash=HvAcbMjNQxevVrN2S1A8w2kl6IPezR1NgoUk6jw11Qk&dl=M7YJkt7CUwrQZPZn8weBHYfqxCK5ztKmgXqFK92grz4'))
    markup.add(types.InlineKeyboardButton('Форма для оплаты',
                                          url='https://vk.com/doc3128348_670791115?hash=qsJcAN4enzibDAzE7OQ3u4EkEJVvOicdz6PEdY7ERck&dl=ujY3Te9QA7dMi2vE3SqHA9m6M05Zj7WqyPkFLpTJyAk'))
    markup.add(types.InlineKeyboardButton('Договор об оказании платных обр.услуг',
                                          url='https://vk.com/doc3128348_670791353?hash=B02g7DHf0K9UIJTrDjk9kCuBVqJcH9GZ4LuHAgMsets&dl=jNTEbj6ke7xA794s9ysmI0kwDfP2wO99toSK8mREgzD'))
    bot.send_photo(message.chat.id, photo=file4,
                   caption='\n<b>Уважаемые родители!</b>\n' '\nС 11 сентября 2023 года открывается запись в «ШКОЛУ БУДУЩЕГО ПЕРВОКЛАССНИКА» через сайт https://navigator.edu54.ru/\n'
                   '\nПошаговая инструкция:' '\n1. Зайти на сайт https://navigator.edu54.ru/ , имея личную электронную почту родителя;' 
                   '\n2. Нажать пункт – РЕГИСТРАЦИЯ;' '\n3. Заполнить все графы персональными данными;' '\n4. Нажать на кнопку ЗАРЕГИСТРОВАТЬ;' 
                           '\n5. Зайти во вкладку ДЕТИ, заполнить информацию о ребенке;' '\n6. Подтвердить сертификат (для этого вам необходимо скачать и распечатать документы, прикрепленные ниже, приложить ксерокопию СНИЛС ребенка, ксерокопию свидетельства о рождении ребенка, ксерокопию паспорта родителя);'
                   '\n7. Запись будет открыта в одну группу, после этого дети будут распределены в случайном порядке.' '\nПОДТВЕРДИТЬ СЕРТИФИКАТ МОЖНО 13 СЕНТЯБРЯ. С 15:30 до 17.30 в холле первого этажа.\n'
                   '\nЖдем всех желающих детей дошкольного возраста для занятий в «ШКОЛЕ БУДУЩЕГО ПЕРВОКЛАССНИКА»' '\nПо всем интересующим вопросам можете обращаться по тел. 8-951-397-19-52 Стародубцева Александра Валерьевна.', reply_markup = markup)

@bot.message_handler(commands=['biblioteka'])
def main(message):
    bot.send_message(message.chat.id,
                     '\n📚 <b>График работы библиотеки:</b>\n\n🕒 Библиотека работает с <b>8:00 - 16:00</b>, с понедельника по пятницу.\nПоследний день месяца - <b>санитарный</b>. \n\n🍽 Перерыв на обед: <b>12:00 - 13:00.</b>')
@bot.message_handler(commands=['perviyklass'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Как попасть в 1 класс',
                                          url='http://sch216nsk.edu54.ru/news/priem-detej-v-pervye-klassy-maou-sosh-216-g-novosibirska-2023-2024'))
    bot.send_message(message.chat.id, '✏️ Ниже нажмите на кнопку <b>"Как попасть в 1 класс"</b>.',
                     reply_markup=markup)
@bot.message_handler(commands=['mikrouchastki'])
def main(message):
    file5 = open('./mikrouchastki.jpg', 'rb')
    bot.send_message(message.chat.id, 'Прикрепляю микроучастки:')
    bot.send_photo(message.chat.id, photo=file5)
@bot.message_handler(commands=['dopobrazovanie'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Дополнительное образование',
                                          url='http://sch216nsk.edu54.ru/dopolnitelnoe-obrazovanie'))
    bot.send_message(message.chat.id, 'Ниже нажмите на кнопку <b>"Дополнительное образование"</b>.',
                     reply_markup=markup)
@bot.message_handler(commands=['firmi'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Колибри', url='https://colibrynsk.ru/'))
    markup.add(types.InlineKeyboardButton('Непоседа', url='http://neposeda-school.ru/'))
    markup.add(types.InlineKeyboardButton('SAMM', url='https://samm-nsk.ru/'))
    markup.add(types.InlineKeyboardButton('Sky Lake', url='https://skylake.ru/'))
    bot.send_message(message.chat.id,
                     'Уважаемые родители!' '\n🏭 Наша школа работает с четырьмя крупными фирмами - <b>Колибри, Непоседа, SAMM, Sky Lake</b>.'
                     '\n\nНапоминаем, что ТРИКОТАЖНЫЙ жилет темно-синего цвета с V-образной горловиной и шевроном, галстук с логотипом (утвержденного образца) для мальчиков / галстук-"птичка" с логотипом для девочек обязательны для всех учащихся с 1 по 4 класс включительно. С 5 класса трикотажный жилет может быть заменен на пиджак темно-синего цвета.'
                     '\nФасон брюк, юбок, сарафанов - это Ваш выбор, но родители должны помнить, что цвет этих изделий должен быть темно-синий. Под жилет допускается сорочка/блузка белая и/или пастельных тонов БЕЗ рисунка.' '\nКроме этого, можете приобрести свитшот с логотипом нашей школы + разрабатывается универсальная модель рубашки поло со школьным логотипом.' '\n\n<b>Контакты:</b>' '\n\n<b>Колибри:</b> Офис: г. Новосибирск,  ул. Богдана Хмельницкого 104' '\nТелефон: +7 (983) 305-80-06, 8-800-201-10-62' '\nE-mail: colibry@bk.ru' '\n\n<b>Непоседа:</b> Офис: г. Новосибирск, ул. Дачная 60, корпус 4.' '\nТелефон: +7 (383) 299-76-71, +7 (383) 299-76-72' '\nE-mail: opt@neposeda-school.ru' '\n\n<b>SAMM:</b> Офис: г. Новосибирск ул. Инская, 69/1 стр., 1 этаж' '\nТелефон: +7 (383) 383-05-55' '\nE-mail: samm-nsk@yandex.ru'
                     '\n\n<b>Sky Lake:</b> Телефон: +7 (495) 363-46-88, +7 (800) 505-46-88.' '\nE-mail: shop@skylake.ru',
                     reply_markup=markup)
@bot.message_handler(commands=['sekretari'])
def main(message):
    bot.send_message(message.chat.id, '🤵🏻‍♀️ <b>Секретари</b>''\n\nПопасть к секретарям можно <b>через приёмную</b> и задать интересующий вас вопрос. \n\n🕒 График работы секретарей: <b>по будням с 14:00 до 17:00</b>')
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Меню кнопок
            item1 = types.KeyboardButton('Форма')
            item2 = types.KeyboardButton('Наши соц.сети')
            item3 = types.KeyboardButton('Расписания')
            item4 = types.KeyboardButton('Как попасть...')
            item6 = types.KeyboardButton('Подготовка к 1 классу')
            item7 = types.KeyboardButton('Справка')
            item8 = types.KeyboardButton('Конс. часы')
            item9 = types.KeyboardButton('Навигатор ДО')
            item10 = types.KeyboardButton('Эл.дневник')
            item11 = types.KeyboardButton('Библиотека')
            item12 = types.KeyboardButton('Доп.образование')
            item13 = types.KeyboardButton('Микроучастки')
            item14 = types.KeyboardButton('Как попасть в 1 класс')

            markup.add(item1, item2, item3, item4, item6, item7, item8, item9, item10, item11, item12, item13, item14)  # Добавление кнопок

            bot.send_message(message.chat.id, 'Назад! Возвращаю вас в главное меню.', reply_markup=markup)

    elif message.text == 'Справка':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на сайт', url=School_spravka))
            bot.send_message(message.chat.id, '📄 Для заказа справки <b>перейдите на сайт школы.</b>\n' '\nЗаполните данные о своем ребенке, и на следующий день ваша справка окажется на вахте.', reply_markup=markup)

    elif message.text == 'Эл.дневник':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти в электронный дневник', url=School_dnevnik))
            bot.send_message(message.chat.id, '📔 Ниже нажмите на кнопку <b>"Перейти в электронный дневник"</b>',
                             reply_markup=markup)

    elif message.text == 'Сайт школы':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url=School_site))
            bot.send_message(message.chat.id, '⚪️ Ниже нажмите на кнопку <b>"Перейти на сайт школы"</b>',
                             reply_markup=markup)

    elif message.text == 'Госпаблик ВКонтакте':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти в госпаблик ВКонтакте', url=School_vkontakte))
            bot.send_message(message.chat.id, '🔵 Ниже нажмите на кнопку <b>"Перейти в госпаблик ВКонтакте"</b>',
                             reply_markup=markup)

    elif message.text == 'Для занятий':
            file2 = open('./forma.jpeg', 'rb')
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Положение о требованиях к форме обучающихся',
                                              url=School_forma))
            bot.send_photo(message.chat.id, photo=file2, caption='<b>👔 О форме</b>\n'
                                                             '\nПо уставу МАОУ СОШ №216 все учащиеся обязаны носить школьную форму установленного образца.\n'
                                                             '\nШкольная форма подразделяется на парадную, повседневную и спортивную.\n'
                                                             '\n📑 Необходимую информацию можно найти в Положении о требованиях к форме обучающих.\n'
                                                             '\nНиже нажмите на кнопку <b>"Положение о требованиях к форме обучающихся"</b>\n',
                       reply_markup=markup)

    elif message.text == 'Директор':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                              url=School_vkontakte))
            markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                              url=School_obrashenie_gragdan))
            bot.send_message(message.chat.id,
                             '🤵🏻<b>Как поговорить с директором?</b>\n' '\nУ вас имеется просьба, претензия или пожелание лично для директора, необходимо с ним связаться?\n' '\n🕒 Личный приём директора ведется по понедельникам, с 17.00 до 19.00.\n'
                             '📞 Записаться на прием можно по телефону 246-09-01.\n' '\nТакже обращение можно оставить на сайте школы, либо написать на электронную почту s_216@edu54.ru и в наше сообщество (госпаблик) в социальной сети "ВКонтакте".\n', reply_markup=markup)

    elif message.text == 'Каникулы':
            bot.send_message(message.chat.id, '<b>Расписание</b> <b>каникул:</b>\n'
                                              'с 28.10.2023 по 06.11.2023,\n'
                                              'с 30.12.2023 по 08.01.2024,\n'
                                              'с 23.03.2024 по 31.03.2024,\n'
                                              'с 29.05.2024 — летние каникулы\n')
    elif message.text == 'Звонки':
            bot.send_message(message.chat.id, '🔔 <b>Расписание</b> <b>звонков:</b>\n'
                                              '<b>1-е, 4-е, 5-е и 10-е и 5С, 6М, 7М, 8М классы</b>\n'
                                              '1 урок: 8:00 - 8:40\n'
                                              '2 урок: 8:50 - 9:30\n'
                                              '3 урок: 9:40 - 10:20\n'
                                              '4 урок: 10:35 - 11:15\n'
                                              '5 урок: 11:35 - 12:15\n'
                                              '6 урок: 12:35 - 13:15\n'
                                              '7 урок: 13:30 - 14:10\n'
                                              '8 урок: 14:30 - 15:10\n'
                                              '\n<b>2-е, 3-е, 6-е, 7-е, 8-е классы </b>\n'
                                              '0 урок: 13:30 - 14:10\n'
                                              '1 урок: 14:30 - 15:10\n'
                                              '2 урок: 15:30 - 16:10\n'
                                              '3 урок: 16:25 - 17:05\n'
                                              '4 урок: 17:15 - 17:55\n'
                                              '5 урок: 18:05 - 18:45\n'
                                              '6 урок: 18:55 - 19:35\n'
                                              '\n<b>9-е и 11-е классы </b>\n'
                                              '1 урок: 8:50 - 9:30\n'
                                              '2 урок: 9:40 - 10:20\n'
                                              '3 урок: 10:35 - 11:15\n'
                                              '4 урок: 11:35 - 12:15\n'
                                              '5 урок: 12:35 - 13:15\n'
                                              '6 урок: 13:30 - 14:10\n'
                                              '7 урок: 14:30 - 15:10\n'
                                              '8 урок: 15:30 - 16:10\n')
    elif message.text == 'Цвет футболок':
            file3 = open('./futbolki.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=file3,
                           caption='<b>К вопросу о цвете футболок для уроков физической культуры:</b>\n'
                                   '1 класс  -  🟠 оранжевый;\n'
                           '2 класс  -  🟢 зеленый;\n'
                           '3 класс  -  🟡 желтый;\n'
                           '4 класс  -  🔵 голубой / синий;\n'
                           '5 класс  -  🔴 красный;\n'
                           '6 класс  -  🟠 оранжевый;\n'
                           '7 класс  -  🟢 зеленый;\n'
                           '8 класс  -  🟡 желтый;\n'
                           '9 класс  -  🔵 голубой / синий;\n'
                           '10 класс - ⚪️ белый;\n'
                           '11 класс - ⚪ белый.\n')
    elif message.text == 'YouTube - канал':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на YouTube - канал школы',
                                                  url='https://www.youtube.com/@No-eg8qq'))
            bot.send_message(message.chat.id, '🔴 Ниже нажмите на кнопку <b>"Перейти на YouTube - канал школы"</b>',
                             reply_markup=markup)
    elif message.text == 'Rutube - канал':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на Rutube - канал школы',
                                                  url='https://rutube.ru/channel/25383693/'))
            bot.send_message(message.chat.id, '⚫️ Ниже нажмите на кнопку <b>"Перейти на Rutube - канал школы"</b>',
                             reply_markup=markup)
    elif message.text == 'Родители':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Конс. час для родителей',
                                                  url='http://www.sch216nsk.edu54.ru/uploads/parents/graph_consult_s_rodit_2023_2024.pdf'))
            bot.send_message(message.chat.id, '👨‍👩‍👧‍👦 Ниже нажмите на кнопку <b>"Конс. час для родителей"</b>',
                             reply_markup=markup)
    elif message.text == 'Дети':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Конс. час для детей',
                                                  url='http://sch216nsk.edu54.ru/uploads/parents/graph_consult_s_uchashimi_2023_2024.pdf'))
            bot.send_message(message.chat.id, '👶🏻 Ниже нажмите на кнопку <b>"Конс. час для детей"</b>',
                             reply_markup=markup)
    elif message.text == 'Навигатор ДО':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Как зарегистрироваться в Навигаторе ДО (видео)',
                                                  url='https://www.youtube.com/watch?v=G2Q1FDU4N1M'))
            bot.send_message(message.chat.id,
                             'Ниже нажмите на кнопку <b>"Как зарегистрироваться в Навигаторе ДО (видео)"</b>',
                             reply_markup=markup)
    elif message.text == 'Форма':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item17 = types.KeyboardButton('Для занятий')
            item18 = types.KeyboardButton('Цвет футболок')
            item19 = types.KeyboardButton('Фирмы')
            item20 = types.KeyboardButton('Назад')
            markup.add(item17, item18, item19, item20)
            bot.send_message(message.chat.id, 'Выберите, что вас интересует из формы:', reply_markup=markup)
    elif message.text == 'Наши соц.сети':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item20 = types.KeyboardButton('Сайт школы')
            item21 = types.KeyboardButton('YouTube - канал')
            item22 = types.KeyboardButton('Госпаблик ВКонтакте')
            item35 = types.KeyboardButton('Назад')
            item23 = types.KeyboardButton('Rutube - канал')
            markup.add(item20, item21, item22, item23, item35)
            bot.send_message(message.chat.id, 'Выберите нужную соц.сеть:', reply_markup=markup)
    elif message.text == 'Расписания':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item24 = types.KeyboardButton('Звонки')
            item25 = types.KeyboardButton('Мед.блок')
            item26 = types.KeyboardButton('Каникулы')
            item27 = types.KeyboardButton('Назад')
            markup.add(item24, item25, item26, item27)
            bot.send_message(message.chat.id, 'Выберите нужное вам расписание:', reply_markup=markup)
    elif message.text == 'Как попасть...':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item28 = types.KeyboardButton('Директор')
            item29 = types.KeyboardButton('Завучи')
            item30 = types.KeyboardButton('Секретари')
            item31 = types.KeyboardButton('Назад')
            markup.add(item28, item29, item30, item31)
            bot.send_message(message.chat.id, 'Выберите, к кому вы хотите попасть:', reply_markup=markup)
    elif message.text == 'Завучи':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                                  url=School_vkontakte))
            markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                                  url=School_obrashenie_gragdan))
            bot.send_message(message.chat.id, '️🤵🏼‍♀️‍ <b>Как поговорить с завучем?</b>\n' '\nЕсли у вас просьба, пожелание или вопрос к одному из заместителей директора, связаться с ним можно согласно нижеследующему графику дежурств:\n'
'\nВторник - <b>Кардаш Яна Александровна</b> (по вопросам ОВЗ и профориентации)\n'
'\nСреда - <b>Ольховик Ольга Константиновна</b> (по вопросам, связанным с уроками и индивидуальным обучением)\n'
'\nЧетверг - <b>Велетень Ольга Сергеевна</b> (по вопросам олимпиад и математических классов)\n'
'\nПятница - <b>Володина Елена Георгиевна</b> (по вопросам воспитания и школьных мероприятий)\n'
'\n📞 Записаться на прием <b>можно по телефону 246-09-01</b> (звонить в рабочее время).'
'\nТакже обращение можно оставить на сайте школы, либо написать на электронную почту s_216@edu54.ru и в наше сообщество (госпаблик) в социальной сети "ВКонтакте".', reply_markup=markup)

    elif message.text == 'Мед.блок':
            markup1 = types.InlineKeyboardMarkup()
            markup1.add(types.InlineKeyboardButton('Информированное добровольное согласие',
                                               url='https://vk.com/doc3128348_602877156?hash=iEu45Utfv9CxsDDXuhg800UQTOvz4FwOllgKsZujI1s&dl=O151cIeCvQ2NUzIusPzUq0oQv2WYN9WNxrj750bjR0o'))
            bot.send_message(message.chat.id,
                             '🏥 <b>Расписание мед.блока:</b>\n' '\nПонедельник - пятница: <b>с 8:00 до 19:00</b>\n' 'Обеденный перерыв: <b>с 12:30 до 16:00</b>\n' '\n🦷 <b>Стоматолог</b>\n' '\nПонедельник - пятница: <b>с 8:30 до 15:00</b>\n' '3-я суббота месяца: <b>с 9:00 до 14:30</b>\n' '\n👩‍⚕️ <b>Зубной врач</b> - Переверзева Людмила Петровна\n' '\nПрием пациентов осуществляется при наличии заполненного, распечатанного и подписанного родителем (законным представителем) ребенка <b>добровольного информированного согласия</b>, с которым можно ознакомиться ниже.' '\nТакже добровольное информированное согласие можно заполнить в кабинете врача.\n' '\n<b>Записаться на прием</b> можно по т. 8-923-109-4098.''\n\n📞 Телефон медиков: 246-09-03', reply_markup=markup1)


    elif message.text == 'Подготовка к 1 классу':
            file4 = open('./podgotovishka.jpg', 'rb')
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Заявление от родителей',
                                                  url='https://vk.com/doc3128348_670791114?hash=HvAcbMjNQxevVrN2S1A8w2kl6IPezR1NgoUk6jw11Qk&dl=M7YJkt7CUwrQZPZn8weBHYfqxCK5ztKmgXqFK92grz4'))
            markup.add(types.InlineKeyboardButton('Форма для оплаты',
                                                  url='https://vk.com/doc3128348_670791115?hash=qsJcAN4enzibDAzE7OQ3u4EkEJVvOicdz6PEdY7ERck&dl=ujY3Te9QA7dMi2vE3SqHA9m6M05Zj7WqyPkFLpTJyAk'))
            markup.add(types.InlineKeyboardButton('Договор об оказании платных обр.услуг',
                                                  url='https://vk.com/doc3128348_670791353?hash=B02g7DHf0K9UIJTrDjk9kCuBVqJcH9GZ4LuHAgMsets&dl=jNTEbj6ke7xA794s9ysmI0kwDfP2wO99toSK8mREgzD'))
            bot.send_photo(message.chat.id, photo=file4,
                           caption='\n<b>Уважаемые родители!</b>\n' '\nС 11 сентября 2023 года открывается запись в «ШКОЛУ БУДУЩЕГО ПЕРВОКЛАССНИКА» через сайт https://navigator.edu54.ru/\n'
                                   '\nПошаговая инструкция:' '\n1. Зайти на сайт https://navigator.edu54.ru/ , имея личную электронную почту родителя;'
                                   '\n2. Нажать пункт – РЕГИСТРАЦИЯ;' '\n3. Заполнить все графы персональными данными;' '\n4. Нажать на кнопку ЗАРЕГИСТРОВАТЬ;'
                                   '\n5. Зайти во вкладку ДЕТИ, заполнить информацию о ребенке;' '\n6. Подтвердить сертификат (для этого вам необходимо скачать и распечатать документы, прикрепленные ниже, приложить ксерокопию СНИЛС ребенка, ксерокопию свидетельства о рождении ребенка, ксерокопию паспорта родителя);'
                                   '\n7. Запись будет открыта в одну группу, после этого дети будут распределены в случайном порядке.' '\nПОДТВЕРДИТЬ СЕРТИФИКАТ МОЖНО 13 СЕНТЯБРЯ. С 15:30 до 17.30 в холле первого этажа.\n'
                                   '\nЖдем всех желающих детей дошкольного возраста для занятий в «ШКОЛЕ БУДУЩЕГО ПЕРВОКЛАССНИКА»' '\nПо всем интересующим вопросам можете обращаться по тел. 8-951-397-19-52 Стародубцева Александра Валерьевна.',
                           reply_markup=markup)
    elif message.text == 'Конс. часы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item31 = types.KeyboardButton('Дети')
            item32 = types.KeyboardButton('Родители')
            item33 = types.KeyboardButton('Назад')
            markup.add(item31, item32, item33)
            bot.send_message(message.chat.id, 'Выберите, что вам нужно:', reply_markup=markup)
    elif message.text == 'Библиотека':
            bot.send_message(message.chat.id, '\n📚 <b>График работы библиотеки:</b>\n\n🕒 Библиотека работает с <b>8:00 - 16:00</b>, с понедельника по пятницу.\nПоследний день месяца - <b>санитарный</b>. \n\n🍽 Перерыв на обед: <b>12:00 - 13:00.</b>')
    elif message.text == 'Как попасть в 1 класс':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Как попасть в 1 класс',
                                              url='http://sch216nsk.edu54.ru/news/priem-detej-v-pervye-klassy-maou-sosh-216-g-novosibirska-2023-2024'))
            bot.send_message(message.chat.id, '✏️ Ниже нажмите на кнопку <b>"Как попасть в 1 класс"</b>.',
                         reply_markup=markup)
    elif message.text == 'Микроучастки':
            file5 = open('./mikrouchastki.jpg', 'rb')
            bot.send_message(message.chat.id, 'Прикрепляю микроучастки:')
            bot.send_photo(message.chat.id, photo=file5)
    elif message.text == 'Доп.образование':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Дополнительное образование',
                                              url='http://sch216nsk.edu54.ru/dopolnitelnoe-obrazovanie'))
            bot.send_message(message.chat.id, 'Ниже нажмите на кнопку <b>"Дополнительное образование"</b>.',  reply_markup=markup)
    elif message.text == 'Фирмы':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Колибри', url='https://colibrynsk.ru/'))
            markup.add(types.InlineKeyboardButton('Непоседа', url='http://neposeda-school.ru/'))
            markup.add(types.InlineKeyboardButton('SAMM', url='https://samm-nsk.ru/'))
            markup.add(types.InlineKeyboardButton('Sky Lake', url='https://skylake.ru/'))
            bot.send_message(message.chat.id,
                             'Уважаемые родители!' '\n🏭 Наша школа работает с четырьмя крупными фирмами - <b>Колибри, Непоседа, SAMM, Sky Lake</b>.'
                             '\n\nНапоминаем, что ТРИКОТАЖНЫЙ жилет темно-синего цвета с V-образной горловиной и шевроном, галстук с логотипом (утвержденного образца) для мальчиков / галстук-"птичка" с логотипом для девочек обязательны для всех учащихся с 1 по 4 класс включительно. С 5 класса трикотажный жилет может быть заменен на пиджак темно-синего цвета.'
                             '\nФасон брюк, юбок, сарафанов - это Ваш выбор, но родители должны помнить, что цвет этих изделий должен быть темно-синий. Под жилет допускается сорочка/блузка белая и/или пастельных тонов БЕЗ рисунка.' '\nКроме этого, можете приобрести свитшот с логотипом нашей школы + разрабатывается универсальная модель рубашки поло со школьным логотипом.' '\n\n<b>Контакты:</b>' '\n\n<b>Колибри:</b> Офис: г. Новосибирск,  ул. Богдана Хмельницкого 104' '\nТелефон: +7 (983) 305-80-06, 8-800-201-10-62' '\nE-mail: colibry@bk.ru' '\n\n<b>Непоседа:</b> Офис: г. Новосибирск, ул. Дачная 60, корпус 4.' '\nТелефон: +7 (383) 299-76-71, +7 (383) 299-76-72' '\nE-mail: opt@neposeda-school.ru' '\n\n<b>SAMM:</b> Офис: г. Новосибирск ул. Инская, 69/1 стр., 1 этаж' '\nТелефон: +7 (383) 383-05-55' '\nE-mail: samm-nsk@yandex.ru'
                             '\n\n<b>Sky Lake:</b> Телефон: +7 (495) 363-46-88, +7 (800) 505-46-88.' '\nE-mail: shop@skylake.ru', reply_markup=markup)
    elif message.text == 'Секретари':
            bot.send_message(message.chat.id, '🤵🏻‍♀️ <b>Секретари</b>''\n\nПопасть к секретарям можно <b>через приёмную</b> и задать интересующий вас вопрос. \n\n🕒 График работы секретарей: <b>по будням с 14:00 до 17:00</b>')
    else:
            bot.send_message(message.chat.id, "Я вас не понял, выберите из кнопок ниже.")

if __name__ == '__main__':
    print('Бот запущен!')
    bot.polling()

