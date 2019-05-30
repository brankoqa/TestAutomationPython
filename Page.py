from selenium.webdriver.common.by import By

"""All web elements located on the page fill-out-form with locators and methods"""

class FillOutFormPage(object):

#Element locators:
    NAME_TEXT_FIELD = "et_pb_contact_name_1"
    MESSAGE_TEXT_FIELD = "et_pb_contact_message_1"
    SUM_EXPRESSION_FIELD = "et_pb_contact_captcha_question"
    SUBMIT_BUTTON = "//div [@class = 'et_pb_column et_pb_column_1_2 et_pb_column_1    et_pb_css_mix_blend_mode_passthrough']//button"
    RESULT_FIELD = "et_pb_contact_captcha_1"
    SUCCESS_ERROR_FIELD = "//div[@id = 'et_pb_contact_form_1']//div[@class = 'et-pb-contact-message']"
    SUCCESS_ERROR_FIELD_BY_XPATH = By.XPATH, "//div[@id = 'et_pb_contact_form_1']//div[@class = 'et-pb-contact-message']"

#Constructor:
    def __init__(self, driver):
        self.driver = driver

#Get the web elements:
    def getNameField(self):
        return self.driver.find_element(By.ID, self.NAME_TEXT_FIELD)

    def getMessageField(self):
        return self.driver.find_element(By.ID, self.MESSAGE_TEXT_FIELD)

    def getTheResultField(self):
        return self.driver.find_element(By.NAME, self.RESULT_FIELD)

    def getSubmitButton(self):
        return self.driver.find_element(By.XPATH, self.SUBMIT_BUTTON)

    def getTheSumExpresionElement(self):
        return self.driver.find_element(By.CLASS_NAME, self.SUM_EXPRESSION_FIELD)

    def getSuccessErrorDiv(self):
        return self.driver.find_element(By.XPATH, self.SUCCESS_ERROR_FIELD)

#Actions on the web elements:
    def fillNameField(self, name="Test name"):
        self.getNameField().send_keys(name)


    def fillMessageField(self, message="Test message"):
        self.getMessageField().send_keys(message)

    def fillResultField(self, result):
        self.getTheResultField().send_keys(result)

    def clickOnSubmitButton(self):
        self.getSubmitButton().click()

    def getSucessErrorMsgText(self):
        return self.getSuccessErrorDiv().text

    def getSumExpressionText(self):
        return self.getTheSumExpresionElement().text


