# functions for the main program when we rebuild (third times a charm!)

def get_following():
    following = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for link in soup.find_all('', class_=''): # <== when not on school wifi add class names for soup
        following.append(link.get('href')) # think about checking this up.. dont look right
    return following


def grab_login(file):
    with open(file, 'r') as f_reader:
        for login in f_reader:
            login = login.split(":")
            return login