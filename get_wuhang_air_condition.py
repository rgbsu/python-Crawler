import requests
import re
from bs4 import BeautifulSoup
import bs4
from goose3 import Goose
from goose3.text import StopWordsChinese



def getHTMLText(URL):
    try:
        r = requests.get(URL)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def geturl(ulist, html):
   
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find('div',attrs= {'class':'c-Part1'})
    for tr in soup.find('ul').children:
        if isinstance(tr, bs4.element.Tag):
            link = tr.find('a')
            
            ulist.append([[link.get('href')],[link.get('title')]])

  

def gethtmlwords(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div',attrs={'class':'detailscon'})
    div = div.find('div', attrs = {'id': 'zoom'})
    words = ''
    for p in div.children:
        if isinstance(p, bs4.element.Tag):
            words+=p.getText()
    return words

# def printTxt(ptr):

def main():
    ulist = []
    depth = 10
    for i in range(depth):
        start_url = 'http://hbj.wuhan.gov.cn/hbKqjcbg/index'
        try:
            i=i+1
            url = start_url + '_'+str(i)+'.jhtml'
            r = getHTMLText(url)
            geturl(ulist,r)

            for i in range(len(ulist)): 
                with open('air_condition/'+ulist[i][1][0] + '.txt', 'w') as f:
                    f.write(gethtmlwords(getHTMLText(ulist[i][0][0])))
        except:
            continue
            

  
main()