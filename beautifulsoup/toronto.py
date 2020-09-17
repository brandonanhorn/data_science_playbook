from bs4 import BeautifulSoup
import requests

url = 'https://toronto.craigslist.org/d/apts-housing-for-rent/search/apa'
r = requests.get(url)
html = r.text

soup = BeautifulSoup(html)

one = soup.find('li', class_='result-row')

def parse_listing(one):
    price = float(one.find('span', class_='result-price').text.replace('$', ''))
    title = one.find('a', class_='result-title hdrlnk').text
    link = one.find('a', class_='result-title hdrlnk').attrs['href']
    try:
        rooms = int(one.find('span', class_='housing').text.strip().split(' -\n')[0][0])
    except AttributeError:
        rooms = None
    listing = {
        'title': title,
        'price': price,
        'rooms': rooms,
        'link': link
    }
    return listing

parse_listing(one)

raw_listings = soup.find_all('li', class_='result-row')
listings = [parse_listing(li) for li in raw_listings]

import pandas as pd

df = pd.DataFrame(listings)
df





#
