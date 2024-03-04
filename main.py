import telebot
from telebot import types
from telebot import apihelper

apihelper.API_URL = "https://tgrasp.co/bot{0}/{1}" # Для подключения к аналитике (graspil.com), нужно заменить api.telegram.org на (https://tgrasp.co) следующей командой, чтобы сервис проксировал все запросы к телеграм и собирал статистику.

bot = telebot.TeleBot('token', parse_mode='HTML') # Токен бота, а ниже идут переменные для текста и URL-ссылок
School_site='http://sch216nsk.edu54.ru/'
School_sitetext='⚪️ Ниже нажмите на кнопку <b>"Перейти на сайт школы"</b>'
School_spravka='http://sch216nsk.edu54.ru/spravki'
School_spravkatext='📄 Для заказа справки <b>перейдите на сайт школы.</b>\n' '\nЗаполните данные о своем ребенке, и на следующий день ваша справка окажется на вахте.'
School_dnevnik='https://school.nso.ru'
School_dnevniktext='📔 Ниже нажмите на кнопку <b>"Перейти в электронный дневник"</b>'
School_vkontakte='https://vk.com/maousosh216'
School_vkontaktetext='🔵 Ниже нажмите на кнопку <b>"Перейти в госпаблик ВКонтакте"</b>'
School_forma='http://sch216nsk.edu54.ru/uploads/oo/doc/polozhenie_o_trebovanii_k_forme_obuchayushyihsya.pdf'
School_formatext='👔 <b>О форме</b>\n' '\nПо уставу МАОУ СОШ №216 все учащиеся обязаны носить школьную форму установленного образца.\n' '\nШкольная форма подразделяется на парадную, повседневную и спортивную.\n' '\n📑 Необходимую информацию можно найти в Положении о требованиях к форме обучающих.\n' '\nНиже нажмите на кнопку <b>"Положение о требованиях к форме обучающихся"</b>\n'
School_firmitext='Уважаемые родители!' '\n🏭 Наша школа работает с четырьмя крупными фирмами - <b>Колибри, Непоседа, SAMM, Sky Lake</b>.''\n\nНапоминаем, что ТРИКОТАЖНЫЙ жилет темно-синего цвета с V-образной горловиной и шевроном, галстук с логотипом (утвержденного образца) для мальчиков / галстук-"птичка" с логотипом для девочек обязательны для всех учащихся с 1 по 4 класс включительно. С 5 класса трикотажный жилет может быть заменен на пиджак темно-синего цвета.''\nФасон брюк, юбок, сарафанов - это Ваш выбор, но родители должны помнить, что цвет этих изделий должен быть темно-синий. Под жилет допускается сорочка/блузка белая и/или пастельных тонов БЕЗ рисунка.' '\nКроме этого, можете приобрести свитшот с логотипом нашей школы + разрабатывается универсальная модель рубашки поло со школьным логотипом.' '\n\n<b>Контакты:</b>' '\n\n<b>Колибри:</b> Офис: г. Новосибирск,  ул. Богдана Хмельницкого 104' '\nТелефон: +7 (983) 305-80-06, 8-800-201-10-62' '\nE-mail: colibry@bk.ru' '\n\n<b>Непоседа:</b> Офис: г. Новосибирск, ул. Дачная 60, корпус 4.' '\nТелефон: +7 (383) 299-76-71, +7 (383) 299-76-72' '\nE-mail: opt@neposeda-school.ru' '\n\n<b>SAMM:</b> Офис: г. Новосибирск ул. Инская, 69/1 стр., 1 этаж' '\nТелефон: +7 (383) 383-05-55' '\nE-mail: samm-nsk@yandex.ru''\n\n<b>Sky Lake:</b> Телефон: +7 (495) 363-46-88, +7 (800) 505-46-88.' '\nE-mail: shop@skylake.ru'
School_futbolki='<b>К вопросу о цвете футболок для уроков физической культуры:</b>\n' '1 класс  -  🟠 оранжевый;\n' '2 класс  -  🟢 зеленый;\n' '3 класс  -  🟡 желтый;\n' '4 класс  -  🔵 голубой / синий;\n' '5 класс  -  🔴 красный;\n' '6 класс  -  🟠 оранжевый;\n' '7 класс  -  🟢 зеленый;\n' '8 класс  -  🟡 желтый;\n' '9 класс  -  🔵 голубой / синий;\n' '10 класс - ⚪️ белый;\n' '11 класс - ⚪ белый.\n'
School_obrashenie_gragdan='https://forms.yandex.ru/u/5e55d8b5a9a45e0a0ef27d06/'
School_youtube='https://www.youtube.com/@No-eg8qq'
School_youtubetext='🔴 Ниже нажмите на кнопку <b>"Перейти на YouTube - канал школы"</b>'
School_rutube='https://rutube.ru/channel/25383693/'
School_rutubetext='⚫️Ниже нажмите на кнопку <b>"Перейти на Rutube - канал школы"</b>'
School_conschasdlyarodit='http://www.sch216nsk.edu54.ru/uploads/parents/graph_consult_s_rodit_2023_2024.pdf'
School_conschasdlyarodittext='👨‍👩‍👧‍👦 Ниже нажмите на кнопку <b>"Конс. час для родителей"</b>'
School_conschasdlyadetey='http://sch216nsk.edu54.ru/uploads/parents/graph_consult_s_uchashimi_2023_2024.pdf'
School_conschasdlyadeteytext='👶🏻 Ниже нажмите на кнопку <b>"Конс. час для детей"</b>'
School_start='Здравствуйте, {0.first_name}, вы попали в школьный чат-бот <b>МАОУ СОШ № 216 г. Новосибирска</b>\n''\nЭтот бот предназначен для быстрого получения информации, касающейся учебного процесса <b>МАОУ СОШ №216.</b>'
School_direktor='️🤵🏻‍️<b>Как поговорить с директором?</b>\n' '\nУ вас имеется просьба, претензия или пожелание лично для директора, необходимо с ним связаться?\n' '\n🕒 Личный приём директора ведется по понедельникам, с 17.00 до 19.00.\n' '📞 Записаться на прием можно по телефону 246-09-01.\n' '\nТакже обращение можно оставить на сайте школы, либо написать на электронную почту s_216@edu54.ru и в наше сообщество (госпаблик) в социальной сети "ВКонтакте".\n'
School_sekretari='🤵🏻‍♀️ <b>Секретари</b>''\n\nПопасть к секретарям можно <b>через приёмную</b> и задать интересующий вас вопрос. \n\n🕒 График работы секретарей: <b>по будням с 14:00 до 17:00</b>'
School_zavuch='<b>️🤵🏼‍♀ ️Как поговорить с завучем?</b>\n' '\nЕсли у вас просьба, пожелание или вопрос к одному из заместителей директора, связаться с ним можно согласно нижеследующему графику дежурств:\n''\nВторник - <b>Кардаш Яна Александровна</b> (по вопросам ОВЗ и профориентации)\n''\nСреда - <b>Ольховик Ольга Константиновна</b> (по вопросам, связанным с уроками и индивидуальным обучением)\n''\nЧетверг - <b>Велетень Ольга Сергеевна</b> (по вопросам олимпиад и математических классов)\n''\nПятница - <b>Володина Елена Георгиевна</b> (по вопросам воспитания и школьных мероприятий)\n''\n📞 Записаться на прием <b>можно по телефону 246-09-01</b> (звонить в рабочее время).''\nТакже обращение можно оставить на сайте школы, либо написать на электронную почту s_216@edu54.ru и в наше сообщество (госпаблик) в социальной сети "ВКонтакте".'
School_zvonki='🔔 <b>Расписание</b> <b>звонков:</b>\n''<b>1-е, 4-е, 5-е и 10-е и 5С, 6М, 7М, 8М классы</b>\n''1 урок: 8:00 - 8:40\n''2 урок: 8:50 - 9:30\n''3 урок: 9:40 - 10:20\n''4 урок: 10:35 - 11:15\n''5 урок: 11:35 - 12:15\n''6 урок: 12:35 - 13:15\n''7 урок: 13:30 - 14:10\n''8 урок: 14:30 - 15:10\n''\n<b>2-е, 3-е, 6-е, 7-е, 8-е классы </b>\n''0 урок: 13:30 - 14:10\n''1 урок: 14:30 - 15:10\n''2 урок: 15:30 - 16:10\n''3 урок: 16:25 - 17:05\n''4 урок: 17:15 - 17:55\n''5 урок: 18:05 - 18:45\n''6 урок: 18:55 - 19:35\n''\n<b>9-е и 11-е классы </b>\n''1 урок: 8:50 - 9:30\n''2 урок: 9:40 - 10:20\n''3 урок: 10:35 - 11:15\n''4 урок: 11:35 - 12:15\n''5 урок: 12:35 - 13:15\n''6 урок: 13:30 - 14:10\n''7 урок: 14:30 - 15:10\n''8 урок: 15:30 - 16:10\n'
School_kanikuli='<b>Расписание</b> <b>каникул:</b>\n''с 28.10.2023 по 06.11.2023,\n''с 30.12.2023 по 08.01.2024,\n''с 23.03.2024 по 31.03.2024,\n''с 29.05.2024 — летние каникулы\n'
School_medblok='🏥 <b>Расписание мед.блока:</b>\n' '\nПонедельник - пятница: <b>с 8:00 до 19:00</b>\n' 'Обеденный перерыв: <b>с 12:30 до 16:00</b>\n' '\n🦷 <b>Стоматолог</b>\n' '\nПонедельник - пятница: <b>с 8:30 до 15:00</b>\n' '3-я суббота месяца: <b>с 9:00 до 14:30</b>\n' '\n<b>👩‍⚕️Зубной врач</b> - Переверзева Людмила Петровна\n' '\nПрием пациентов осуществляется при наличии заполненного, распечатанного и подписанного родителем (законным представителем) ребенка <b>добровольного информированного согласия</b>, с которым можно ознакомиться ниже.' '\nТакже добровольное информированное согласие можно заполнить в кабинете врача.\n' '\n<b>Записаться на прием</b> можно по т. 8-923-109-4098.''\n\nТелефон медиков: 246-09-03'
School_medbloksoglasie='https://vk.com/doc3128348_602877156?hash=iEu45Utfv9CxsDDXuhg800UQTOvz4FwOllgKsZujI1s&dl=O151cIeCvQ2NUzIusPzUq0oQv2WYN9WNxrj750bjR0o'
School_medbloksoglasietext='Информированное добровольное согласие'
School_podgotovishkatext='\n<b>Уважаемые родители!</b>\n' '\nС 11 сентября 2023 года открывается запись в «ШКОЛУ БУДУЩЕГО ПЕРВОКЛАССНИКА» через сайт https://navigator.edu54.ru/\n''\nПошаговая инструкция:' '\n1. Зайти на сайт https://navigator.edu54.ru/ , имея личную электронную почту родителя;''\n2. Нажать пункт – РЕГИСТРАЦИЯ;' '\n3. Заполнить все графы персональными данными;' '\n4. Нажать на кнопку ЗАРЕГИСТРОВАТЬ;''\n5. Зайти во вкладку ДЕТИ, заполнить информацию о ребенке;' '\n6. Подтвердить сертификат (для этого вам необходимо скачать и распечатать документы, прикрепленные ниже, приложить ксерокопию СНИЛС ребенка, ксерокопию свидетельства о рождении ребенка, ксерокопию паспорта родителя);''\n7. Запись будет открыта в одну группу, после этого дети будут распределены в случайном порядке.' '\nПОДТВЕРДИТЬ СЕРТИФИКАТ МОЖНО 13 СЕНТЯБРЯ. С 15:30 до 17.30 в холле первого этажа.\n''\nЖдем всех желающих детей дошкольного возраста для занятий в «ШКОЛЕ БУДУЩЕГО ПЕРВОКЛАССНИКА»' '\nПо всем интересующим вопросам можете обращаться по тел. 8-951-397-19-52 Стародубцева Александра Валерьевна.'
School_biblioteka='\n📚 <b>График работы библиотеки:</b>\n\n🕒 Библиотека работает с <b>8:00 - 16:00</b>, с понедельника по пятницу.\nПоследний день месяца - <b>санитарный</b>. \n\n🍽 Перерыв на обед: <b>12:00 - 13:00.</b>'
School_perviyklassurl='http://sch216nsk.edu54.ru/news/priem-detej-v-pervye-klassy-maou-sosh-216-g-novosibirska-2023-2024'
School_dopobrazovanieurl='http://sch216nsk.edu54.ru/dopolnitelnoe-obrazovanie'
School_nazad='Назад! Возвращаю вас в главное меню.'
menu1='Форма'
menu2='Наши соц.сети'
menu3='Расписания'
menu4='Как попасть...'
menu6='Подготовка к 1 классу'
menu7='Справка'
menu8='Конс. часы'
menu9='Навигатор ДО'
menu10='Эл.дневник'
menu11='Библиотека'
menu12='Доп.образование'
menu13='Микроучастки'
menu14='Как попасть в 1 класс'
@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Меню кнопок
    item1 = types.KeyboardButton(menu1)
    item2 = types.KeyboardButton(menu2)
    item3 = types.KeyboardButton(menu3)
    item4 = types.KeyboardButton(menu4)
    item6 = types.KeyboardButton(menu6)
    item7 = types.KeyboardButton(menu7)
    item8 = types.KeyboardButton(menu8)
    item9 = types.KeyboardButton(menu9)
    item10 = types.KeyboardButton(menu10)
    item11 = types.KeyboardButton(menu11)
    item12 = types.KeyboardButton(menu12)
    item13 = types.KeyboardButton(menu13)
    item14 = types.KeyboardButton(menu14)

    markup.add(item1, item2, item3, item4, item6, item7, item8, item9, item10, item11, item12, item13,
               item14)  # Добавление кнопок
    file1 = open('./school216.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo=file1,
                   caption=School_start.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['photo', 'video', 'audio', 'files']) # Если отправить фото, видео, аудио и другие файлы, то высветиться вот такое сообщение
