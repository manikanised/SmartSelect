#!/usr/bin/env python
# coding: utf-8

# In[1]:

def feature_extraction():
    from bs4 import BeautifulSoup
    import requests
    
    
    rnge='500000-2000000'
    
    
    HEADERS = ({'User-Agent':'Chrome/44.0.2403.157',
                'Accept-Language': 'en-US, en;q=0.5'})

    URL="https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A1389432031%2Cp_36%3A"+rnge+"&dc&qid=1636374607&rnid=1318502031&ref=sr_nr_p_36_1"
    
    
    webpage=requests.get(URL, headers=HEADERS)
    soup= BeautifulSoup(webpage.content, "lxml")
    
    al=soup.findAll("div",attrs={"data-component-type": 's-search-result'})
    
    
    links=[]
    prices=[]
    
    for i in al:
        try:
            price=i.find("span", attrs={"class":"a-offscreen"})
            price=price.string
            prices.append(price[1:])
        except:
            continue
        i=i.find("span",attrs={"data-component-type":"s-product-image"})
        i=i.find("a")["href"]
        links.append(i)
    
    names=[(i.split('/'))[1] for i in links]
    
    
    print(len(prices),len(links))
    print(names)
    
    def clean(featstr):
        i=0
        while i < len(featstr)-1:
            if featstr[i]=="M" and featstr[i+1]=="P" and featstr[i-1]==" ":
                featstr=featstr[:i-1]+featstr[i:]
            if featstr[i]=="G" and featstr[i+1]=="B" and featstr[i-1]==" ":
                featstr=featstr[:i-1]+featstr[i:]
            i+=1
        print("features",featstr)
        return featstr
                
    
    def extract(featstr):
        featstr=clean(featstr)
        featstr=featstr.split(' ')
        lst=[""]*3
        for i in featstr:
            if i[-2:]=='MP' and lst[0]=="":
                s=i[:-2]
                s=s.replace("MP","")
                print(s)
                if "+" in s:
                    s=s.split("+")
                    s=list(map(int,s))
                    s=max(s)
                else:
                    s=int(s)
                lst[0]=s
            elif i[-2:]=='GB' and lst[1]=="":
                lst[1]=int(i[:-2])
            elif i[-2:]=='GB' and lst[2]=="":
                lst[2]=int(i[:-2])
        return lst

    lstoffeatures=[]
    for i in range(6):
        URL1=links[i]
        URL1="http://amazon.in"+URL1
        print("fetching from-", URL1)
        
        webpage=requests.get(URL1, headers=HEADERS)
        soup1= BeautifulSoup(webpage.content, "lxml")
        features=soup1.find("div", attrs={'id':'feature-bullets'}).findAll("li")
        
        featstr=''
        for j in features:
            j=j.string
            j=j.rstrip()
            j=j.lstrip()
            featstr+=j
            featstr+=' '
        lst=extract(featstr)
        price=prices[i]
        price=price.replace(',','')
        price=int(price)
        lst.append(price)
        lstoffeatures.append(lst)
    return names[:6],lstoffeatures

print(feature_extraction())

    
    



