from tech_news.database import db
from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    result = db.news.find(query)
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    query = {"timestamp": formatted_date}
    result = db.news.find(query)
    return [(news["title"], news["url"]) for news in result]


# Requisito 9
def search_by_category(category):
    result = search_news({"category": {"$regex": category, "$options": "i"}})
    news_list = [(new["title"], new["url"]) for new in result]
    return news_list