def get_photo(message):
    bot.reply_to(message, 'Нельзя отправлять фото, видео и аудиофайлы. Пожалуйста, выберите интересующую вас информацию из кнопок ниже.')


@bot.message_handler(commands=['spravka'])  # Команда Справка
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url=School_spravka))
    bot.send_message(message.chat.id, School_spravkatext, reply_markup=markup)

@bot.message_handler(commands=['dnevnik'])  # Команда Дневник
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти в электронный дневник', url=School_dnevnik))
    bot.send_message(message.chat.id, School_dnevniktext, reply_markup=markup)


@bot.message_handler(commands=['site']) # Команда Сайт школы
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url=School_site))
    bot.send_message(message.chat.id, School_sitetext, reply_markup=markup)


@bot.message_handler(commands=['vkontakte']) # Команда Госпаблик ВКонтакте
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти в госпаблик ВКонтакте', url=School_vkontakte))
    bot.send_message(message.chat.id, School_vkontaktetext, reply_markup=markup)



@bot.message_handler(commands=['forma']) # Команда Форма
def main(message):
    file2 = open('./forma.jpeg', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Положение о требованиях к форме обучающихся',
                                          url=School_forma))
    bot.send_photo(message.chat.id, photo=file2, caption=School_formatext, reply_markup=markup)

