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

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
path = os.getcwd() + "/"

def grab_login(file):
    with open(file, 'r') as f_reader:
        for login in f_reader:
            login = login.split(":")
            return login

def login(target_website):
    driver.get(target_website + "/login")
    user_details = grab_login(f"{path}info/user.txt")
    usern = user_details[0]
    passw = user_details[1]

    username = driver.find_element_by_id("email")
    username.send_keys(usern)
    time.sleep(2.5)
    password = driver.find_element_by_id("pass")
    time.sleep(3.5)
    password.send_keys(passw)
    time.sleep(2.5)
    driver.find_element_by_name("login").click()
    time.sleep(2.5)

def clean_up():
    print("Cleaning up...")
    driver.close()
    os.subprosses.call("clear", shell=True)

def doScrape_Following():
    following = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for link in soup.find_all('', role='link'): # <== when not on school wifi add class names for soup
        following.append(link.get('href')) # think about checking this up.. dont look right
    return following


# run while alive
if __name__ == "__main__":
    # init variables
    target_profile = ""
    target_website = ""
    target_endpoint = ""
    target_url = ""

    # start the program
    target_profile = input("Enter the profile you want to scrape (i.e. /Mwing10/ [yes with slashes]): ")
    target_website = input("Enter the website you want to scrape (i.e. https://facebook.com): ")
    target_endpoint = input("Enter the endpoint you want to scrape (i.e. following): ")
    target_url = target_website + target_profile + target_endpoint

with alive_bar(100, dual_line=True, bar="classic") as bar:
    for i in range(15):
        bar.text("Target Aquired: %s" % target_url) # initialize the program
    for i in range (15):
        grab_login(f"{path}info/user.txt") # grab the login details
        time.sleep(2)
        bar.text("Finishing up login...")
        login(target_website) # login to facebook
        time.sleep(1.5)
    for i in range(15):
        bar()
    clean_up() # clean up the terminal