import os
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

src = 'https://coinmarketcap.com/'


def get_soup_from_url(url, browser):
    browser.get(url)
    return BeautifulSoup(browser.page_source, 'html.parser')


def get_browser():
    current_location = os.getcwd()
    return webdriver.Chrome(current_location + '/drivers/chromedriver')


def export_to_csv(data, headers):
    df = pd.DataFrame(data, columns=headers)
    export_dir = 'exports/'
    df.to_csv(export_dir + 'cmc_data.csv', index=False)


if __name__ == '__main__':
    browser = get_browser()
    browser.set_window_size(1920, 1080)
    data = []
    headers = ['#', 'Name', 'Market Cap', 'Price',
               'Volume (24h)', 'Circulating Supply', 'Change (24h)']
    soup = get_soup_from_url(src, browser)

    rows = soup.find_all('tr')
    rows = rows[3:]
    for row in rows:
        cols = row.find_all('td')
        cols = cols[:-2]
        row_data = [col.get_text() for col in cols]
        data.append(row_data)
    browser.close()
    export_to_csv(data, headers)
