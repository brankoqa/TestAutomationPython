from selenium import webdriver
from Page import FillOutFormPage
import unittest
from Utilities import *
from selenium.webdriver.common.by import By


"""This class consist of tests. It inherits unittest.TestCase class. Also consist setUp and tearDown methods which are 
used to set up test with necessarily preconditions which will be executed before each test and to set up conditions 
which will be executed after each test"""

class AutomationTests(unittest.TestCase):


    @classmethod
    def setUp(self):
        self.baseUrl = "https://www.ultimateqa.com/filling-out-forms/" # Storing the URL into var
        self.chromeDriverPath = "C:\\chromedriver_win32\\chromedriver.exe" # Storing the path to chrome driver into var
        self.driver = webdriver.Chrome(executable_path= self.chromeDriverPath) # Initialize webdriver object and staring the browser
        self.driver.maximize_window() # Maximizing the window after launching the Chrome browser
        self.driver.implicitly_wait(5) # Setting implicitly wait to 5 sec
        self.driver.get(self.baseUrl) # Going to the desirable URL
        self.form = FillOutFormPage(self.driver) # Initialize FillOutFormPage object


    def tearDown(self):
        self.driver.quit()


    """This test will fill out form but in the 'Result' field will pass negative 1 which will result in the error msg. 
    At the end it verifies that sum expression before clicking on the 'Submit' button is different that sum expression 
    after clicking on the 'Submit button'"""

    def test_verifySumExpressionsAreNotEqual(self):

        print("*********Running test Verify Sum Expressions Are Not Equal: \n")
        self.form.fillNameField() # Filling the Name field with "Text name"
        self.form.fillMessageField() # Filling the Message field with "Text message"
        sumExpressionBeforeSubmit = self.form.getSumExpressionText() # Getting the sum expression text
        print("Sum expression before submit is "+ "'" + sumExpressionBeforeSubmit + "'") # Printing the sum expression text into console
        self.form.fillResultField(-1) # Filling the Result field with negative 1
        self.form.clickOnSubmitButton() #Clicking on the Submit button
        sumExpressionAfterSubmit = self.form.getSumExpressionText() # Getting the sum expression text after Submit
        print("Sum expression after submit is "+ "'" + sumExpressionAfterSubmit + "'") # Printing the sum expression text into console after submit
        assert sumExpressionBeforeSubmit != sumExpressionAfterSubmit # Verification (If stings are't equal assert return True)
        if sumExpressionBeforeSubmit != sumExpressionAfterSubmit: # Verification (same as assert) => OVDE TREBA IZBACITI JEDNU VERIFIKACIJU
            print("Expessions are DIFERENT")
        else:
            print("Expressions are the SAME")


    """This test will fill out form and it will fill out correct 'Result' which will result showing the success msg to
     the user. At the end it verifies that success msg is equal to 'Success'"""

    def test_verifySuccessMsg(self):

        print("*********Running test Verify Success Msg: \n")
        self.form.fillNameField() # Filling the Name field with "Text name"
        self.form.fillMessageField() # Filling the Message field with "Message name"
        sumExpressonString = self.form.getSumExpressionText() # Getting the sum expression text
        print("Sum expression before submit is "+ "'" + sumExpressonString + "'") # Printing the sum expression text into console
        add = Calculation() # Initialize Calculation object
        correctResult = add.calculateCorrectResult(sumExpressonString) # Passing string sumExpressionString to the
                                                                       # method which will calculate correct result
        print("Correct result is "+ str(correctResult)) # Casting the number correctResult into string and printing it
        self.form.fillResultField(correctResult) # Filling the Result field with correct result
        self.form.clickOnSubmitButton() # Clicking on the Submit button
        wait = WaitForElements(self.driver) # Initialize WaitForElements object
        wait.waitForElement(self.form.SUCCESS_ERROR_FIELD_BY_XPATH) # Passing the element locator to method to wait that element
        print("Success msg is "+ "'"+ self.form.getSucessErrorMsgText()+"'") # Getting the success message and printing it
        assert self.form.getSucessErrorMsgText() == "Success" # Verifying that success msg is "Success"


if __name__ == '__main__':
    unittest.main(verbosity=2)
