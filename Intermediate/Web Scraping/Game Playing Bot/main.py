from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")

# driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documantation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documantation_link.text)
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


###################################################### CHALLENGE 1 ###################################################################

# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time" : event_times[n].text,
#         "name" : event_names[n].text
#     }

# print(events)


###################################################### CHALLENGE 2 ###################################################################
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# # all_portals.click()

# search = driver.find_element(By.NAME , "search")
# search.send_keys("Python", Keys.ENTER)

###################################################### CHALLENGE 3 ###################################################################

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("Taylor", Keys.ENTER)
last_name.send_keys("Smith", Keys.ENTER)
email.send_keys("TS@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()




 


# driver.close()
# driver.quit()