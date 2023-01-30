#Import Libraries
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService
    from bs4 import BeautifulSoup
    import time, random, os, csv
    import pandas as pd
    from alive_progress import alive_bar
except ImportError as e:
    print("Unable to import some libraries, please install them first with 'python3 -m pip install -r requirements.txt'\n", e)
    time.sleep(3)
    exit()

# alive progress bar (also for finished product)
# with alive_bar(100, bar="classic") as bar:
#    for i in range(100):
#        time.sleep(0.1)
#        bar()

# set path to chromedriver
# options = webdriver.ChromeOptions() <= for headless (finished product)
# options.add_argument('--headless')  <-------|
def clean_up():
    print("Cleaning up...")
    os.subprosses.call("clear", shell=True)

def grab_login(file):
    with open(file, 'r') as f_reader:
        for login in f_reader:
            login = login.split(":")
            return login

path = os.getcwd() + "/"
# driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) <= for headless (finished product)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# open the webpage
driver.get("https://www.facebook.com/")
time.sleep(2)

# login to facebook
user_details = grab_login(f"{path}info/user.txt")
usern = user_details[0]
passw = user_details[1]

username = driver.find_element_by_id("email")
username.send_keys(usern)
time.sleep(5)
password = driver.find_element_by_id("pass")
time.sleep(5)
password.send_keys(passw)
time.sleep(5)
driver.find_element_by_name("login").click()
time.sleep(5)

# open the facebook page
driver.get("https://www.facebook.com/ExtonRegionChamber/following")
time.sleep(10)


driver.close()
clean_up()