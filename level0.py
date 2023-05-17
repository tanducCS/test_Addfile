import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException


class Utils:
    def login(driver):
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        username.clear()
        username.send_keys("teacher")
        password = driver.find_element(by=By.ID, value="password")
        password.clear()
        password.send_keys("moodle")
        password.send_keys(Keys.RETURN)

class GradeSettingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("./chromedriver"))
        self.driver.maximize_window()
        self.driver.get("https://school.moodledemo.net/course/modedit.php?update=565&return=0&sr=0")
        Utils.login(self.driver)

    def test_1(self):
        try:
            driver = self.driver
        
            # Wait for the element to become visible and enabled
            wait = WebDriverWait(driver, 15)

            
            addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
            addfilebutton.click()

            addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
            addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase\\1.txt")
            
            

            uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
            uploadbutton.click()

            save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton2")))
            save_and_returntocourse.click()

            assert "https://school.moodledemo.net/course/view.php?id=56#section-1" == driver.current_url
            print("Testcase 1 : Passed")
        except:
            print("Testcase 1: Failed")


    def test_2(self):
        try:
            driver = self.driver
        


            # Wait for the element to become visible and enabled
            wait = WebDriverWait(driver, 15)

            
            addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
            addfilebutton.click()

            addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
            addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase\\2.txt")
            
            

            uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
            uploadbutton.click()

            save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton2")))
            save_and_returntocourse.click()

            assert "https://school.moodledemo.net/course/view.php?id=56#section-1" == driver.current_url
            print("Testcase 2: Passed")
        except:
            print("Testcase 2: Failed")
    
    
    def test_3(self):
        try:
            driver = self.driver
        


            # Wait for the element to become visible and enabled
            wait = WebDriverWait(driver, 15)

            
            addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
            addfilebutton.click()

            addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
            addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase\\3.txt")
            
            

            uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
            uploadbutton.click()

            save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton2")))
            save_and_returntocourse.click()

            assert "https://school.moodledemo.net/course/view.php?id=56#section-1" == driver.current_url
            print("Testcase 3: Passed")
        except:
            print("Testcase 3: Failed")
    
    
    def test_4(self):
        try:
            driver = self.driver
        


            # Wait for the element to become visible and enabled
            wait = WebDriverWait(driver, 15)

            
            addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
            addfilebutton.click()

            addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
            addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase\\4.txt")
            
            

            message = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'moodle-exception-message')))

            assert "The file '4.txt' is either empty or a folder. To upload folders zip them first." == message.text
            print("Testcase 4: Passed")
        except:
            print("Testcase 4: Failed")
    
    def test_5(self):
        try:
            driver = self.driver
        


            # Wait for the element to become visible and enabled
            wait = WebDriverWait(driver, 15)

            
            addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
            addfilebutton.click()

            addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
            addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase\\5.txt")
            
            

            uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
            uploadbutton.click()

            save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton2")))
            save_and_returntocourse.click()

            assert "https://school.moodledemo.net/course/view.php?id=56#section-1" == driver.current_url
            print("Testcase 5: Passed")
        except:
            print("Testcase 5: Failed")

    def test_6(self):
        try:
            driver = self.driver
        


            # Wait for the element to become visible and enabled
            wait = WebDriverWait(driver, 15)

            
            addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
            addfilebutton.click()

            addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
            addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase\\6.txt")
            
            

            uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
            uploadbutton.click()

            save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton2")))
            save_and_returntocourse.click()

            assert "https://school.moodledemo.net/course/view.php?id=56#section-1" == driver.current_url
            print("Testcase 6: Passed")
        except:
            print("Testcase 6: Failed")


    def test_7(self):
        try:
            driver = self.driver
        


            # Wait for the element to become visible and enabled
            wait = WebDriverWait(driver, 15)

            
            addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
            addfilebutton.click()

            addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
            addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase\\7.txt")
            
            

            uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
            uploadbutton.click()

            save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton2")))
            save_and_returntocourse.click()

            assert "https://school.moodledemo.net/course/view.php?id=56#section-1" == driver.current_url
            print("Testcase 7: Passed")
        except:
            print("Testcase 7: Failed")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
