import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from graduatework.settings import auth_page_url, driver_path


@pytest.fixture(autouse=True)
def testing_pass_rec():
    """Фикстура заходит в браузер, открывает страницу авторизации, переходит на страницу восстановления пароля,
    ожидает загрузку страницы. После выполнения теста выходит из браузера."""
    pytest.driver = webdriver.Chrome(driver_path)
    # Переход на страницу авторизации.
    pytest.driver.get(auth_page_url)
    # Явное ожидание видимого отображения заголовка формы авторизации.
    element = WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1[@class="card-container__title"]')))
    # Переход на страницу восстановления пароля.
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    # Явное ожидание видимого отображения заголовка формы восстановления пароля.
    element = WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1[@class="card-container__title"]')))
    yield
    pytest.driver.quit()


# Кнопка возврата на страницу авторизации
def test_pass_rec_reset_back():
    """Валидация кнопки возврата на страницу авторизации."""
    pytest.driver.find_element(By.ID, 'reset-back').click()
    # Явное ожидание видимого отображения заголовка формы авторизации.
    element = WebDriverWait(pytest.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//h1[@class="card-container__title"]')))

    # Проверка, что возврат на страницу авторизации осуществился.
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == "Авторизация",\
        'reset back error'
