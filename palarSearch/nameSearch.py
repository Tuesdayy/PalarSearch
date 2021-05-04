import requests
from lxml import etree
from selenium import webdriver
import time

def nameSearch(search):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49'}
    url = 'https://scholar.google.com/'

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    search_text = driver.find_element_by_name('q')
    search_text.send_keys(search)
    search_text.submit()
    time.sleep(1)

    currentURL = driver.current_url
    currentResponse = requests.get(currentURL, headers=headers)
    currentHtml = etree.HTML(currentResponse.content)
    driver.close()

    fristLink = "//h3/a/@href"
    link_html = currentHtml.xpath(fristLink)
    link_html = link_html[0]

    return link_html


