#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request as req
from bs4 import BeautifulSoup as soup


# In[2]:


user_agent = {"User-Agent" : "Mozilla/5.0"}


# In[12]:


url = 'https://www.wuxiaworld.com/novel/rmji/rmji-chapter-'
default = int(input("Enter Default chapter no : "))


# In[9]:


def fetch_page(url):
    print(url)
    page = req.urlopen(req.Request(url,headers=user_agent))
    container = soup(page,'html.parser')
    return container


# In[10]:


def fetch_chapter(file,container):
    txt = container.find_all('p',{'dir' : 'ltr'})
    file.write('''<h1>
            {}
        </h1>
        '''.format(container.find_all('h4',{'class':''})[1].text))
    for i in range(len(txt)): 
        file.write('''<p>{}</p>'''.format(txt[i].text))
    file.write("</body>\n</html>")


# In[13]:


with open('file.html','w',encoding='utf-8') as file:
    file.write('''<!DOCTYPE html>
    <html>
        <head>
            <meta charset='UTF-32'>
        </head>
        <body>''')
    
    for i in range(int(input("Chapters required : "))+1):
        fetch_chapter(file,fetch_page(url+str(i+default)))


# In[7]:


file.close()


# In[ ]:





# In[ ]:




