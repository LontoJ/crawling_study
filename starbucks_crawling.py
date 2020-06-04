from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import csv

crawling_url = "https://www.starbucks.co.kr/menu/drink_list.do"
front_url = "https://www.starbucks.co.kr/menu/drink_view.do?product_cd="

driver = webdriver.Chrome()
driver.get(crawling_url)

csv_filename = "Starbucks_crawling.csv"
csv_open = open(csv_filename, 'w+', encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('이름', '영어 이름', '설명', '제품 사진'))

time.sleep(2)

body = driver.find_element_by_tag_name('body')
page_down = 0
while page_down < 20:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    page_down += 1

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
bucks_list = soup.select('.goDrinkView')

for i in bucks_list:
    coffee_num = i.attrs['prod']
    coffee_name = i.img.attrs['alt']
    num_url = coffee_num
    product_url = front_url + num_url
    
    driver.get(product_url)
    time.sleep(1)
    html2 = driver.page_source
    soup2 = BeautifulSoup(html2, "html.parser")
    coffee_info = soup2.select('.product_view_wrap1')
    for i in coffee_info:
        coffee_name_eng = i.select_one('h4').span.text
        coffee_mood = i.select_one('.t1').text
        coffee_img = "https:" + i.img.attrs['src']
    
    csv_writer.writerow((coffee_name, coffee_name_eng, coffee_mood, coffee_img))
    




    

    










driver.close()