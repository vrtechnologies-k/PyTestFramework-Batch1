from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryEditBox = (By.ID, 'country')
    countryName = (By.LINK_TEXT, 'India')
    agreeCheckbox = (By.CSS_SELECTOR,"div[class*='checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR,"input[class*='btn-success']")
    sucMessage = (By.CSS_SELECTOR,"div[class*='alert-success']")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.countryEditBox)

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def selectchkbox(self):
        return self.driver.find_element(*ConfirmPage.agreeCheckbox)

    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSucmessage(self):
        return self.driver.find_element(*ConfirmPage.sucMessage)