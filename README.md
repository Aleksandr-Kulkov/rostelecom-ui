# rostelecom-ui
Skillfactory - Graduatework

Тестирование сайта компании «Ростелеком Информационные Технологии».

Бриф от заказчика: https://lms.skillfactory.ru/assets/courseware/v1/f78e146f0eb3ace247a28b07e66467de/asset-v1:SkillFactory+QAP-3.0+2021+type@asset+block/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_SSO_%D0%B4%D0%BB%D1%8F_%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_last.doc

Тестовая документация: https://docs.google.com/spreadsheets/d/1f1FC1MGe85-yy2FcyRfxySQLAQusoQWKjrSiOZKTCFk/edit?usp=sharing

Тестовое окружение:
1. OS - Windows 10 Pro 22H2
2. Browser - Chrome 117.0.5938.152 (скачан соответствующий chromedriver).
3. IDE - PyCharm
4. Python 3.11

Тестовые сценарии проверяют функциональность элементов страниц авторизации, регистрации и восстановления пароля.

Перед запуском тестов необходимо в файле graduatework/settings.py в переменной driver_path вместо <path_to_driver> указать путь до проекта.

Для запуска тестов необходимо выполнить следующие команды в терминале PyCharm (вместо <path_to_driver> необходимо указать путь до проекта):
1. Страница авторизации: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/graduatework/chromedriver-win64/chromedriver.exe graduatework/tests/test_auth_page.py
2. Страница регистрации: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/graduatework/chromedriver-win64/chromedriver.exe graduatework/tests/test_reg_page.py
3. Страница восстановления пароля: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/graduatework/chromedriver-win64/chromedriver.exe graduatework/tests/test_pass_rec_page.py

При тестировании применены следующие библиотеки:
- pytest - версия 6.2.5
- pytest-selenium - версия 4.0.0
- selenium - версия 4.9.0

При тестировании применен паттерн PageObject.

При тестировании поля "Имя" формы регистрации применены следующие техники тест-дизайна:
1. Классы эквивалентности
2. Граничные значения

Данные техники использованы для оптимизации процесса тестирования поля в соответствии с требованиями.

Требования к длине поля: от 2 до 30 символов.

Значения для тестирования длины поля: 0, 1, 2, 3, 29, 30, 31 символов.
