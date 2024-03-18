import requests
import json
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN_BOT')
bot = telebot.TeleBot(TOKEN)

repo_owner = os.getenv('REPO_OWER')
repo_name = os.getenv('REPO_NAME')
workflow_id = os.getenv('WORKWLOF_ID')

def post_run_test():
    token = os.getenv('TOKEN_GITHUB')

    payload = {
        "ref": "main",
    }

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.post(
        f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_id}/dispatches',
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 204:
        print("Workflow запущен успешно!")
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")

def send_welcome(chat_id):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Запустить тесты', callback_data='run_tests'))
    bot.send_message(chat_id, "Добро пожаловать! Нажмите кнопку, чтобы запустить тесты.", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_handler(message):
    send_welcome(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "run_tests":
        post_run_test()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Тесты успешно запущены!")

@bot.my_chat_member_handler()
def chat_member_handler(message):
    if message.new_chat_member.status == 'kicked':
        return
    send_welcome(message.chat.id)

bot.polling()