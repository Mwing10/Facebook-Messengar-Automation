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



# run while alive
if __name__ == "__main__":
    while True:
        print("Starting...")