@bot.message_handler(commands=['direktor']) # Команда Как попасть к директору
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                          url=School_vkontakte))
    markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                          url=School_obrashenie_gragdan))
    bot.send_message(message.chat.id, School_direktor, reply_markup=markup)
@bot.message_handler(commands=['youtube']) # Команда YouTube - канал
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на YouTube - канал школы', url=School_youtube))
    bot.send_message(message.chat.id, School_youtubetext, reply_markup=markup)

@bot.message_handler(commands=['rutube']) # Команда Rutube - канал
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на Rutube - канал школы', url=School_rutube))
    bot.send_message(message.chat.id, School_rutubetext, reply_markup=markup)


@bot.message_handler(commands=['futbolki'])  # Команда Футболки
def main(message):
    file3 = open('./futbolki.jpg', 'rb')
    bot.send_photo(message.chat.id, photo=file3, caption=School_futbolki)

@bot.message_handler(commands=['zvonki'])  # Команда Расписание звонков
def main(message):
    bot.send_message(message.chat.id, School_zvonki)

@bot.message_handler(commands=['kanikuli'])  # Команда Расписание каникул
def main(message):
    bot.send_message(message.chat.id, School_kanikuli)


@bot.message_handler(commands=['navigator']) # Команда Навигатор ДО
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Как зарегистрироваться в Навигаторе ДО (видео)',
                                          url='https://www.youtube.com/watch?v=G2Q1FDU4N1M'))
    bot.send_message(message.chat.id, 'Ниже нажмите на кнопку <b>"Как зарегистрироваться в Навигаторе ДО (видео)"</b>', reply_markup=markup)


