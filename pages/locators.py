from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_EN_GB = (By.LINK_TEXT, "View basket")
    BASKET_BUTTON_RU = (By.LINK_TEXT, "Посмотреть корзину")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    """Локаторы для кнопки входа в форму регистрации"""
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/"


class LoginPageLocators():
    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    SUBSTRING_LOGIN = "login"
    LOGIN_FORB_TXT = (By.CSS_SELECTOR, "//*[text()='Log In']")  # Текст в форме логина Log In
    LOGIN_FORM = (By.ID, "login_form")  # Форма Log In
    LOGIN_FORM_EMAIL = (By.ID, "#id_login-username")  # Поле ввода эмаил адресса
    LOGIN_FORM_PASSWORD = (By.ID, "#id_login-password")  # Поле ввода пароля
    LOG_IN_BUTTON = (By.NAME, "login_submit")  # Кнопка входа по логину

    REGISTER_FORM = (By.ID, "register_form")  # Форма register
    EMAIL_ADDR_INPUT = (By.ID, "id_registration-email")  # Поле ввода эмаил адресса
    PASSWORD1_INPUT = (By.ID, "id_registration-password1")  # Поле ввода пароля
    PASSWORD2_INPUT = (By.ID, "id_registration-password2")  # Поле потверждения пароля
    REGISTER_BUTTON = (By.NAME, "registration_submit")  # Копка регитсрации


class ProductPageLocators():
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    PRODUCT_PAGE_LINK_1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    PRODUCT_PAGE_LINK_2 = "/?promo=newYear"
    PRODUCT_PAGE_LINK_3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    PRODUCT_PAGE_LINK_promo = PRODUCT_PAGE_LINK_1 + PRODUCT_PAGE_LINK_2  # полная ссылка
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")  # кнопка добавить
    BOOK_TO_COMPARE = (By.CSS_SELECTOR, ".product_main h1")  # название книги
    PRICE_TO_COMPARE = (By.CLASS_NAME, "price_color")  # цена книги
    BOOK_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    PRICE_NUMBER = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")


class CartPageLocators():
    BASKET_EMPTY = (By.ID, "content_inner")
    BASKET_NOT_EMPTY = (By.CLASS_NAME, "basket-title")
    SUBSTRING_BASKET_EN_GB = "Your basket is empty" #"Ваша корзина пуста"
    SUBSTRING_BASKET_RU = "Ваша корзина пуста"
