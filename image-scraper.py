# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:13:59 2019

@author: aprilmarikko
"""

from urllib.request import urlretrieve as saveimg
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.reddit.com/r/imveryedgy/'

page_html = ""

def fetch_html(url):
    try:
            uClient = uReq(my_url)
            page_html = uClient.read()
            return page_html
    except:
            print ("failed,trying again....")
            return ( fetch_html(url) );




page_soup = soup(fetch_html(my_url), "html.parser")

images = page_soup.findAll("img", {"alt":"Post image"})
titles = page_soup.findAll("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})


counter = 0
for image in images:
    title = titles[counter].text
    saveimg(image["src"], title + ".jpg")
    counter += 1