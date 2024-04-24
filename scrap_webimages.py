from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os

def fetch_images_from_google(web_driver, search_query, num_images):
    base_url = "https://www.google.com/imghp"
    web_driver.get(base_url)
    
    search_box = web_driver.find_element_by_name('q')
    search_box.send_keys(search_query + Keys.RETURN)
    time.sleep(2)

    images = web_driver.find_elements_by_css_selector('img.rg_i.Q4LuWd')
    count = 0
    for img in images:
        src = img.get_attribute('src')
        try:
            if src:
                src = str(src)
                if src.startswith('http') or src.startswith('https'):
                    img_res = requests.get(src)
                    img_path = f"./images/{count}.jpg"
                    with open(img_path, 'wb') as f:
                        f.write(img_res.content)
                    count += 1
                    if count == num_images:
                        break
        except requests.exceptions.MissingSchema:
            continue

if __name__ == "__main__":
    driver = webdriver.Chrome()
    search_term = "Diageo brand images"
    fetch_images_from_google(driver, search_term, 10)
    driver.quit()
