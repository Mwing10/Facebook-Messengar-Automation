from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time, csv, os

options = webdriver.ChromeOptions() 
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
path = os.getcwd() + "/"
bad_links = ["videos", "login", "photos", "login/", "photos/", "videos/", "login?next", "photos?tab", "videos?tab", "login?next=", "photos?tab=", "videos?tab=", "reg/", "reg", "?rs=7", "recover/", "photo/", "/login/", "/recover/", "/photo/"]

driver.get("https://www.facebook.com/ExtonRegionChamber/following")
time.sleep(3)

links = []

i = 0
while i < 30:
    i+=1
    time.sleep(1)
    page = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elems = driver.find_elements_by_xpath("//a[@href]") 
    
def do_ScrapFollowing():
    for elem in elems:
        if elem.get_attribute("href").startswith("https://www.facebook.com/"):
            if elem.get_attribute("href") != bad_links:
                links.append(elem.get_attribute("href"))
                print(elem.get_attribute("href"))
            else: 
                print("Not a facebook link")

do_ScrapFollowing()
with open(f'{path}current/following.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(links)