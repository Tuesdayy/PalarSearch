from selenium import webdriver
from nameSearch import nameSearch
import re

magsig = dict()
magsig['sciencedirect'] = "//a[@title='References']"
magsig['nature'] = "//*[@data-track-label='link:References']"


def magzineLabel(html):
    label = None
    for key in magsig.keys():
        if re.search(key, html):
            label = key
            break
    return label


def magazineSearch(name, label):
    driver = webdriver.Chrome()
    url = nameSearch(name)
    driver.get(url)
    driver.implicitly_wait(10)

    if label == 'sciencedirect':
        driver.find_element_by_xpath("//a[@title='References']").click()
        ref_title = list()
        for k in range(1, 10):
            s = 'ref-id-sref' + str(k)
            text = driver.find_element_by_id(s)
            ref_title.append(text.text)

        ref_title = [x for x in ref_title if x]
        return ref_title

    if label == 'nature':
        driver.find_element_by_xpath("//*[@data-track-label='link:References']").click()
        ref_title = list()
        for k in range(1, 10):
            s = 'ref-CR' + str(k)
            text = driver.find_element_by_id(s)
            ref_title.append(text.text)

        ref_title = [x for x in ref_title if x]
        return ref_title

    warning = 'not in dict'
    return warning