@bot.message_handler(commands=['konschasdlyarodit']) # Команда Консультативные часы для родителей
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Конс. час для родителей',
                                          url=School_conschasdlyarodit))
    bot.send_message(message.chat.id, School_conschasdlyarodittext, reply_markup=markup)


@bot.message_handler(commands=['konschasdlyadetey']) # Команда Консультативные часы для детей
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Конс. час для детей', url=School_conschasdlyadetey))
    bot.send_message(message.chat.id, School_conschasdlyadeteytext, reply_markup=markup)


@bot.message_handler(commands=['medblok']) # Команда Расписание мед.блока и стоматолога
def main(message):
    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton(School_medbloksoglasietext, url=School_medbloksoglasie))
    bot.send_message(message.chat.id, School_medblok, reply_markup=markup1)


@bot.message_handler(commands=['zavuch']) # Команда Как попасть к завучам
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                          url=School_vkontakte))
    markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                          url=School_obrashenie_gragdan))
    bot.send_message(message.chat.id, School_zavuch, reply_markup=markup)

@bot.message_handler(commands=['podgotovishka']) # Команда Подготовка к первому классу
def main(message):
    file4 = open('./podgotovishka.jpg', 'rb')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Заявление от родителей',
                                          url='https://vk.com/doc3128348_670791114?hash=HvAcbMjNQxevVrN2S1A8w2kl6IPezR1NgoUk6jw11Qk&dl=M7YJkt7CUwrQZPZn8weBHYfqxCK5ztKmgXqFK92grz4'))
    markup.add(types.InlineKeyboardButton('Форма для оплаты',
                                          url='https://vk.com/doc3128348_670791115?hash=qsJcAN4enzibDAzE7OQ3u4EkEJVvOicdz6PEdY7ERck&dl=ujY3Te9QA7dMi2vE3SqHA9m6M05Zj7WqyPkFLpTJyAk'))
    markup.add(types.InlineKeyboardButton('Договор об оказании платных обр.услуг',
                                          url='https://vk.com/doc3128348_670791353?hash=B02g7DHf0K9UIJTrDjk9kCuBVqJcH9GZ4LuHAgMsets&dl=jNTEbj6ke7xA794s9ysmI0kwDfP2wO99toSK8mREgzD'))
    bot.send_photo(message.chat.id, photo=file4, caption=School_podgotovishkatext, reply_markup=markup)
