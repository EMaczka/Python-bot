from selenium import webdriver
import time
import random
from login_data import email, password

class Swiper():
    def __init__(self):
        self.web = webdriver.Chrome()

    def login(self):
        self.web.get('https://tinder.com')
        time.sleep(3)

        #login via fb auth

        buttonFacebook = self.web.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        buttonFacebook.click()

        windowMain = self.web.windowHandle[0]
        self.web = windowSwitch(self.web.windowHandle[1])

        fieldEmail = self.web.find_element_by_xpath('//*[@id="email"]')
        fieldEmail.send_keys(email)

        fieldPassword = self.web.find_element_by_xpath('//*[@id="pass"]')
        fieldPassword.send_keys(password)

        buttonLogin = self.web.find_element_by_xpath('//*[@id="u_0_0"]')
        buttonLogin.click()

        self.web.windowSwich(windowMain)

        #pop up windows handling

        popupLocation = self.web.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popupLocation.click()

        popupNotification = self.web.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popupNotification.click()

    def closePopup1(self):
        popupHomescreen = self.web.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popupHomescreen.click()

    def closePopup2(self):
        popupMatch = self.web.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        popupMatch.click()

    #account swiping 

    def swipeRight(self):
        buttonRight = self.web.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        buttonRight.click()

    def loopSwipe(self):
        while True:
            sleep(random.randint(1,3))
            try:
                self.swipeRight()
            except Exception as error:
                try:
                    self.closePopup1()
                except Exception:
                    self.closePopup2()

bot = Swiper()
bot.login()        

        




