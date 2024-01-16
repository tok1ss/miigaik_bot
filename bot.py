# -*- coding: utf-8 -*-


import telebot
from telebot import types

bot_token = '6567990017:AAEY-8wSfuG5v5Ve4jN_GfSJoPjAq7T9Q4Q'
bot = telebot.TeleBot(bot_token)
chat_id = '811622664'
#chat_id = '1137084318'

material_support = {
    'Тяжелое материальное положение': ['Подробное описание ситуации', 'Копия паспорта'],
    'Дети-сироты': ['Свидетельство о сметри родителей', 'Копия паспорт'],
    'Инвалиды 1,2 и 3 группы': ['Копия свидетельства об инвалидности', 'Копия паспорта'],
    'Студенты, находящиеся на диспансерном учетес хрон. заболеванием': ['Копия свидетельства об инвалидности', 'Копия паспорта'],
    'Компенсация проездных документов у иногородних студентов на тер. РФ': ['Оригинал билета', 'Копия паспорта'],
    'Студенческие семьи, имеющие детей': ['Копия свидетельства о регистрауии брака', 'Свидетельство о рождении ребенка', 'Справка с места учебы', 'Копия паспорта'],
    'Являющиеся членами многодетных семей': ['Справка о составе семьи', 'Копия удостоверения многодетной матери', 'Копия свидетельства о рождении', 'Копия паспорта'],
    'Студенты при вступлении в брак': ['Копия свидетельства о заключении брака', 'Копия паспорта'],
    'Студенты, проживающие в общежитии': ['Справка из общежития', 'Копия паспорта'],
    'Рождение ребенка': ['Свидетельство о рождении ребенка', 'Копия паспорта'],
    'Смерть одного из родителей': ['Свидетельство о сметри', 'Копия паспорта', 'Документы, подтверждающие факт родства'],
    'Наличие тяжелого заболевания': ['Справка из больницы', 'Копия паспорта'],
    'Лечение студента(преобретение медикаментов, прохождение платного обледования и т.д.)': ['Справка из больницы', 'Копия платежных документов','Копия паспорта'],
    'В случае возникновения кризисных ситаций: пожар, стихийные бедствия': ['Копия паспорта', 'Документы, подтверждающие признание студента пострадавшим'],
    'Иные категории студентов': ['Копия паспорта', 'Иные подтверждающие документы'],
}

scholarships =  {
    'Государственная академическая стипендия': ['Очная, бюджетная форма обучения', 'Отсутсвие задолжностей и оценок "удовлетворительно"', '3900 руб. при оценках: хорошо', '4825 руб. при оценках: хорошо > отлично', '5825 руб. при оценках: отлично > хорошо', '8075 руб. при оценках: отлично'],
    'Повышенная государственная академическая стипендия': ['Очная, бюджетная форма обучения', 'Отсутсвие задолжностей и оценок "удовлетворительно"','Наличие достижений в следующих видах деятельности: Учебная деятельность; Научная деятельность; Общественная деятельность; Культурно-творческая деятельность, Спортивная деятельность'],
    'Государственная социальная студента': ['Очная, бюджетная форма обучения', 'Дети-сироты и дети, оставшиеся без попечения родителей','Лица, потерявшие в период обучения родителей или родителя','Дети-инвалиды, инвалиды 1 и 2 групп, инвалиды с детства','Пострадавшие в результате аварии на Чернобыльской АЭС','Граждане, получившие государственную помощь','Инвалиды вследствие военной травмы или заболевания, полученных в период прохождения военной службы'],
    'Степендия аспирантам': ['Очная, бюджетная форма обучения', 'Отсутсвие задолжностей и оценок "удовлетворительно"'],
    
}

grants = {
    'Студенты-сироты': ['Копия паспорта', 'Копия справки из органов опеки и попечительства'],
    'Студенты-инвалиды': ['Копия паспорта', 'Копия документа, подтверждающего факт установления инвалидности'],
    'Студенты из многодетной семьи': ['Копия паспорта', 'Копия свидетельства о рождении студента', 'Копия удостоверения многодетной семьи или справка о составе семьи'],
    'Студенты, имеющие детей': ['Копия паспорта', 'Копия свидетельства о рождении ребенка'],
    'Студенты-участники военный действий': ['Копия паспорта', 'Копия удостоверения участника боевых действий'],
    'Студенты-чернобыльцы': ['Копия паспорта', 'Копия удостоверения эвакуированного, переселенного из зон радиоактивного загрязнения'],
    'Студенты, имеющие родителей-инвалидов, родителей-пенсионеров': ['Копия паспорта', 'Копия свидетельства о рождении студента','Копия дейсвтующих справок об инвалидности родителей или Копия пенсионных удостовенений родителей'],
    'Студенты из неполных семей': ['Копия паспорта', 'Копия свидетельства о рождении студента','Копия документа, подтверждающего наличие неполной семьи'],
    'Студенты, находящиеся на диспансерном учёте с хроническими заболеваниями': ['Копия паспорта', 'Копия справки из медицинского учреждения'],
    'Студенты, проживающие в общежитии': ['Копия паспорта', 'Оригинал справки из общежития'],
    'Студенты, не получающие стипендию': ['Копия паспорта', 'Справка из Управления бухгалтеркого учета(оригинал)'],
}

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_material_support = types.KeyboardButton('Материальная поддержка')
    item_scholarships = types.KeyboardButton('Стипендии')
    item_grants = types.KeyboardButton('Дотации')
    markup.add(item_material_support, item_scholarships, item_grants)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Материальная поддержка')
