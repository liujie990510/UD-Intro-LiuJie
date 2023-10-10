from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# open browser object
# create ChromeOptions
chrome_options = webdriver.ChromeOptions()
# create Chrome
driver = webdriver.Chrome(options=chrome_options)
# maximum time to wait for a page to load (in seconds)
driver.implicitly_wait(10)



#####scrap logic
url = "https://openlibrary.org/"
driver.get(url)
html = driver.page_source
import requests
from bs4 import BeautifulSoup
import os
# use BeautifulSoup interpret HTML
soup = BeautifulSoup(html, 'html.parser')

# check <img> tab
images = soup.find_all('img')


# iterate over all images and download JPG images
for image in images:
    src = image.get('src')
    if src.endswith('.jpg'):
        # constructing the URL of a JPG image
        if src.startswith('http'):
            jpg_url = src
        else:
            base_url = 'http:'  # URL
            jpg_url = base_url + src
        print(jpg_url)
        # download JPG

        try:
            response = requests.get(jpg_url)
            if response.status_code == 200:
                # withdraw JPG filename
                file_name = os.path.basename(jpg_url)
                # save JPG
                with open(file_name, 'wb') as file:
                    file.write(response.content)
                print("下载成功:", file_name)
            else:
                print("下载失败:", jpg_url)
        except Exception as E:
            print(E)
            pass
            time.sleep(5)

# exit
driver.quit()


