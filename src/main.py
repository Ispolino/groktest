import datetime
import time
import requests
from bs4 import BeautifulSoup
from src.database import db_price
from src.config import settings
from logs import getLogger

logger = getLogger(__name__)


def save_db(data):
    db_price.insert_one(data)
    logger.debug("add data to db")


def get_price(html):
    price = html.find("div", attrs={"class": "amount"})
    btc_price = price.text.strip()
    logger.info(f"get btc price: {btc_price}")

    save_db({
        "time": datetime.datetime.now(),
        "price": btc_price
    })
    return price


def get_page(url: str, headers: str):
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            logger.info(f"get status code: {response.status_code}")
            soup = BeautifulSoup(response.content, "lxml")
            return soup

    except Exception as e:
        logger.error(e)
        logger.exception(e)


def main():
    while True:
        url = settings.URL
        headers = {
            'accept-language': 'uk,en-US;q=0.9,en;q=0.8,ru;q=0.7',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_0) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/47.0.1181.360 Safari/603'
        }
        page = get_page(url, headers)
        get_price(page)

        time.sleep(int(settings.INTERVAL))


if __name__ == "__main__":
    main()
