# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:55:05 2020

@author: Administrator
"""

from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())

from bs4 import BeautifulSoup
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

"""

Der kan opstå fejl, hvis man forsøger at tilgå en side som ikke findes.
Nu kommer der noget kode som tager højde for den slags fejl.

HTTP-fejl, hvis siden ikke er på serveren, eller hvis der går 
noget galt når man prøver at kalde den. (eks. 404 page not found).

URL-fejl, hvis siden er nede eller url-linket ikke finder noget. 

"""

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    print("ingen fejl!")
    
"""

Når man kalder objekter på en hjemmeside med BeautifulSoup, leder man efter
deres "tags" i HTML-koden. Det kan være smart at tilføje en linje kode, som tjekker
om ens tag overhovedet eksisterer.

"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
        try:
            html = urlopen(url)
        except HTTPError as e:
            return None
        try:
            bsObj = BeautifulSoup(html.read())
            title = bsObj.body.h1
        except AttributeError as e:
            return None
        return title

title = getTitle("http://pythonscraping.com/pages/page1.html")

if title == None:
    print("title could not be found")
else:
    print(title)
    
    
