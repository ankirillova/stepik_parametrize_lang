import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_alien_answer(browser):
    browser.get(link)
    basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert len(basket_button) != 0, "Кнопки В корзину нет на странице"
