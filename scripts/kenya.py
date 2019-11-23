# import requests
# import bs4
#
# indexes = []
#
# uri = "http://kenyalaw.org/kl/index.php?id=9091"
#
# content = requests.get(uri)
#
# soup = bs4.BeautifulSoup(content.text)
#
# table = soup.find("table")
#
# rows = []
# for row in table.findAll("tr"):
#     data = {}
#     link = row.find('a')
#     if link:
#         data['link'] = link['href']
#         rows.append(link['href'])


import csv
import requests
from bs4 import BeautifulSoup

indexes = [9091, 7938, 6819, 5991, 5189,
           4250, 4251, 519, 520, 521, 522, 523, 524, 525]



# with open('bills.csv', 'w') as f:
#     writer = csv.writer(f)
#     for index in indexes:
#         url = f"http://kenyalaw.org/kl/index.php?id={index}"
#         print(f"Curent URL : {url}")
#         u = requests.get(url)
#         soup=BeautifulSoup(u.text)
#         for tr in soup.find_all('tr')[1:]:
#                 tds = tr.find_all('td')
#                 row = [elem.text.encode('utf-8') for elem in tds]
#                 writer.writerow(row)


# with open('urls.txt', 'w') as f:
#     for index in indexes:
#         url = f"http://kenyalaw.org/kl/index.php?id={index}"
#         print(f"Curent URL : {url}")
#         u = requests.get(url)
#         soup=BeautifulSoup(u.text)
#         for tr in soup.find_all('tr')[1:]:
#                 tds = tr.find_all('td')
#                 for element in tds:
#                     finder = element.find('a')
#                     if finder:
#                         url = finder['href']
#                         f.writelines(url+'\n')

import urllib.request

with open('urls.txt', 'r') as fil:
    urls = fil.readlines()
    for idx, url in enumerate(urls, start=1):
        if url.startswith("http://kenyalaw.org/kl/"):
            valid = f"http://kenyalaw.org/kl/{url}"
        else:
            valid = url
        print(valid)
        urllib.request.urlretrieve(valid, f'/Users/Olamilekan/Desktop/Machine Learning/OpenSource/crawlers/kenyan_bills/{idx}.pdf')