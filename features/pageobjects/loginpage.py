import time

from selenium import webdriver
from features.pageobjects.Base import BaseSettingsPage
from Utilities.configreader import ConfigReader
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class flipkart(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)

    def fliphome(self):
        self.driver.get(ConfigReader("base info","URL"))

    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("closeloginwindow_XPATH")
        time.sleep(5)

    def clickloginLink(self):
        e = self.driver.find_element(By.CSS_SELECTOR,"#container>div>div._1kfTjk>div._1rH5Jn>div._2Xfa2_>div.go_DOp._2errNR>div>div>div>a")
        a = ActionChains(self.driver)
        a.move_to_element(e)
        a.perform()
        time.sleep(5)

    def clickSignUpLink(self):
        self.driver.find_element(By.CSS_SELECTOR,"#container>div>div._1kfTjk>div._1rH5Jn>div._2Xfa2_>div.go_DOp._2errNR>div>div>div.ZEl_b_._1J9ow0._2ogGYG._23xUYh._3pAV4E>div._3_Fivj>div>div>div>div._3wJI0x").click()

    def validateText(self,expectedText):
        self.AssertText("NewUserText_XPATH",expectedText)

    def entermob(self,number):
        self.TypeEditBox("RegMobileNo_XPATH",number)
        time.sleep(40)
    def continuebutton(self):
        self.ClickButton("continuebutton_XPATH")
        time.sleep(10)

    def enterpass(self,password):
        self.TypeEditBox("password_XPATH",password)

    def clickSignUpbutton(self):
        self.ClickButton("SignUpbutton_XPATH")

