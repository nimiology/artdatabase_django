import numpy
from art.models import Art
import bs4
import requests
def erw(pagenumb):
    req = requests.get(
        f'https://www.wga.hu/cgi-bin/search.cgi?author=&time=any&school=any&form=any&type=any&title=&comment=&location=&from={pagenumb}&max=20&format=1')
    html = req.text
    bs = bs4.BeautifulSoup(html, 'html.parser')
    list_tr = bs.findAll('tr')
    for artnum in range(2, len(list_tr) - 1):
        if artnum % 2 == 0:
            v1 = list_tr[artnum]
            v2 = list_tr[artnum]
            v3 = list_tr[artnum]
            v4 = list_tr[artnum]
            v5 = list_tr[artnum]
            v6 = list_tr[artnum]
            Art(painter=v1.find_all('td')[1].find('b').text,
                title=v2.find_all('td')[1].text.split('\n')[2],
                picture='https://www.wga.hu' + v3.find('a').get('href'),
                year=v4.find_all('td')[1].text.split('\n')[3],
                type=v5.find_all('td')[1].text.split('\n')[4],
                location=v6.find_all('td')[1].text.split('\n')[5]).save()
for page in numpy.arange(0, 51459, 20):
    print(page)
    erw(page)