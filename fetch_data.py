import requests

wineReviews1 = open('winereviews_html.txt', 'wb')
numberofpages = 2
for pg_no in range(1, numberofpages+1):
    uri = 'http://www.winespectator.com/dailypicks/category/catid/1/page/+str(pg_no)'
    res = requests.get(uri)
    try:
        res.raise_for_status()
        for chunk in res.iter_content(256):
            wineReviews1.write(chunk)
    except Exception as exc:
        print('There was a problem: %s' % (exc))
wineReviews1.close()

from bs4 import BeautifulSoup
wineReviews2 = open('winereviews_html.txt')

WRsoup = BeautifulSoup(wineReviews2, "html.parser")


h5s = WRsoup.find_all('h5',class_ = '')
reviewlst = [h5.text for h5 in h5s]
review_only_lst =[]

for i in range(0,len(reviewlst)):
    WRstring = reviewlst[i].split('\t')
    review_only_lst.append(WRstring[3]+"\n")

with open('Wine Reviews.txt', 'w') as wineReviews3:
    for i in range(len(review_only_lst)):
        wineReviews3.write(review_only_lst[i])

