import time
import yaml
import random
from selenium import webdriver
from utils import extract_clean_text
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def main():
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
    
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://nitrotype.com/")

    log_in_button = driver.find_element(By.XPATH, "/html/body/div/div/header/div/div/a[3]")
    log_in_button.click()

    username_field = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
    username_field.send_keys(config.get("username", "username"))

    password_field = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
    password_field.send_keys(config.get("password", "password"))

    sign_in_confirm_button = driver.find_element(By.XPATH,  "/html/body/div/div/div/main/div/section/div[2]/div/div[3]/form/button")
    sign_in_confirm_button.click()

    race_now_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[1]/div[3]/div[2]/div[3]/div[1]/a")
    race_now_button.click()

    while True:
        words_to_type_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section/div/div[3]/div[1]/div[1]/div[2]/div[1]")
        words_to_type_clean = extract_clean_text(words_to_type_element.get_attribute("outerHTML"))
        print("Now typing: " + words_to_type_clean + "\n")
        
        actions = ActionChains(driver)

        for char in words_to_type_clean:
            actions.send_keys(char).perform()
            time.sleep(random.uniform(0.01, 0.2))

        time.sleep(5)
        race_again_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section/div/div[1]/div[2]/div[4]/div/div[2]/div/button")
        race_again_element.click()

if __name__ == "__main__":
    main()