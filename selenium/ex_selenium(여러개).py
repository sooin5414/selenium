from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

search_words = ["트와이스 모모", "트와이스 미나", "트와이스 정연", "마마무 솔라"]

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
current_path = os.getcwd()

for search_word in search_words:
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(search_word)
    elem.send_keys(Keys.RETURN) #python selenium enter key

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_elements(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
            
        last_height = new_height

#이미지 저장 폴더 생성

    try:
        if not os.path.exists(search_word):
            os.makedirs(search_word)
    except Exception as err:
        print(err)
        pass

#images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")[0].click() #python selenium click key
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

    count = 1
    for image in images:
        if count > 300:
            break
        try :
            image.click() #이미지를 클릭하는 
            time.sleep(2) #이미지 로딩 시간 주기 
            img_url = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img").get_attribute("src") #python selenium img src 
            #python download image by url
            urllib.request.urlretrieve(img_url, search_word +"/" +search_word+ str(count) + ".jpg")
            count += 1

        except:
            pass
    driver.back()
driver.close()

