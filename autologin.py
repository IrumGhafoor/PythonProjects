from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def startBot(username, password, url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    wait = WebDriverWait(driver, 15)

    driver.get(url)

    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(username)
    driver.find_element(By.NAME, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()

    # 👇 IMPORTANT: wait for homepage fully
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    print("Still running...")

    # 👇 Keep browser open to observe
    input("Press Enter to close...")

username = "irumghafoor852@gmail.com"
password = "Irum@Multan1234"
url = "https://www.facebook.com/"

startBot(username, password, url)