import telebot

token = '7000352105AAE6lRX_3sf-a0BFyFObBQ3j9_Izdo36RKI'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message)

    user = message.from_user
    first_name = user.first_name
    last_name = user.last_name

    if last_name
        bot.reply_to(message, fПривіт, {last_name}!)

#@bot.message_handler(func=lambda message True)
#def echo_all(message)
#   bot.reply_to(message, message.text)


@bot.message_handler(func=lambda message True)
def echo_all(message)
    if message.text.lower() == hello
        bot.reply_to(message, Hello!)
    else
        bot.reply_to(message, Good bye)


bot.polling()

Лістинг коду  
import telebot

token = '7000352105AAE6lRX_3sf-a0BFyFObBQ3j9_Izdo36RKI'

bot = telebot.TeleBot(token)

registered_users = {}  

@bot.message_handler(commands=['start'])
def start_message(message)
    bot.reply_to(message, Для початку реєстрації введіть команду registr)

@bot.message_handler(commands=['registr'])
def registration(message)
    chat_id = message.chat.id
    if chat_id not in registered_users 
        bot.reply_to(message, Введіть ваше ім'я)
        bot.register_next_step_handler(message, process_name_step)
    else
        bot.reply_to(message, Ви вже зареєстровані.)

def process_name_step(message)
    chat_id = message.chat.id
    name = message.text
    registered_users[chat_id] = {'name' name}
    bot.reply_to(message, Введіть ваше прізвище)
    bot.register_next_step_handler(message, process_surname_step)

def process_surname_step(message)
    chat_id = message.chat.id
    surname = message.text
    registered_users[chat_id]['surname'] = surname
    bot.reply_to(message, Введіть ваш вік)
    bot.register_next_step_handler(message, process_age_step)

def process_age_step(message)
    chat_id = message.chat.id
    try
        age = int(message.text)
        registered_users[chat_id]['age'] = age
        bot.reply_to(message, fВаш вік {age}. Реєстрація завершена.)
    except ValueError
        bot.reply_to(message, Будь ласка, введіть числове значення для віку.)

bot.polling()
