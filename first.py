from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH ="C:\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/c/Dupamicaffeine/videos")

try:
    items =WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"contents"))
    )
    links=items.find_elements_by_tag_name("a")
    for link in links:
        imgs=link.find_elements_by_tag_name("img")
        for img in imgs:
            print(img.get_attribute("src"))

except :
    driver.quit()






