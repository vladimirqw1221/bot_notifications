import os

import telebot
from telebot import types
import time
from run_jobs.run_jobs import RunJobs
from table_user.database import DataBase
from global_enum.hellper_enum import HelpEnum
from dotenv import load_dotenv


load_dotenv()
class StartBot(RunJobs):

    def __init__(self):
        self.TOKEN = os.getenv('TOKEN_BOT')
        self.tests_button_clicked = False
        self.bot = telebot.TeleBot(self.TOKEN)
        self.admins = DataBase()


    def request_name(self, message):
        self.bot.send_message(message.chat.id, "🔒Пожалуйста, введите  пароль:🔒")
        self.bot.register_next_step_handler(message, self.check_user)

    def check_user(self, message):
        user_name = message.text.strip().lower()
        user = self.admins.check_user(user_name)  # Проверяем наличие пользователя в базе данных
        if user:
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='🔥Запустить тесты 🔥', callback_data='run_tests'))
            self.bot.send_message(message.chat.id, "Для запуска тестов нажмите кнопку ниже.", reply_markup=markup)
        else:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('Связь с автором 📧', url='https://t.me/valdimirshe'))
            self.bot.send_message(message.chat.id,
                                  "У вас нет прав доступа на запуск тестов. Обратитесь к администратору.",
                                  reply_markup=markup)

    def get_emoji_animation(self, seconds):
        emojis = ['⏳', '⌛', '⏰', '⏱️', '🕰️']
        index = (seconds // 10) % len(emojis)
        return emojis[index] * (seconds % 10)

    def start_handler(self, message):
        self.request_name(message)

    def callback_query(self, call):
        if call.data == "run_tests":
            if not self.tests_button_clicked:
                self.tests_button_clicked = True
                message = self.bot.send_message(call.message.chat.id, HelpEnum.START_TEST_AMIMATION.value)
                self.post_run_test()
                for i in range(3 * 60):
                    self.bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=message.message_id,
                        text=HelpEnum.START_TEST_ANIMATION_NEW.value + "\n" + self.get_emoji_animation(i)
                    )
                    time.sleep(1)
                self.bot.delete_message(call.message.chat.id, message.message_id)
                self.bot.send_message(
                    call.message.chat.id,
                    HelpEnum.MESSAGE.value,
                    parse_mode='HTML'
                )
                self.tests_button_clicked = False
            else:
                self.bot.answer_callback_query(call.id, "🔥Тесты уже были запущены.🔥", show_alert=True)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def start_handler_wrapper(message):
            self.start_handler(message)

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query_wrapper(call):
            self.callback_query(call)

        self.bot.polling()
