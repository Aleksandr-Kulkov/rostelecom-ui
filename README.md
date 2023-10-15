# graduatework
Skillfactory - Graduatework

Тестирование сайта компании «Ростелеком Информационные Технологии».
Тестовые сценарии проверяют функциональность элементов страниц авторизации, регистрации и восстановления пароля.

Для запуска тестов необходимо выполнить следующие команды в терминале PyCharm (вместо <path_to_driver> необходимо указать путь до проекта):

python -m pytest -v --driver Chrome --driver-path <path_to_driver>/graduatework/chromedriver-win64/chromedriver.exe graduatework/tests/test_auth_page.py

python -m pytest -v --driver Chrome --driver-path <path_to_driver>/graduatework/chromedriver-win64/chromedriver.exe graduatework/tests/test_reg_page.py

python -m pytest -v --driver Chrome --driver-path <path_to_driver>/graduatework/chromedriver-win64/chromedriver.exe graduatework/tests/test_pass_rec_page.py

При тестировании применены следующие библиотеки:
pytest - версия 6.2.5
pytest-selenium - версия 4.0.0
selenium - версия 4.9.0

При тестировании применен паттерн PageObject.

При тестировании поля "Имя" формы регистрации применены следующие техники тест-дизайна:
1. Классы эквивалентности
2. Граничные значения
Данные техники использованы для оптимизации процесса тестирования поля в соответствии с требованиями.
Требования к длине поля: от 2 до 30 символов.
Значения для тестирования длины поля: 0, 1, 2, 3, 29, 30, 31 символов.
