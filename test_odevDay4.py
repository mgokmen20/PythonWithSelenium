from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By




class Test_Sauce:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        sleep(5)

    def input_kontrol(self):   # Kullanıcı adı ve şifre alanları boş geçildiğinde 
        
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(5)
        errorMessage =self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Test Sonucu : {testResult} Hata Aciklamasi {errorMessage.text}")
        
        

    def password_conrol(self): # Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak

        usernameInput = self.driver.find_element(By.ID,"user-name")
        paswordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("a")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(5)
        errorMessage =self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu : {testResult} Hata Aciklamasi {errorMessage.text}")

        sleep(2)
        

    def lockedUser_control(self): # Bloklanmis kullanici girisi yapildiginda
        usernameInput = self.driver.find_element(By.ID,"user-name")
        paswordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        paswordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(5)
        errorMessage =self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu : {testResult} Hata Aciklamasi {errorMessage.text}")

        sleep(2)
        

    def redAlertButton(self): # Hata uyarilarini kapatmak icin
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        close_btn = self.driver.find_element(By.XPATH, "//button[@class='error-button']")
        close_btn.click()
        red_x_icons = self.driver.find_elements(By.XPATH, "//div[@class='input-error form_group']/svg[@class='svg-inline--fa fa-exclamation-circle fa-w-16']")
        assert len(red_x_icons) == 0
        sleep(3)
        


    def acceptedUser(self): # Kullanici adi ve sifrenin dogru girilerek sitedeki ürünlerin sayilmasi
        usernameInput = self.driver.find_element(By.ID,"user-name")
        paswordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        paswordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(3)
        productList=self.driver.find_elements(By.CLASS_NAME,"inventory_item_description")  
        print(f"Sitede suan - {len(productList)} - adet ürün var")
        



test=Test_Sauce()  

# test.input_kontrol()
# test.password_conrol()
# test.lockedUser_control()
# test.redAlertButton()
test.acceptedUser()








