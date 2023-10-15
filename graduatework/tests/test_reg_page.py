import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from graduatework.settings import auth_page_url, driver_path, empty, msg_reg_first_name, msg_reg_last_name,\
    msg_username, msg_pass, msg_pass_confirm, cyrillic_2, email, password, cyrillic_1, cyrillic_31, space,\
    spaces_group, spaces_in_cyrillic, latin, numbers, symbols, password_2, msg_pass_mismatch


@pytest.fixture(autouse=True)
def testing_reg():
    """Фикстура заходит в браузер, открывает страницу авторизации, переходит на страницу регистрации,
    ожидает загрузку страницы. После выполнения теста выходит из браузера."""
    pytest.driver = webdriver.Chrome(driver_path)
    # Переход на страницу авторизации.
    pytest.driver.get(auth_page_url)
    # Явное ожидание видимого отображения заголовка формы авторизации.
    element = WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1[@class="card-container__title"]')))
    # Переход на страницу регистрации.
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Явное ожидание видимого отображения заголовка формы регистрации.
    element = WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1[@class="card-container__title"]')))
    yield
    pytest.driver.quit()


def test_reg_with_empty_fields():
    """Валидация отправки пустой формы регистрации."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(empty)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(empty)
    pytest.driver.find_element(By.ID, 'address').send_keys(empty)
    pytest.driver.find_element(By.ID, 'password').send_keys(empty)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(empty)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[2]/span').text == msg_reg_last_name,\
        'msg reg last name error'
    assert pytest.driver.find_element(By.XPATH, '//*[@class="register-form__address"]/div/span').text == msg_username,\
        'msg username error'
    assert pytest.driver.find_element(By.XPATH, '//*[@class="new-password-container"]/div[1]/span').text == msg_pass,\
        'msg pass error'
    assert pytest.driver.find_element(By.XPATH, '//*[@class="new-password-container"]/div[2]/span').text == \
           msg_pass_confirm, 'msg pass confirm error'


# Поле "Имя"
def test_reg_with_empty_first_name():
    """Валидация поля "Имя" с пустым значением."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(empty)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_cyrillic_1_first_name():
    """Валидация поля "Имя" с 1 символом (кириллица)."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(cyrillic_1)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_cyrillic_31_first_name():
    """Валидация поля "Имя" с 31 символом (кириллица и '-')."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(cyrillic_31)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_space_first_name():
    """Валидация поля "Имя" с пробелом."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(space)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_spaces_group_first_name():
    """Валидация поля "Имя" с группой пробелов."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(spaces_group)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_spaces_in_cyrillic_first_name():
    """Валидация поля "Имя" с пробелами в значении (кириллица)."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(spaces_in_cyrillic)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_latin_first_name():
    """Валидация поля "Имя" с латиницей."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(latin)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_numbers_first_name():
    """Валидация поля "Имя" с числами."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(numbers)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


def test_reg_with_symbols_first_name():
    """Валидация поля "Имя" со спецсимволами."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(symbols)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="name-container"]/div[1]/span').text == msg_reg_first_name,\
        'msg reg first name error'


# Поле "Подтверждение пароля"
def test_reg_with_unvalid_password_confirm():
    """Валидация поля "Подтверждение пароля" с password_confirm, отличным от password."""
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(cyrillic_2)
    pytest.driver.find_element(By.ID, 'address').send_keys(email)
    pytest.driver.find_element(By.ID, 'password').send_keys(password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(password_2)
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    # Проверка, что регистрация не осуществилась.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Регистрация",\
        'reg error'
    # Проверка сообщений.
    assert pytest.driver.find_element(By.XPATH, '//*[@class="rt-input-container__meta rt-input-container__meta--error"]'
                                                '').text == msg_pass_mismatch, 'msg pass mismatch error'