@bot.message_handler(commands=['biblioteka']) # Команда График работы библиотеки
def main(message):
    bot.send_message(message.chat.id, School_biblioteka)
@bot.message_handler(commands=['perviyklass']) # Команда Как попасть в 1 класс
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Как попасть в 1 класс', url=School_perviyklassurl))
    bot.send_message(message.chat.id, '✏️ Ниже нажмите на кнопку <b>"Как попасть в 1 класс"</b>.', reply_markup=markup)


@bot.message_handler(commands=['mikrouchastki'])  # Команда Фото микроучастков
def main(message):
    file5 = open('./mikrouchastki.jpg', 'rb')
    bot.send_message(message.chat.id, 'Прикрепляю микроучастки:')
    bot.send_photo(message.chat.id, photo=file5)
@bot.message_handler(commands=['dopobrazovanie']) # Команда Доп.образование
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Дополнительное образование',
                                          url=School_dopobrazovanieurl))
    bot.send_message(message.chat.id, 'Ниже нажмите на кнопку <b>"Дополнительное образование"</b>.',
                     reply_markup=markup)


@bot.message_handler(commands=['firmi'])  # Команда Фирмы одежды нашей школы
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Колибри', url='https://colibrynsk.ru/'))
    markup.add(types.InlineKeyboardButton('Непоседа', url='http://neposeda-school.ru/'))
    markup.add(types.InlineKeyboardButton('SAMM', url='https://samm-nsk.ru/'))
    markup.add(types.InlineKeyboardButton('Sky Lake', url='https://skylake.ru/'))
    bot.send_message(message.chat.id, School_firmitext, reply_markup=markup)

