from webdriver_manager.chrome import ChromeDriverManager
#opening browser
from webdriver_manager.chrome import ChromeDriverManager 
browser= webdriver.Chrome(executable_path=ChromeDriverManager().install())
#Login to facebook
def login():
    browser.get('https://www.facebook.com')
    #enter own user here
    browser.find_element_by_id("email").send_keys("6103124684")
    time.sleep(random.randrange(1,5))
    #enter own password here
    browser.find_element_by_id("pass").send_keys("Winger910")
    time.sleep(random.randrange(1,5))
    browser.find_element_by_id("pass").send_keys(Keys.ENTER)

#provide the link to Facebook Friend list page
browser.get('https://www.facebook.com/me/friends')
#this loop is for scrolling down till the end of page
#you can increase or decrease the size of loop according to your friend list
i=0
while i<2000:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    i=i+1
    print(i)
    time.sleep(5)

#pull urls from following
html=browser.page_source
soup=BeautifulSoup(html)
links=soup.find_all('a',{"class":"qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq jxuftiz4 cxfqmxzd"})
users=[]
i=0
for link in links:
    i=i+1
    users.append(link["href"])
#Export to excel
df=pd.DataFrame(users,columns=["URL"])
#put the address of the directory accordingly 
df.to_excel(r"/Users/mikewing/Desktop/Excel/FB_Following")
