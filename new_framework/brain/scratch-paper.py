from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
bad_links = ["videos", "login", "photos", ""]
driver.get("https://www.facebook.com/ExtonRegionChamber/following")
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    if elem.get_attribute("href").startswith("https://www.facebook.com/"):
        if elem.get_attribute("href") != "https://www.facebook.com/login" or "https://www.facebook.com/ExtonRegionChamber/" or "https://www.facebook.com/photos":
            links = []
            links.append(elem.get_attribute("href"))
        print(elem.get_attribute("href"))
    else: 
        print("Not a facebook link")