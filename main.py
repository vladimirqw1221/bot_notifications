import telebot
from dotenv import load_dotenv
import os
import requests
import json
from table_user.database import DataBase

# Инициализация объекта для работы с базой данных
admins = DataBase()

# Загрузка переменных окружения
load_dotenv()
TOKEN = '6542640277:AAGnNXb-0DmXvwInthdYkh4fk6OOGaYDNYU'
bot = telebot.TeleBot(TOKEN)

# Функция для запроса имени пользователя
def request_name(message):
    bot.send_message(message.chat.id, "Пожалуйста, введите ваше имя:")
    bot.register_next_step_handler(message, check_user)

# Функция для проверки наличия пользователя в базе данных
def check_user(message):
    user_name = message.text.strip()
    user = admins.check_user(user_name)  # Проверяем наличие пользователя в базе данных
    if user:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Запустить тесты', callback_data='run_tests'))
        bot.send_message(message.chat.id, "Для запуска тестов нажмите кнопку ниже.", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "У вас нет прав доступа на запуск тестов. Обратитесь к администратору.")

# Функция для запуска тестов
# def post_run_test():
#     repo_owner = os.getenv('REPO_OWNER')
#     repo_name = os.getenv('REPO_NAME')
#     workflow_id = os.getenv('WORKFLOW_ID')
#     token = os.getenv('TOKEN_GITHUB')
#
#     payload = {
#         "ref": "main",
#     }
#
#     headers = {
#         "Authorization": f"token {token}",
#         "Accept": "application/vnd.github.v3+json"
#     }
#
#     response = requests.post(
#         f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_id}/dispatches',
#         headers=headers,
#         data=json.dumps(payload)
#     )
#
#     if response.status_code == 204:
#         print("Workflow запущен успешно!")
#     else:
#         print(f"Ошибка: {response.status_code} - {response.text}")

# Обработчик команды /reg для запроса имени пользователя
@bot.message_handler(commands=['reg'])
def reg_user(message):
    request_name(message)

# Обработчик нажатия на inline-кнопку для запуска тестов
# @bot.callback_query_handler(func=lambda call: call.data == 'run_tests')
# def run_tests_callback(call):
#     post_run_test()
#     bot.send_message(call.message.chat.id, "Тесты успешно запущены!")
#
# # Запуск бота
# bot.polling()
