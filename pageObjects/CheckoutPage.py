from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class Checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.CSS_SELECTOR, '.card-title a')
    cartFooter = (By.CSS_SELECTOR, '.card-footer button')
    checkoutButton = (By.XPATH, '//a[contains(@class,"btn-primary")]')
    buttonSuccess = (By.CSS_SELECTOR, 'button[class*="btn-success"]')

    def getCardTitles(self):
        return self.driver.find_elements(*Checkoutpage.cardTitles)

    def getCardFooter(self):
        return self.driver.find_elements(*Checkoutpage.cartFooter)

    def clickcheckout(self):
        return self.driver.find_element(*Checkoutpage.checkoutButton)

    def getbuttonsuccess(self):
        self.driver.find_element(*Checkoutpage.buttonSuccess).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
