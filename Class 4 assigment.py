## 1.

# from selenium import webdriver
# from time import sleep
# my_driver = webdriver.Chrome(executable_path="c:/Users/yanivl/Downloads/chromedriver.exe")
# my_driver2 = webdriver.Firefox(executable_path="c:/Users/yanivl/Downloads/geckodriver.exe")
#
# my_driver.get("http:///www.walla.co.il")
# my_driver2.get(http:///www.ynet.co.il)





### 2.
# from selenium import webdriver
# my_driver = webdriver.Chrome(executable_path="c:/Users/yanivl/Downloads/chromedriver.exe")
# my_driver2 = webdriver.Firefox(executable_path="c:/Users/yanivl/Downloads/geckodriver.exe")
#
#
# title = "walla.co.il"
# my_driver.get("http:///www.walla.co.il")
# my_driver2.get("http://ynet.co.il")
# my_driver.navigate().refresh()
# get_title = my_driver.title
# assert get_title == title


### 4.


# from selenium import webdriver
# my_driver = webdriver.Chrome(executable_path="c:/Users/yanivl/Downloads/chromedriver.exe")

# my_driver.get("https://translate.google.com/?sl=iw&tl=en&op=translate")
# my_element = my_driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea")
# my_element.send_keys("אני רובוט")


## 5.
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# URL = "https://github.com"
#
# my_driver = webdriver.Chrome(executable_path="c:/Users/yanivl/Downloads/chromedriver.exe")
# my_driver.get(URL)
#
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# browser = webdriver.Chrome(executable_path=my_driver, chrome_options=chrome_options)
# browser.get(URL)



from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome(executable_path="c:/Users/yanivl/Downloads/chromedriver.exe")
my_driver.get("https://he.aliexpress.com/")
my_element = my_driver.find_element_by_xpath("""//*[@id="search-key"]""")
my_element.send_keys("Itay")
sleep(3)
my_driver.find_element_by_xpath("//*[@id=\"form-searchbar\"]/div[1]/input").click()
