from .base_page import BasePage


""" В нем создайте класс  MainPage. Его нужно сделать наследником класса BasePage. 
Класс-предок в Python указывается в скобках """


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
