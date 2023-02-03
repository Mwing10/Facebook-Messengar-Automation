try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service as ChromeService
    import time, os, csv, subprocess
    from alive_progress import alive_bar
except ImportError as e:
    print("Unable to import some libraries, please install them first with 'python3 -m pip install -r requirements.txt'\n", e)
    time.sleep(3)
    exit()
options = webdriver.ChromeOptions() # for headless
options.add_argument('--headless')

# start and init the driver + variables
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) #options=options, (for headless)
path = os.getcwd() + "/"
bad_links = ["videos", "login", "photos", "login/", "photos/", "videos/", "login?next", "photos?tab", "videos?tab", "login?next=", "photos?tab=", "videos?tab=", "reg/", "reg", "?rs=7", "recover/", "photo/", "/login/", "/recover/", "/photo/"]
links = []
target_profile = ""
target_website = ""
target_endpoint = ""
target_url = ""

def grab_login(file): #open file and grab login details
    with open(file, 'r') as f_reader:
        for login in f_reader:
            login = login.split(":")
            return login

def login(target_website):
    driver.get(target_website + "/login") # drive browser to target website login page
    user_details = grab_login(f"~/info/user.txt")
    usern = user_details[0]
    passw = user_details[1] # save login details to variables
    username = driver.find_element_by_id("email") # find email feild 
    username.send_keys(usern) # send username to feild
    time.sleep(2.5)
    password = driver.find_element_by_id("pass") # find password feild
    time.sleep(3.5) 
    password.send_keys(passw) # send password to feild
    time.sleep(2.5)
    driver.find_element_by_name("login").click() # click login button
    time.sleep(10)

def do_ScrapFollowing():
    for elem in elems: # loop through all populated profile elements from the page
        if elem.get_attribute("href").startswith("https://www.facebook.com/"): # check links for relevence 
            if elem.get_attribute("href") != bad_links: # check links for relevence
                links.append(elem.get_attribute("href")) # add links to list of good links

def clean_up():
    print("Cleaning up...")
    time.sleep(1)
    subprocess.run("clear", shell=True)

# run while alive
if __name__ == "__main__":

    # start the program, input target website data
    target_profile = input("Enter the profile you want to scrape (i.e. /ExtonRegionChamber/ [yes with slashes]): ")
    target_website = input("Enter the website you want to scrape (i.e. https://facebook.com): ")
    target_endpoint = input("Enter the endpoint you want to scrape (i.e. following): ")
    target_url = target_website + target_profile + target_endpoint

    print("Logging in...")
    grab_login(f"{path}info/user.txt") # grab the login details
    login(target_website) # login to facebook
    clean_up()
    driver.get(target_url)

    with alive_bar(100, dual_line=True, bar="classic") as bar:
        for i in range(3):
            bar.text("Target Aquired: %s" % target_url) 
            time.sleep(1)
            driver.get(target_url) # drive browser to target website
            time.sleep(1)
            bar()
        for i in range(62):
            bar.text("Scraping...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll down to populate list of elements
            time.sleep(1)
            elems = driver.find_elements_by_xpath("//a[@href]")  # find all elements with href
            time.sleep(1)
            bar()
        for i in range(15):
            bar.text("Saving...")
        for i in range(30):
            bar.text("Cleaning up...")
            bar() # finish bar
    
    do_ScrapFollowing() # grab the links to following profiles and save them to a execl file
    with open(f'{path}current/following.csv', 'w') as f:
        writer = csv.writer(f) # write to csv
        writer.writerow(links)
    clean_up() # clean up the terminal
    driver.close() # close the driver
    print("Finished! Contents scrapped saved to following.csv")
