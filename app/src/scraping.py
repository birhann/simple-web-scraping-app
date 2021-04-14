import requests
from bs4 import BeautifulSoup


def getProductInfo(productLink):
    source = requests.get(productLink).text
    soup = BeautifulSoup(source, "html.parser")

    name = soup.find('meta', {"property": "og:title"})[
        'content']
    img = soup.find('div', {"class": "image-carousel-container"}).img['src']
    price = soup.find('meta', {"property": "etsymarketplace:price_value"})[
        'content']
    priceSymbol = soup.find('meta', {"property": "etsymarketplace:currency_symbol"})[
        'content']
    description = soup.find('meta', {"property": "og:description"})[
        'content'][0:499]
    return {
        'name': name,
        'img': img,
        'price': price,
        'price_symbol': priceSymbol,
        'description': description
    }
