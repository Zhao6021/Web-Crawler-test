#!/usr/bin/env python
# coding: utf-8

# In[83]:


import requests as rq
from bs4 import BeautifulSoup as BS

url = "https://www.ptt.cc/bbs/Beauty/index.html"

r = rq.Session()
payload={
    'from':'/bbs/Beauty/index.html',
    'yes':'yes'
}
#print(r.text)
r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FBeauty%2Findex.html", payload)

for i in range(1,1001):
    if not i%50:
        print("----------------------------------------------")
    test = r.get(url)
    soup = BS(test.text, "html.parser")
    
    bigTitle = soup.select("div.r-ent")
    for tar in bigTitle:
        if tar.select_one("div.nrec span") and tar.select_one("div.nrec span").text == "爆":
            result = tar.select_one("div.title a")
            print(result.text,":")
            print("https://www.ptt.cc"+result["href"])
        
    '''
    sel = soup.select("div.title a")

    for tar in sel:
        print(tar["href"], tar.text)
    '''
        
    l = soup.select("div.btn-group.btn-group-paging a")
    url = "https://www.ptt.cc" + l[1]["href"]

