from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
# from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import pandas as pd

option = webdriver.ChromeOptions()
path ="C:/Users/Tlou Ramotshela/Downloads/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path, options=option)
driver.get("https://www.checkers.co.za/c-2413/All-Departments/Food")

# "https://www.checkers.co.za/c-2257/All-Departments/Drinks"
# https://www.checkers.co.za/c-2413/All-Departments/Food
driver.maximize_window()
time.sleep(5)
products = []
prod_information = []
columns = []
rows_in = []
num = driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[2]/p").text
number = num[0]
num1 = int(number)* 1000
num2 = num[2:5]
numt = num1 + int(num2)+1
print(numt)
scr = numt / 20
loo = round(scr, 0) + 1
print(loo)
for p in range(1, 44):
    try:
        driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/ul/li[8]").click()
        time.sleep(3)
    except ElementClickInterceptedException:
        time.sleep(2)
        pass
    except NoSuchElementException:
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/ul/li[8]").click()
for k in range(1, 12):
    img = driver.find_elements_by_class_name("item-product__image")
    for i in range(2, len(img)+1):
        try:
            item = driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[2]/div["+str(i)+"]/div/figure/div")
            print(item)
            item.click()
            time.sleep(7)
        except ElementClickInterceptedException:
            pass
        except NoSuchElementException:
            item = driver.find_element_by_xpath(f"/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[2]/div[{str(i)}]/div/figure/figcaption/div[1]/h3/a")
            item.click()
            time.sleep(5)
        try:
            prod_name = driver.find_element_by_class_name("pdp__name").text
            time.sleep(1)
            driver.execute_script("window.scrollBy(0,500)", "")
            time.sleep(1)
            try:
                driver.find_element_by_id("accessibletabsnavigation0-1").click()
                time.sleep(2)
            except ElementClickInterceptedException:
                pass
            rows = driver.find_elements_by_xpath("/html/body/main/div[4]/div[4]/div/div/div/div[4]/div/table/tbody/tr")
            print(len(rows))
            time.sleep(2)
            time.sleep(2)
            row = len(rows)
            time.sleep(2)
            for r in range(1, row+1):
                cols = driver.find_elements_by_xpath(f"/html/body/main/div[4]/div[4]/div/div/div/div[4]/div/table/tbody/tr[{str(r)}]/td")
                print(len(cols))
                time.sleep(2)
                col = len(cols)
                for c in range(1, col+1):
                    content = driver.find_element_by_xpath(f"/html/body/main/div[4]/div[4]/div/div/div/div[4]/div/table/tbody/tr[{str(r)}]/td[{str(c)}]").text
                    print(content)
                    '/html/body/main/div[4]/div[4]/div/div/div/div[4]/div/table/tbody/tr[1]/td[1]'
                    '/html/body/main/div[4]/div[4]/div/div/div/div[4]/div/table/tbody/tr[1]/td[2]'
                    if c == 1:
                        columns.append({content})
                    elif c == 0:
                        rows_in.append({content})
                    else:
                        columns.append({content})
                    prod_information.append(content)
            products.append({"ProdName": prod_name})
            print(prod_name)
            time.sleep(2)
        except NoSuchElementException:
            time.sleep(5)
        print('Done')
        driver.back()
        time.sleep(7)
        # action = ActionChains(driver)
        # action.move_to_element(driver.find_element_by_xpath("/html/body/main/header/div[3]/div[2]/div[1]/nav/div[3]/ul/li[1]/span[1]"))
        # driver.find_element_by_xpath("/html/body/main/header/div[3]/div[2]/div[1]/nav/div[3]/ul/li[1]/div/div/div[2]/div/ul/li[2]").click()
    try:
        driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/ul/li[8]").click()
    except ElementClickInterceptedException:
        time.sleep(2)
        pass
    except NoSuchElementException:
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/main/div[4]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/ul/li[8]").click()
print('We are ready to go')
df2 = pd.DataFrame(columns)
df3 = pd.DataFrame(rows_in)
df = pd.DataFrame(products)
df1 = pd.DataFrame(prod_information)
df1.to_csv('table.csv', index=False)
df.to_csv('checkers_scraper.csv', index=False)
df2.to_csv('columns.csv', index=False)
df3.to_csv('rows.csv', index=False)
driver.close()