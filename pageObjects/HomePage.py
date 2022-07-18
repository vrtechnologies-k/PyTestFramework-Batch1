from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import Checkoutpage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, 'Shop')

    def shopItem(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutPage = Checkoutpage(self.driver)
        return checkoutPage
