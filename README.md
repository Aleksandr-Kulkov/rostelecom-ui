# rostelecom-ui

UI-тестирование сайта компании «Ростелеком Информационные Технологии».

Тестовая документация: https://docs.google.com/spreadsheets/d/1f1FC1MGe85-yy2FcyRfxySQLAQusoQWKjrSiOZKTCFk/edit?usp=sharing

Тестовое окружение:
1. OS - Windows 10 Pro 22H2
2. Browser - Chrome 130.0.6723.71 (скачан соответствующий chromedriver).
3. IDE - PyCharm
4. Python 3.13.0

Тестовые сценарии проверяют функциональность элементов страниц авторизации, регистрации и восстановления пароля.

Перед запуском тестов необходимо:
- скачать архив с файлом chromedriver в соответствии с версией браузера Chrome по ссылке https://developer.chrome.com/docs/chromedriver/downloads?hl=ru, разархивировать архив, переместить папку с файлом chromedriver в папку проекта;
- в файле settings.py в переменной driver_path вместо <path_to_driver> указать путь до проекта.

Команды для запуска тестов в терминале PyCharm (вместо <path_to_driver> необходимо указать путь до проекта):
1. Страница авторизации: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/rostelecom-ui/chromedriver-win64/chromedriver.exe tests/test_auth_page.py
2. Страница регистрации: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/rostelecom-ui/chromedriver-win64/chromedriver.exe tests/test_reg_page.py
3. Страница восстановления пароля: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/rostelecom-ui/chromedriver-win64/chromedriver.exe tests/test_pass_rec_page.py

При тестировании применены следующие библиотеки:
- pytest - версия 8.3.3
- pytest-selenium - версия 4.1.0
- selenium - версия 4.26.0

При тестировании применен паттерн PageObject.

При тестировании поля "Имя" формы регистрации применены следующие техники тест-дизайна:
1. Классы эквивалентности
2. Граничные значения

Данные техники использованы для оптимизации процесса тестирования поля в соответствии с требованиями.

Требования к длине поля: от 2 до 30 символов.

Значения для тестирования длины поля: 0, 1, 2, 3, 29, 30, 31 символов.
