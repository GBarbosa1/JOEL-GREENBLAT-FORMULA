from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
 
def scrap_init(is_headless, url):
    options = Options()
    options.headless = is_headless
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    url = url
    browser.get(url)
    time.sleep(0.05)
    soup = BeautifulSoup(browser.page_source, 'lxml')
    browser.quit()
    return soup
            
   
