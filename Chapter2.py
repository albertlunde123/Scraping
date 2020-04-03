# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 10:25:36 2020

@author: Administrator

--chapter 2--

"""
"""
Jeg scraper alle navne i War and Peace. Jeg udnytter at de er omgivet af 
et "span" tag med og classen "green"
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
type(bsObj)

name_list = bsObj.findAll("span", {"class":"green"})
for name in name_list:
    print(name.get_text())
    
"""
Jeg scraper nogle ting fra den falske webbutik på pythonscraping. Jeg skal her
gøre brug af tingene placering i HTML-koden ikke deres tags.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)


for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)

"""
siblings
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)


"""
parents

Jeg vælger det første billede på siden, går en tak bagud i træet (parent) og en
gren op (previous sibling). Derefter tager teksten i det (get_text()). 
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

"""
Regular Expressions - nu bruger re-pakken til at finde billedet.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
