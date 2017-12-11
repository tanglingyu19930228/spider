#!/usr/bin/env python3
# coding=utf-8
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

homeurl = 'http://www.landchina.com/default.aspx?tabid=263&ComName=default'
driver.get(homeurl)

start_time = '//*[@id="TAB_queryDateItem_270_1"]'
end_time = '//*[@id="TAB_queryDateItem_270_2"]'
xingzhengqu = '//*[@id="TAB_queryTblEnumItem_256"]'
tudiyongtu = '//*[@id="TAB_queryTblEnumItem_212"]'
gongyingfangshi = '//*[@id="TAB_queryTblEnumItem_215"]'

elem1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, start_time)))
elem1.click()
elem1.send_keys('2005-1-1')
driver.find_element_by_xpath('//*[@id="TAB_queryDateItem_270_1_Canlender"]/div/div[3]/a').click()

elem2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, end_time)))
elem2.click()
elem2.send_keys('2017-12-6')
driver.find_element_by_xpath('//*[@id="TAB_queryDateItem_270_2_Canlender"]/div/div[3]/a').click()

elem3 = driver.find_element_by_xpath(xingzhengqu)
elem3.click()
driver.switch_to_window(driver.window_handles[1])
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="treeDemo_19_switch"]'))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="treeDemo_35_switch"]'))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="treeDemo_49_ico"]'))).click()
driver.find_element_by_xpath('//*[@id="Table1"]/tbody/tr[1]/td/table/tbody/tr/td[3]/input[1]').click()
driver.switch_to_window(driver.window_handles[0])

elem4 = driver.find_element_by_xpath(tudiyongtu)
elem4.click()
driver.switch_to_window(driver.window_handles[1])
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="treeDemo_2_switch"]'))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="treeDemo_17_ico"]'))).click()
driver.find_element_by_xpath('//*[@id="Table1"]/tbody/tr[1]/td/table/tbody/tr/td[3]/input[1]').click()
driver.switch_to_window(driver.window_handles[0])

elem5 = driver.find_element_by_xpath(gongyingfangshi)
elem5.click()
driver.switch_to_window(driver.window_handles[1])
time.sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="treeDemo_3_ico"]'))).click()
driver.find_element_by_xpath('//*[@id="Table1"]/tbody/tr[1]/td/table/tbody/tr/td[3]/input[1]').click()
driver.switch_to_window(driver.window_handles[0])

chaxun = '//*[@id="TAB_QueryButtonControl"]'
elem6 = driver.find_element_by_xpath(chaxun)
elem6.click()


# 提交
urls=[]
def get_info():
    N = 2
    apath = '//*[@id="TAB_contentTable"]/tbody/tr[2]/td[3]/a'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, apath)))
    while True:
        try:
            elemt = driver.find_element_by_xpath('//*[@id="TAB_contentTable"]/tbody/tr[%d]/td[3]/a' % N)
            need_url=elemt.get_attribute("href")
            print(N-1,'>>>',need_url)
            list_url=[]
            list_url.append(need_url)
            urls.append(list_url)
            N += 1
        except:
            break

def next_page():
    bpath='//*[@id="mainModuleContainer_485_1113_1539_tdExtendProContainer"]/table/tbody/tr[1]/td/tabl' \
          'e/tbody/tr[2]/td/div/table/tbody/tr/td[2]/a[7]'
    elem=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, bpath)))
    xiayiye=elem.get_attribute('href')
    elem.click()
    return xiayiye


while True:
    get_info()
    if next_page() is not None:
        pass
    else:
        break

with open('中国土地.csv','w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(urls)

