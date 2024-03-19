import telebot
from telebot import types
import os
from dotenv import load_dotenv
import time
from run_jobs.run_jobs import RunJobs

load_dotenv()


class StartBot(RunJobs):
    def __init__(self):
        self.TOKEN = os.getenv('TOKEN_BOT')
        self.tests_button_clicked = False
        self.bot = telebot.TeleBot(self.TOKEN)
        self.message = "✅ Тесты успешно запущены! Результаты доступны по ссылке" \
                       " <a href='https://vladimirqw1221.github.io/test_ui/'>Allure Report</a>."

    def send_welcome(self, chat_id):
        markup = types.InlineKeyboardMarkup()

        if not self.tests_button_clicked:
            markup.row(types.InlineKeyboardButton('🔥 Запустить тесты 🔥', callback_data='run_tests'))
        else:
            markup.row(types.InlineKeyboardButton('🔥 Тесты уже запущены 🔥', callback_data='tests_already_running'))

        markup.row(types.InlineKeyboardButton('Связь с автором 📧', url='https://t.me/valdimirshe'))
        self.bot.send_message(chat_id, "Добро пожаловать! Нажмите кнопку, чтобы запустить тесты.", reply_markup=markup)

    def get_emoji_animation(self, seconds):
        emojis = ['⏳', '⌛', '⏰', '⏱️', '🕰️']
        index = (seconds // 10) % len(emojis)
        return emojis[index] * (seconds % 10)

    def start_handler(self, message):
        self.send_welcome(message.chat.id)

    def callback_query(self, call):
        if call.data == "run_tests":
            if not self.tests_button_clicked:
                self.tests_button_clicked = True
                message = self.bot.send_message(call.message.chat.id,
                                                "🚀 Тесты запускаются! Пожалуйста, подождите... 🚀")
                self.post_run_test()
                for i in range(3 * 60):
                    self.bot.edit_message_text(chat_id=call.message.chat.id, message_id=message.message_id,
                                               text=f"🕒 Тесты запускаются! Пожалуйста, подождите... 🕒\n{self.get_emoji_animation(i)}")
                    time.sleep(1)
                self.bot.delete_message(call.message.chat.id, message.message_id)
                self.bot.send_message(
                    call.message.chat.id,
                    self.message,
                    parse_mode='HTML'

                )

                self.tests_button_clicked = False
            else:
                self.bot.answer_callback_query(call.id, "Тесты уже были запущены.", show_alert=True)

    def chat_member_handler(self, message):
        if message.new_chat_member.status == 'kicked':
            return
        self.send_welcome(message.chat.id)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def start_handler_wrapper(message):
            self.start_handler(message)

        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query_wrapper(call):
            self.callback_query(call)

        @self.bot.my_chat_member_handler()
        def chat_member_handler_wrapper(message):
            self.chat_member_handler(message)

        self.bot.polling()
