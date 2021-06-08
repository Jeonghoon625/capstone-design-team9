from flask import Flask, render_template, redirect, request, url_for
import requests
import urllib.request
import pickle
from bs4 import BeautifulSoup
import csv

def Crawler(recipeUrl):
    url = recipeUrl
    
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")

    res = soup.find('div','ready_ingre3')

    try :
        source=[]

        for n in res.find_all('ul'):
            for tmp in n.find_all('li'):
                k = tmp.get_text()
                k = k.split(' \n')[0]
                source.append(k.replace(' ',''))

        s_index=[]

        for a in res.find_all("a"):
            href = a.attrs['href']
            href = href.split('\'')[1]
            s_index.append(href)

        source_dic = {name:value for name, value in zip(source, s_index)}

    except (AttributeError):
            return

    if "닭봉" in source:
        source[source.index("닭봉")] = "닭고기"

    if "달걀" in source:
        source[source.index("달걀")] = "계란"

    if "쪽파또는대파" in source:
        source[source.index("쪽파또는대파")] = "대파"

    with open('Crawl_data.csv', 'w+',newline='') as f: 
        write = csv.writer(f) 
        write.writerow(source)
        
    c_u = open("Crawl_url.csv", 'w+')
    c_u.write(url)

    return source

# source_dic = {}
# source_dic = Crawler("https://www.10000recipe.com/recipe/6940325")
# print(source_dic)
# print(source_dic['우유'])

#with open('Crawl_data.csv', newline="") as csvfile:
    #data_reader = csv.reader(csvfile)
    #csv_data = [row for row in data_reader]
    #print(csv_data[0])

