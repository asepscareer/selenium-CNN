import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
## In the following segment, I show how you can get a list of news article URLs based on a keyword search.
## I use CNN as an example but news source would work.

base_url = u'https://edition.cnn.com/search?size=10&q=politics'

browser.get(base_url)
time.sleep(1)

#Finds the container that contains every news article.
main_news_container = browser.find_element_by_class_name('cnn-search__results-list')

#In main container get 'a'
text_sections = main_news_container.find_elements_by_xpath("//a[@href]")

for elem in text_sections:
    if "/2022/" in elem.get_attribute("href"):
        #this is printing the link
        print(elem.get_attribute("href"))
        #this is printing the Headline
        print(elem.text)

#Find the text body_elements inside the main_news_container
body_elements = main_news_container.find_elements_by_class_name("cnn-search__result-body")

#this is how you get the body body_elements text
print(body_elements[0].text)