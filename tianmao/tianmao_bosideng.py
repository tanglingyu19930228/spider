#!/usr/bin/env python3
# coding=utf-8
import time
import csv
from functools import namedtuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()


'''通过天猫的搜索访问旗舰店的主页'''
driver.get('https://www.tmall.com/')
assert "天猫" in driver.title
elem_sousuo = driver.find_element_by_name("q")
elem_sousuo.clear()
elem_sousuo.send_keys("波司登")
elem_sousuo.send_keys(Keys.RETURN)
elem1_tuijian = driver.find_element_by_xpath("//div[@class='m-portal']/div/div/a")
tuijian_herf = elem1_tuijian.get_attribute("href")
driver.get(tuijian_herf)

elem_allbaby = driver.find_element_by_xpath("//*[@id='shop17361190421']/div/div/div/div/div/div/div/div[15]/a")
allbaby_href = elem_allbaby.get_attribute("href")
time.sleep(1)
driver.get(allbaby_href)
'''获取所有宝贝'''
assert "No results found." not in driver.page_source


'''获取信息'''
infos = []
row = ['name', 'price', 'sale_area', 'judge']
def get_info():
    item_xpath = '//*[@id="J_ShopSearchResult"]/div/div[@class="J_TItems"]'
    source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, item_xpath)))

    '''获取名称，价格，销量，评价'''
    name = '//dd[@class="detail"]/a'
    # 名称
    price = '//dd[@class="detail"]/div/div[1]/span[2]'
    # 价格
    sale_area = '//dd[@class="detail"]/div/div[2]/span'
    # 销量
    judge = '//dd[@class="rates"]/div/h4/a'
    # 评价
    source1 = source.find_elements(By.XPATH, name)
    names = [name.text for name in source1]
    source2 = source.find_elements(By.XPATH, price)
    prices = [price.text for price in source2]
    source3 = source.find_elements(By.XPATH, sale_area)
    sale_areas = [sale_area.text for sale_area in source3]
    source4 = source.find_elements(By.XPATH, judge)
    judges = [judge.text for judge in source4]
    info = namedtuple('info', row)
    how_many = len(names) - 8
    # print(len(names),len(prices),len(sale_areas),len(judges))
    # 推荐的商品没有评价
    for i in range(how_many):
        oneinfo = info(names[i], prices[i], sale_areas[i], judges[i])
        infos.append(oneinfo)
    print('Download one page')



'''获取下一页地址'''
def next_url():
    next_xpath = '//*[@id="J_ShopSearchResult"]/div/div[@class="J_TItems"]/div[@class="pagination"]' \
                 '/a[@class="J_SearchAsync next"]'
    try:
        source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, next_xpath)))
        return source.get_attribute("href")
    except TimeoutException:
        return None
    except:
        print('有一些未知的错误')
        return None



'''循环获取信息'''
while True:
    get_info()
    if next_url() is not None:
        driver.get(next_url())
        continue
    else:
        break



'''保存'''
with open('data_bosideng1.csv', 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(row)
    f_csv.writerows(infos)
print('Done')
driver.close()