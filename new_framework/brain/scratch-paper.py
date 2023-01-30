from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
bad_links = ["videos", "login", "photos", "login/", "photos/", "videos/", "login?next", "photos?tab", "videos?tab", "login?next=", "photos?tab=", "videos?tab=", "reg/", "reg", "?rs=7", "recover/", "photo/", "/login/", "/recover/", "/photo/"]
driver.get("https://www.facebook.com/ExtonRegionChamber/following")
time.sleep(3)

i = 0
while i < 30:
    i+=1
    time.sleep(1)
    page = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
def do_ScrapFollowing():
    elems = driver.find_elements_by_xpath("//a[@href]") 
    for elem in elems:
        if elem.get_attribute("href").startswith("https://www.facebook.com/"):
            if elem.get_attribute("href") != bad_links:
                links = []
                links.append(elem.get_attribute("href"))
                print(elem.get_attribute("href"))
            else: 
                print("Not a facebook link")