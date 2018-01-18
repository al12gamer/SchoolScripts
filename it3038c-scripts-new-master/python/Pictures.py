# -*- coding: utf-8 -*-
"""
@author: Wolfeco + Seibenab
"""
#TODO: do things like turning html to pdf
from bs4 import BeautifulSoup
import requests
import re
import sys, traceback
import glob, os
#traceback is for seeing proper errors

def grabImages(url, session, soup):
#we are ALL SOUP

    #today children we're taking a url, session and content of the page, then grab everything
    #with an img, we will write all those files to the current directory
    #The function also edits the source file names of the images to match names they done did get assigned when downloaded
    r= session
    #extensions ['.gif', '.jpg','.png']
    count = 0
    for img in soup.find_all("img"):
        imageurl = url + img['srcset']
        #print(imageurl)
        picture_name = 'p' + str(count) + '.jpg'
        r = session.get(imageurl, timeout=5)
        if r.status_code == 200:
            with open(picture_name, 'wb') as f:
                f.write(r.content)
        img['srcset'] = picture_name
        #img['width'] = "400"
        #img['height'] = "250"
        count = count + 1
    return soup
#def grabUnformattedText(soup):
    #wholly unneccessary for this program just testing.
    #CLIF WHY ARE WE JUST TESTING?
    #I don't know
    #unformattedText = soup.get_text()
    #return unformattedText
#def grab_page(soup):

    #stuff important on webpage in this tag
    #**hmm or just everything but the CSS

    #p = soup.find_all("div", id="HtmlView")
    #page = BeautifulSoup(str(p), "lxml")
    #return page

#def get_next_page_url(soup, url_base, bookname):
    #So that we know where to point our next requests.session.
    #thanks clif for the url -welcome dude

s = requests.session()
url = 'https://giphy.com/gifs/rabbit-chocolate-easter-TAz8QjRX1fUpq'
r = s.get(url)
soup = BeautifulSoup(r.content, "lxml")
grabImages(url, s, soup)