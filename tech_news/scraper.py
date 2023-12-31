import requests
import time
from parsel import Selector
from tech_news.database import create_news
from itertools import islice


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
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-header-inner h1.entry-title::text") \
        .get().strip()
    timestamp = selector.css("ul.post-meta li.meta-date::text") \
        .get()
    writer = selector.css("ul.post-meta li.meta-author span.author a::text") \
        .get()
    reading_time = int(
        selector.css("ul.post-meta li.meta-reading-time::text")
        .re_first(r"\d+")
    )
    summary = "".join(
        selector.css("div.entry-content > p:first-of-type *::text").getall()
    ).strip()
    category = selector \
        .css(".meta-category a.category-style span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    base_url = "https://blog.betrybe.com/"
    news_urls = []
    while len(news_urls) < amount:
        html_content = fetch(base_url)
        if not html_content:
            break
        news_urls.extend(scrape_updates(html_content))
        base_url = scrape_next_page_link(html_content)

    news_content = []
    for url in islice(news_urls, amount):
        news_html = fetch(url)
        if not news_html:
            continue
        news_data = scrape_news(news_html)
        news_content.append(news_data)

    create_news(news_content)
    return news_content
