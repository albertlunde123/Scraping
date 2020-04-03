# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:15:40 2020

@author: Administrator

Chapter 3 - starting to crawl.
"""

"""
Det første jeg gør er at finde alle links på Tiger Woods wikipedia-side.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Tiger_Woods")
bsObj = BeautifulSoup(html)

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs["href"])
        
"""
Det finder som det skal alle links på siden, men der er også en masse som jeg 
ikke gider at have. Jeg skal derfor bruge re til at sortere i dem.

De har 3 ting tilfælles:
    They reside within the div with id set to bodycontent.
    The URLs do not contain colons
    The URLS begin with /wiki/
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Tiger_Woods")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",
                                            href=re.compile("^(\/wiki\/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

"""
Det her er helt fint, nu vil jeg lave en funktion, som tager en givet wikipedia
og spytter de interne links på den side ud.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getlinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a", 
                        href=re.compile("^(\/wiki\/)((?!:).)*$"))

links = getlinks("/wiki/Tiger_Woods")
while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getlinks(newArticle)

"""
Nu laver jeg en som undgår at gå på den samme side 2 gange.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")

"""
Nu laver jeg en som finder vælger et link, hopper til siden og snupper titlen, det
første paragraf og edit-linket. 
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print("title" + bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id = "ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("Noget der mangler, dw")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("-------------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("/wiki/Tiger_Woods")

"""
Den opfører sig lidt underligt, men så vidt jeg kan se har jeg ikke lavet nogle fejl
"""



