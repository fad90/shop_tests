from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")
    PRODUCT_PRICE = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    ADDED_TO_BASKET_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    PRICE_OF_BASKET_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
