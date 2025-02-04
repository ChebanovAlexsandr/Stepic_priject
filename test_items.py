import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
button = "#add_to_basket_form"


class TestProductPage:

    def test_button_add_to_basket_is_visible(self, browser):
        """Тест проверяет, что страница товара
         содержит кнопку добавления в корзину
        """
        # Открываем страницу товара
        browser.get(link)
        browser.implicitly_wait(10)
        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(5)

        # Проверяем наличие кнопки добавления товара в корзину
        if 'fr' in browser.current_url:
            time.sleep(10)
            # Проверка на надпись
            assert browser.find_element(By.CSS_SELECTOR, button).text == "Ajouter au panier"
        elif 'en' in link:
            # Проверка на присутствие элемета
            assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, button)))
