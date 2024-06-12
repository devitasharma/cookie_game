#todo importing essential selenimum classes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#todo setting up selenium
driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option("detach", True)
driver_object = webdriver.Chrome(driver_option)
driver_object.get("http://orteil.dashnet.org/experiments/cookie/")
# todo setting up to click cookie
cookie_click = driver_object.find_element(By.ID, value="cookie")
# todo get item name that we can upgrade
item_name = driver_object.find_elements(By.CSS_SELECTOR, value="#store div")
item_name_list = []
for i in item_name:
    item_id = i.get_attribute("id")
    item_name_list.append(item_id)
#todo setting up the timings for the game to run until
timout_after_5sec = time.time() + 5
timout_after_5min = time.time() + 60 * 5
#todo while loop to keep the game running
while True:
    #todo keep the cookie clicking until 5 sec
    cookie_click.click()
    #todo check if 5 sec have passed or not?
    if time.time() > timout_after_5sec:
        price = driver_object.find_elements(By.CSS_SELECTOR, value="#store b")
        item_price_list = []
        # for i in price:
        #     element = i.text
        #     if element != " ":
        #         cost = element.split("-")[1].replace(",","")
        #         print(cost) ANOTHER METHOD FOR THIS IS AS FOLLOW:
        for i in price:
            if len(i.text) != 0:
                item_price = i.text.replace(",", "").split()
                item_price_list.append(int(item_price[-1]))
        # print(item_price_list)
        #todo join item_price and item_name in dictionary
        upgraded_items = {}
        for i in range(len(item_price_list)):
            upgraded_items[item_price_list[i]] = item_name_list[i]
        #print(upgraded_items)
        #todo counting cookies total currently
        count = driver_object.find_element(By.ID, value="money").text
        if "," in count:
            count = count.replace(",", "")
        cookie_count = int(count)
        # print(cookie_count)
        #todo checking what item we can afford with our cookie_count
        affordable_items = {}
        for key, value in upgraded_items.items():
            if cookie_count >= key:
                affordable_items[key] = value
        # print(affordable_items)
        #todo purchase most expensive cookie & click on it
        most_expensive_cookie = max(affordable_items)
        # print(most_expensive_cookie)
        purchase_upgrade_id = affordable_items[most_expensive_cookie]
        # print(purchase_upgrade_id)
        purchase_click = driver_object.find_element(By.ID, value=f"{purchase_upgrade_id}")
        purchase_click.click()
        #todo add next 5 sec
        timout_after_5sec = time.time() + 5
        #todo check if time cross 5min from start
        if time.time() >= timout_after_5min:
            cookies_per_sec = driver_object.find_element(By.ID, value="cps").text
            print(cookies_per_sec)
            break
