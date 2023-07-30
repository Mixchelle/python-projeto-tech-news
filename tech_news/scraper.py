import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {
        "user-agent": "Fake user-agent"
    }

    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None
    except requests.RequestException:
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    news_urls = []
    selector = Selector(text=html_content)
    news_cards = selector.css(".entry-title")
    for card in news_cards:
        url = card.css('a::attr(href)').get()
        if url:
            news_urls.append(url)
    if news_urls and selector.css(".entry-title").css('.highlighted'):
        news_urls.pop(0)
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_link = selector.css('a.next::attr(href)').get()

    return next_page_link


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
