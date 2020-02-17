# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:21:45 2020

@author: Rishabh Taneja
"""

#url = https://311.boston.gov/?service_id=54c65c0669632a1ac4f2acb1

import urllib
import urllib.request
from bs4 import BeautifulSoup
import string
from warnings import warn
from string import digits
import re

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

i = 1

for number in digits:
    soup = make_soup("https://311.boston.gov/?" + number +"service_id=54c65c0669632a1ac4f2acb1")
    
    for img in soup.find_all('img', {'src':re.compile('.jpg')}):
        temp = img.get('src')
        temp = temp.replace("/thumb_large_","/")
        if temp[:1] == "/":
            image = "https://311.boston.gov" + temp
        else:
            image = temp
    
    
        nametemp = img.get('alt')
        if len(nametemp)==0:
            filename = str(i)
            i = i + 1
        else:
            filename = nametemp
            
        imagefile = open(filename + ".jpeg", "wb")
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()
        
        
        
  