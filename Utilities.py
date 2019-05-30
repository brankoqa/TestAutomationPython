from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

""""Classes for utilities which can be used on any page"""

class Calculation():

    def calculateCorrectResult(self, expression):
        first = int(expression.split()[0]) # Split the string into the list and get the first element of that list and
                                           # cast it to Integer
        second = int(expression.split()[-1]) # The same as upper row except that is getting the last element of the list
        return first+second # return result of addition

class WaitForElements():

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locator, timeout=10, pollFrequency=0.5): # Method with 3 argument. Two has predefined values
        element = None # Giving the not value to element var since it need to be defined as we are using that var in try/except
        try:
            print("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency) # Instantiating WebDriverWait object
            element = wait.until(EC.visibility_of_element_located(locator)) # passing the locator to method
            print("Element is visible on the web page")
        except:
            print("Element is not visible on the web page")
            print_stack()
        return element