def handle_material_support(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for support in material_support:
        btn = types.KeyboardButton(support)
        markup.add(btn)
    markup.add(types.KeyboardButton('Назад'))
    bot.send_message(message.chat.id, "Размер выплаты зависит от возникших обстоятельств и подтверждающих документов.\nВыберите основание:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in material_support)
def handle_material_support_docs(message):
    support = message.text
    docs = material_support[support]
    bot.send_message(message.chat.id, f"Необходимые документы:\n" + '\n'.join(docs))

@bot.message_handler(func=lambda message: message.text == 'Стипендии')
def handle_scholarships(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for scholarship in scholarships:
        btn = types.KeyboardButton(scholarship)
        markup.add(btn)
    markup.add(types.KeyboardButton('Назад'))
    bot.send_message(message.chat.id, "Выберите стипендию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in scholarships)
def handle_scholarship_criteria(message):
    scholarship = message.text
    criteria = scholarships[scholarship]
    bot.send_message(message.chat.id, f"Критерии для получения:\n" + '\n'.join(criteria))

@bot.message_handler(func=lambda message: message.text == 'Дотации')
def handle_grants(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    for grant in grants:
        btn = types.KeyboardButton(grant)
        markup.add(btn)
    markup.add(types.KeyboardButton('Назад'))
    bot.send_message(message.chat.id, "Подача документов на оказание выплаты проходит раз в полгода(~октябрь, апрель). \nРазмер выплаты - 1200 рублей.\nВыберите категорию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in grants)
def handle_grant_docs(message):
    grant = message.text
    docs = grants[grant]
    bot.send_message(message.chat.id, f"Необходимые документы:\n" + '\n'.join(docs))

@bot.message_handler(func=lambda message: message.text == 'Назад')
def handle_back(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_material_support = types.KeyboardButton('Материальная поддержка')
    item_scholarships = types.KeyboardButton('Стипендии')
    item_grants = types.KeyboardButton('Дотации')
    markup.add(item_material_support, item_scholarships, item_grants)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.message_handler(commands=['help'])
def handle_help(message):
    commands_info = (
        "/start - Начать взаимодействие с ботом\n"
        "/help - Вывести список всех команд\n"
        "/links - Показать полезные ссылки\n"
        "/info - Информация о проекте\n"
        "/social - Информация о службе соц. обеспечения\n"
        "/message - Обратиться в службу соц. обеспечения"
    )
    bot.send_message(message.chat.id, commands_info)



    
@bot.message_handler(commands=['message'])
def handle_message_command(message):
    # Проверяем, что команда содержит текст
    if len(message.text.split()) > 1:
        user_message = ' '.join(message.text.split()[1:])
        # Отправляем сообщение пользователю 
        bot.send_message(chat_id=chat_id, text = f"Получено новое сообщение от пользователя @{message.from_user.username}:\n{user_message}")
        
        # Отправляем уведомление пользователю, что сообщение успешно отправлено
        bot.send_message(message.chat.id, "Ваше сообщение успешно отправлено пользователю")
    else:
        # Если команда /message была введена без текста, отправляем уведомление о необходимости ввести сообщение
        bot.send_message(message.chat.id, "Вы забыли ввести текст сообщения. Используйте /message [текст сообщения].")


@bot.message_handler(commands=['links'])
def handle_links(message):
    bot.send_message(message.chat.id, "Полезные ссылки:\n1. [Профсоюз МИИГИиК](https://vk.com/profmycom)\n2. [МИИГАиК](https://vk.com/miigaik)")

@bot.message_handler(commands=['social'])
def handle_social(message):
    bot.send_message(message.chat.id, "Фактический адрес: г. Москва, Гороховский пер., 4, каб. 355\n\n Почтовый адрес: 105064, Москва, Гороховский пер., 4, Служба социального обеспечения\n\n Телефоны: 8 (499) 261-09-84 (доб. 4109) - руководитель Службы\n\n Адрес электронной почты по вопросам студентов и общим вопросам: sso.stip@miigaik.ru\n\n Адрес электронной почты для внутреннего взаимодействия: dom@miigaik.ru\n\n Режим работы:\nПН - ЧТ с 10.00 до 8.00\nПТ с 10.00 до 17.00\nОбед с 13.00 до 14.00")

@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в бота для просмотра видов социальной поддержки в МИИГАиК 🎓💼! Здесь ты можешь получить моментальный доступ к информации о стипендиях, дотациях и материальной помощи. Так же можно просмотреть информацию о работе службы социального обеспечения.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
