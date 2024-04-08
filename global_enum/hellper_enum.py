from enum import Enum


class HelpEnum(str, Enum):
    MESSAGE: str = "✅ Тесты успешно запущены! Результаты доступны по ссылке" \
                   " <a href='https://vladimirqw1221.github.io/test_ui/'>Allure Report</a>."
    WELCOME_BOT: str = "Добро пожаловать! Нажмите кнопку, чтобы запустить тесты."
    START_TEST_AMIMATION: str = "🚀 Тесты запускаются! Пожалуйста, подождите... 🚀"
    START_TEST_ANIMATION_NEW: str = "🕒 Тесты запускаются! Пожалуйста, подождите... 🕒"
    MESSAGE_API: str = "✅ Тесты успешно запущены! Результаты доступны по ссылке" \
                   " <a href='https://vladimirqw1221.github.io/api_test/'>Allure Report</a>."