@bot.message_handler(commands=['sekretari'])  # Команда Как попасть к секретарям
def main(message):
    bot.send_message(message.chat.id, School_sekretari)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Меню кнопок
            item1 = types.KeyboardButton(menu1)
            item2 = types.KeyboardButton(menu2)
            item3 = types.KeyboardButton(menu3)
            item4 = types.KeyboardButton(menu4)
            item6 = types.KeyboardButton(menu6)
            item7 = types.KeyboardButton(menu7)
            item8 = types.KeyboardButton(menu8)
            item9 = types.KeyboardButton(menu9)
            item10 = types.KeyboardButton(menu10)
            item11 = types.KeyboardButton(menu11)
            item12 = types.KeyboardButton(menu12)
            item13 = types.KeyboardButton(menu13)
            item14 = types.KeyboardButton(menu14)

            markup.add(item1, item2, item3, item4, item6, item7, item8, item9, item10, item11, item12, item13, item14)  # Добавление кнопок

            bot.send_message(message.chat.id, School_nazad, reply_markup=markup)

    elif message.text == 'Справка':  # Справка
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на сайт', url=School_spravka))
            bot.send_message(message.chat.id, School_spravkatext, reply_markup=markup)
    elif message.text == 'Эл.дневник': # Электронный дневник
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти в электронный дневник', url=School_dnevnik))
            bot.send_message(message.chat.id, School_dnevniktext, reply_markup=markup)

    elif message.text == 'Сайт школы': # Сайт школы
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на сайт школы', url=School_site))
            bot.send_message(message.chat.id, School_sitetext, reply_markup=markup)

    elif message.text == 'Госпаблик ВКонтакте': # Госпаблик ВКонтакте
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти в госпаблик ВКонтакте', url=School_vkontakte))
            bot.send_message(message.chat.id, School_vkontaktetext, reply_markup=markup)

    elif message.text == 'Для занятий': # Форма для занятий
            file2 = open('./forma.jpeg', 'rb')
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Положение о требованиях к форме обучающихся',
                                              url=School_forma))
            bot.send_photo(message.chat.id, photo=file2, caption=School_formatext,
                       reply_markup=markup)

    elif message.text == 'Директор': # Как попасть к директору
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                              url=School_vkontakte))
            markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                              url=School_obrashenie_gragdan))
            bot.send_message(message.chat.id, School_direktor, reply_markup=markup)

    elif message.text == 'Каникулы':  # Расписание каникул
        bot.send_message(message.chat.id, School_kanikuli)

    elif message.text == 'Звонки':  # Расписание звонков
        bot.send_message(message.chat.id, School_zvonki)

    elif message.text == 'Цвет футболок':  # Цвет футболок на физкультуру
            file3 = open('./futbolki.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=file3, caption=School_futbolki)

    elif message.text == 'YouTube - канал':  # YouTube - канал
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на YouTube - канал школы',
                                                  url=School_youtube))
            bot.send_message(message.chat.id, School_youtubetext, reply_markup=markup)
    elif message.text == 'Rutube - канал':  # Rutube - канал
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Перейти на Rutube - канал школы',
                                                  url='https://rutube.ru/channel/25383693/'))
            bot.send_message(message.chat.id, School_rutubetext, reply_markup=markup)
    elif message.text == 'Родители':  # Консультативные часы для родителей
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Конс. час для родителей',
                                                  url=School_conschasdlyarodit))
            bot.send_message(message.chat.id, School_conschasdlyarodittext, reply_markup=markup)
    elif message.text == 'Дети': # Консультативные часы для детей
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Конс. час для детей', url=School_conschasdlyadetey))
            bot.send_message(message.chat.id, School_conschasdlyadeteytext, reply_markup=markup)
    elif message.text == 'Навигатор ДО': # Навигатор ДО
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Как зарегистрироваться в Навигаторе ДО (видео)',
                                                  url='https://www.youtube.com/watch?v=G2Q1FDU4N1M'))
            bot.send_message(message.chat.id,
                             'Ниже нажмите на кнопку <b>"Как зарегистрироваться в Навигаторе ДО (видео)"</b>',
                             reply_markup=markup)
    elif message.text == 'Форма': # Меню кнопок Форма
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item17 = types.KeyboardButton('Для занятий')
            item18 = types.KeyboardButton('Цвет футболок')
            item19 = types.KeyboardButton('Фирмы')
            item20 = types.KeyboardButton('Назад')
            markup.add(item17, item18, item19, item20)
            bot.send_message(message.chat.id, 'Выберите, что вас интересует из формы:', reply_markup=markup)
    elif message.text == 'Наши соц.сети': # Меню кнопок Наши соц.сети
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item20 = types.KeyboardButton('Сайт школы')
            item21 = types.KeyboardButton('YouTube - канал')
            item22 = types.KeyboardButton('Госпаблик ВКонтакте')
            item35 = types.KeyboardButton('Назад')
            item23 = types.KeyboardButton('Rutube - канал')
            markup.add(item20, item21, item22, item23, item35)
            bot.send_message(message.chat.id, 'Выберите нужную соц.сеть:', reply_markup=markup)
    elif message.text == 'Расписания': # Меню кнопок Расписания
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item24 = types.KeyboardButton('Звонки')
            item25 = types.KeyboardButton('Мед.блок')
            item26 = types.KeyboardButton('Каникулы')
            item27 = types.KeyboardButton('Назад')
            markup.add(item24, item25, item26, item27)
            bot.send_message(message.chat.id, 'Выберите нужное вам расписание:', reply_markup=markup)
    elif message.text == 'Как попасть...': # Меню кнопок Как попасть...
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item28 = types.KeyboardButton('Директор')
            item29 = types.KeyboardButton('Завучи')
            item30 = types.KeyboardButton('Секретари')
            item31 = types.KeyboardButton('Назад')
            markup.add(item28, item29, item30, item31)
            bot.send_message(message.chat.id, 'Выберите, к кому вы хотите попасть:', reply_markup=markup)
    elif message.text == 'Завучи': # Как попасть к завучам
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Госпаблик ВКонтакте',
                                                  url=School_vkontakte))
            markup.add(types.InlineKeyboardButton('Обращение граждан МАОУ СОШ №216',
                                                  url=School_obrashenie_gragdan))
            bot.send_message(message.chat.id, School_zavuch, reply_markup=markup)

    elif message.text == 'Мед.блок':  # Расписание мед.блока и стоматолога
            markup1 = types.InlineKeyboardMarkup()
            markup1.add(types.InlineKeyboardButton(School_medbloksoglasietext,
                                                   url=School_medbloksoglasie))
            bot.send_message(message.chat.id, School_medblok, reply_markup=markup1)

    elif message.text == 'Подготовка к 1 классу': # Подготовка к первому классу
            file4 = open('./podgotovishka.jpg', 'rb')
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Заявление от родителей',
                                                  url='https://vk.com/doc3128348_670791114?hash=HvAcbMjNQxevVrN2S1A8w2kl6IPezR1NgoUk6jw11Qk&dl=M7YJkt7CUwrQZPZn8weBHYfqxCK5ztKmgXqFK92grz4'))
            markup.add(types.InlineKeyboardButton('Форма для оплаты',
                                                  url='https://vk.com/doc3128348_670791115?hash=qsJcAN4enzibDAzE7OQ3u4EkEJVvOicdz6PEdY7ERck&dl=ujY3Te9QA7dMi2vE3SqHA9m6M05Zj7WqyPkFLpTJyAk'))
            markup.add(types.InlineKeyboardButton('Договор об оказании платных обр.услуг',
                                                  url='https://vk.com/doc3128348_670791353?hash=B02g7DHf0K9UIJTrDjk9kCuBVqJcH9GZ4LuHAgMsets&dl=jNTEbj6ke7xA794s9ysmI0kwDfP2wO99toSK8mREgzD'))
            bot.send_photo(message.chat.id, photo=file4, caption=School_podgotovishkatext, reply_markup=markup)

    elif message.text == 'Конс. часы':  # Меню кнопок Конс.часы
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item31 = types.KeyboardButton('Дети')
            item32 = types.KeyboardButton('Родители')
            item33 = types.KeyboardButton('Назад')
            markup.add(item31, item32, item33)
            bot.send_message(message.chat.id, 'Выберите, что вам нужно:', reply_markup=markup)
    elif message.text == 'Библиотека': # Расписание работы библиотеки
            bot.send_message(message.chat.id, School_biblioteka)
    elif message.text == 'Как попасть в 1 класс': # Как попасть в 1 класс
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Как попасть в 1 класс',
                                              url=School_perviyklassurl))
            bot.send_message(message.chat.id, '✏️ Ниже нажмите на кнопку <b>"Как попасть в 1 класс"</b>.',
                         reply_markup=markup)
    elif message.text == 'Микроучастки': # Фото микроучастков
            file5 = open('./mikrouchastki.jpg', 'rb')
            bot.send_message(message.chat.id, 'Прикрепляю микроучастки:')
            bot.send_photo(message.chat.id, photo=file5)
    elif message.text == 'Доп.образование': # Доп.образование
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Дополнительное образование',
                                              url=School_dopobrazovanieurl))
            bot.send_message(message.chat.id, 'Ниже нажмите на кнопку <b>"Дополнительное образование"</b>.',  reply_markup=markup)
    elif message.text == 'Фирмы': # Фирмы одежды нашей школы
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Колибри', url='https://colibrynsk.ru/'))
            markup.add(types.InlineKeyboardButton('Непоседа', url='http://neposeda-school.ru/'))
            markup.add(types.InlineKeyboardButton('SAMM', url='https://samm-nsk.ru/'))
            markup.add(types.InlineKeyboardButton('Sky Lake', url='https://skylake.ru/'))
            bot.send_message(message.chat.id, School_firmitext, reply_markup=markup)
    elif message.text == 'Секретари': # Как попасть к секретарям
            bot.send_message(message.chat.id, '🤵🏻‍♀️ <b>Секретари</b>''\n\nПопасть к секретарям можно <b>через приёмную</b> и задать интересующий вас вопрос. \n\n🕒 График работы секретарей: <b>по будням с 14:00 до 17:00</b>')
    else:
            bot.send_message(message.chat.id, "Я вас не понял, выберите из кнопок ниже.") # Если человек в чат напишет непонятную команду для бота, то он выдаст такое сообщение

if __name__ == '__main__':
    print('Бот запущен!')
    bot.polling()

