from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def scroll_down(driver):
    """A method for scrolling the page."""
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height


def create_driver():
    username = input("Enter a Quora Username : ")
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get("https://www.quora.com/profile/" + username + "/answers")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class=\"q-box qu-borderBottom\"]")))
    return driver


def load_content(driver):
    # for x in range(5):
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     time.sleep(2)
    scroll_down(driver)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(10)


def create_dataset(driver):
    f = open("dataset.txt", "w")
    f.close()
    f = open("dataset.txt", "a")
    buttons = driver.find_elements_by_class_name("q-absolute")
    for button in buttons:
        button.click()
        time.sleep(1)

    answers = driver.find_elements_by_xpath("//*[@class=\'q-relative spacing_log_answer_content\']")
    for answer in answers:
        f.write(answer.text + "\n\n")
        print(answer.text, "\n\n")
    f.close()
