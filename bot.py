from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

class Bot:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome(executable_path = "./chromedriver.exe")
        self.action = webdriver.ActionChains(self.browser) 
        self.username = username
        self.password = password
        self.post_url = post_url
        self.tags = tag_users
        self.phrases = random_phrases
        self.num_tag = no_of_ppl_to_tag
        self.comments = 0
    
    def connect(self) -> bool:
        self.browser.get("https://www.instagram.com")
        time.sleep(3)

        # accept cookies
        cookies_btn = self.browser.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        cookies_btn.click()
        time.sleep(3)

        # get username and password fields
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys(username)
        password_input.send_keys(password)

        # press login btn
        login_btn = self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        time.sleep(2)
        login_btn.click()
        time.sleep(5)

        return True

    def generateStr(self) -> str:
        # get N number of tags
        tags = []
        while len(tags) < 3:
            selection = random.choice(self.tags)
            if selection not in tags:
                tags.append(selection)
        
        return ' '.join(tags) + ' ' + random.choice(self.phrases)

    def navigate_to_giveaway(self) -> None:
        # navigate to post
        self.browser.get(self.post_url)
        time.sleep(2)
        return

    def comment(self) -> None:
        text_area = self.browser.find_element(By.CLASS_NAME, "Ypffh")
        text_area.click()
        time.sleep(3)
        text_area = self.browser.find_element(By.CLASS_NAME, "Ypffh")
        text_area.send_keys(self.generateStr())
        time.sleep(3)
        comment_btn = self.browser.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]')
        time.sleep(3)
        self.browser.execute_script('arguments[0].click()', comment_btn)
        time.sleep(3)
        return

    def start(self) -> None:
        if self.connect() == True:
            self.navigate_to_giveaway()
            while True:
                self.comment()
                self.comments += 1
                time.sleep(random.randint(20, 40))