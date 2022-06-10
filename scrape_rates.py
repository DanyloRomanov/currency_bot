import requests
from bs4 import BeautifulSoup

URL = "https://kurs.com.ua/#main_table"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
rates = soup.find_all('div', class_='course')

currency_to_index = {
    'usd': [0, 1, 2, 3],
    'euro': [4, 5, 6, 7],
    'gbp': [47, 48, 49, 50]
}


def get_rate_for_currency(currency):
    indexes = currency_to_index[currency]
    banks_buy_rate = rates[indexes[0]].text.split('\n')[0]
    banks_sell_rate = rates[indexes[1]].text.split('\n')[0]
    banks_commercial_rate = rates[indexes[2]].text.split('\n')[0]
    nbu_rate = rates[indexes[3]].text.split('\n')[0]

    usd_rate = f'''The currency for {currency.upper()} at the moment is:
    buy for {banks_buy_rate},
    sell for {banks_sell_rate},
    commercial for {banks_commercial_rate},
    official NBU {nbu_rate}'''

    return usd_rate


