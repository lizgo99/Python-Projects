from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

five_min_timout = time.time() + 60*5
five_sec_timout = time.time() + 5

# FIRST ATTEMPT
# while True:
#     cookie.click()
#     if time.time() > five_min_timout:
#         print(driver.find_element(By.ID, "cps").text)
#         break 
#     elif time.time() > five_sec_timout:
#         store = driver.find_elements(By.CSS_SELECTOR, "#store div b")
#         grayed_items = driver.find_elements(By.CSS_SELECTOR, "#store div.grayed b")
#         non_grayed_items = []
#         prices = []
#         for item in store:
#             if item not in grayed_items:
#                 non_grayed_items.append(item)
#                 prices.append(int(item.text.split(" - ")[1].replace(",","")))

#         if prices:
#             i = prices.index(max(prices))
#             item = non_grayed_items[i]
#             item.click()
            
#         five_sec_timout = time.time() + 5

# SECOND ATTEMPT - way faster
while True:
    cookie.click()
    if time.time() > five_min_timout:
        print(driver.find_element(By.ID, "cps").text)
        break 
    elif time.time() > five_sec_timout:
        my_money = int(driver.find_element(By.ID, "money").text.replace(",",""))
        store = driver.find_elements(By.CSS_SELECTOR, "#store div b")
        max_affordable = None
        for item in store:
            if item.text:
                price = int(item.text.split(" - ")[1].replace(",",""))
                if price <= my_money : 
                    max_affordable = item
        if max_affordable:
            max_affordable.click()
        five_sec_timout = time.time() + 5
            



    
        
driver.close()
# driver.quit()
