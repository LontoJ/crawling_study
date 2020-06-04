from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
import csv


crawling_url = 'https://www.billboard.com/charts/hot-100'


driver = webdriver.Chrome()
driver.get(crawling_url)

csv_filename = "Billboard_crawling.csv"
csv_open = open(csv_filename, 'w+', encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('이번주 랭킹', '제목', '가수', '커버 이미지'))

time.sleep(2)


body = driver.find_element_by_tag_name('body')
page_down = 0
while page_down < 20:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    page_down += 1


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
chart_list = soup.select('.chart-element__wrapper.display--flex.flex--grow.sort--this-week')

for i in chart_list:
    song_name = i.select_one('.chart-element__information__song').text
    song_rank = i.select_one('.chart-element__rank__number').text
    song_artist = i.select_one('.chart-element__information__artist').text
    song_img = i.select_one('.chart-element__image')['style']
    
    #print(song_name)
    #print(song_rank)
    #print(song_artist)
    #print(song_img)
    #print()
    


    
    
    
    
    csv_writer.writerow((song_rank, song_name, song_artist, song_img[23:-3]))

driver.close()