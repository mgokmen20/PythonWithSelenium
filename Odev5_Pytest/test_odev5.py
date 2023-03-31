from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # sleep uygulamasi yerine kullanilacak modül
from selenium.webdriver.support import expected_conditions as ec #ilgili bekleme isleminin sartini belirlemek icin kullanilir.
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date




class Test_Sauce:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) 
    
    def teardown_method(self):
        self.driver.quit()

    def test_empty_all(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")))
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_all.png") 
        assert errorMessage.text == "Epic sadface: Username is required"
    
    def test_empty_pass(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_pass.png") 
        assert errorMessage.text == "Epic sadface: Password is required"


    def test_locked_user(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce") 
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_locked_user.png") 
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_empty_caution(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"error-button")))
        hataikon = self.driver.find_element(By.CLASS_NAME,"error-button")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_caution.png") 
        hataikon.click()


    def test_standart(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/test_standart.png")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    def test_product(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        numberOfProducts = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test_product.png")
        assert len(numberOfProducts) == 6

    @pytest.mark.parametrize("ad,soyad,postcode",[("Mehmet","Gökmen","12345"),("ömer","Turan","54321"),("Ali","yildiz","98765")])
    def test_checkout_success(self,ad,soyad,postcode):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        urunBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        urunBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"shopping_cart_container")))
        sepetBtn = self.driver.find_element(By.ID,"shopping_cart_container")
        sepetBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutBtn = self.driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        adi = self.driver.find_element(By.ID,"first-name")
        soyadi = self.driver.find_element(By.ID,"last-name")
        postaKodu = self.driver.find_element(By.ID,"postal-code")
        devamBtn = self.driver.find_element(By.ID,"continue")
        adi.send_keys(ad)
        soyadi.send_keys(soyad)
        postaKodu.send_keys(postcode)
        devamBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_checkout.png")
        assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    
    @pytest.mark.parametrize("ad,soyad,postcode",[("","Gökmen","12345"),("","Turan","54321"),("","yildiz","98765")])
    def test_checkout_empty_name(self,ad,soyad,postcode):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        kullaniciAdi = self.driver.find_element(By.NAME,"user-name")
        sifre = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        kullaniciAdi.send_keys("standard_user")
        sifre.send_keys("secret_sauce")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        urunBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        urunBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"shopping_cart_container")))
        sepetBtn = self.driver.find_element(By.ID,"shopping_cart_container")
        sepetBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        cikisBtn = self.driver.find_element(By.ID,"checkout")
        cikisBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        adi = self.driver.find_element(By.ID,"first-name")
        soyadi = self.driver.find_element(By.ID,"last-name")
        postaKodu = self.driver.find_element(By.ID,"postal-code")
        devamBtn = self.driver.find_element(By.ID,"continue")
        adi.send_keys(ad)
        soyadi.send_keys(soyad)
        postaKodu.send_keys(postcode)
        devamBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_checkout_empty_name.png")
        assert errorMessage.text == "Error: First Name is required"

    @pytest.mark.parametrize("ad,soyad,postcode",[("Mehmet","","12345"),("ömer","","54321"),("Ali","","98765")])
    def test_checkout_empty_lastName(self,ad,soyad,postcode):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.NAME,"user-name")
        password = self.driver.find_element(By.NAME,"password")
        loginBtn = self.driver.find_element(By.NAME,"login-button")
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        loginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        urunBtn = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        urunBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"shopping_cart_container")))
        sepetBtn = self.driver.find_element(By.ID,"shopping_cart_container")
        sepetBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"checkout")))
        cikisBtn = self.driver.find_element(By.ID,"checkout")
        cikisBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))
        adi = self.driver.find_element(By.ID,"first-name")
        soyadi = self.driver.find_element(By.ID,"last-name")
        postaKodu = self.driver.find_element(By.ID,"postal-code")
        devamBtn = self.driver.find_element(By.ID,"continue")
        adi.send_keys(ad)
        soyadi.send_keys(soyad)
        postaKodu.send_keys(postcode)
        devamBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_checkout_empty_lastName.png")
        assert errorMessage.text == "Error: Last Name is required"

