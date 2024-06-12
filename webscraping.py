# import base64
# import functions_framework
# import requests
# from bs4 import BeautifulSoup
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

import requests
from bs4 import BeautifulSoup
import functions_framework

@functions_framework.http
def scraping_yahoo(request):
    url = 'https://search.yahoo.co.jp/realtime'

    response = requests.get(url)
    response.raise_for_status()  

    soup = BeautifulSoup(response.content, 'html.parser')

    trend_links = soup.find_all('a', {'data-cl-params': True})

    yahoo_trend_dict = {}

    count = 1

    for link in trend_links:
        article = link.find('article')
        if article:
            trend_name = article.find('h1').get_text(strip=True)
            yahoo_trend_dict[count] = trend_name
            count += 1

    result = "\n".join([f'{key}: {value}' for key, value in yahoo_trend_dict.items()])
    return result
