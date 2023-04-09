from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import openpyxl



class Test_Sauce:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    def teardown_method(self):
        self.driver.quit()


    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    # Basarili bir giris yaparak, bir ürün satin alip sonrada teslimat adresini girerek basarili bir alisveris yaparak sayfadan logout islemi yaptim.
    def test_shopping(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        paswordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        paswordInput.send_keys("secret_sauce")        
        self.waitForElementVisible((By.ID,"login-button"))
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-backpack"))
        addProduct = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addProduct.click()
        self.waitForElementVisible((By.CLASS_NAME,"shopping_cart_link"))
        cartButton = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cartButton.click()
        self.waitForElementVisible((By.CLASS_NAME,"cart_item"))
        cartList = self.driver.find_elements(By.CLASS_NAME,"cart_item")
        print(f"sepetinizde suan - {len(cartList)} - adet ürün bulunmakta")
        checkOut = self.driver.find_element(By.ID,"checkout")
        checkOut.click()
        self.waitForElementVisible((By.ID,"first-name"))
        firstName = self.driver.find_element(By.ID,"first-name")
        firstName.send_keys("Mehmet")
        self.waitForElementVisible((By.ID,"last-name"))
        lastName = self.driver.find_element(By.ID,"last-name")
        lastName.send_keys("Gökmen")
        self.waitForElementVisible((By.ID,"postal-code"))
        zipCode = self.driver.find_element(By.ID,"postal-code")
        zipCode.send_keys("3552")
        self.waitForElementVisible((By.ID,"continue"))
        continueButton= self.driver.find_element(By.ID,"continue")
        continueButton.click()
        self.waitForElementVisible((By.ID,"finish"))
        finishButton = self.driver.find_element(By.ID,"finish")
        finishButton.click()
        DeliveryMessage = self.driver.find_element(By.CLASS_NAME,"complete-text")
        assert DeliveryMessage.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        self.waitForElementVisible((By.ID,"back-to-products"))
        backHomeButton = self.driver.find_element(By.ID,"back-to-products")
        backHomeButton.click()
        self.waitForElementVisible((By.ID,"react-burger-menu-btn"))
        burgerMenu = self.driver.find_element(By.ID,"react-burger-menu-btn")
        burgerMenu.click()
        self.waitForElementVisible((By.ID,"logout_sidebar_link"))
        logOut = self.driver.find_element(By.ID,"logout_sidebar_link")
        logOut.click()
        







