from tech_news.database import db


# Requisito 10
def top_5_categories():
    # Busca todas as notícias no banco de dados
    all_news = db.news.find()

    # Cria um dicionário para contar a ocorrência de cada categoria
    category_count = {}
    for news in all_news:
        categories = news.get("categories", [])
        for category in categories:
            category_count[category] = category_count.get(category, 0) + 1

    # Ordena as categorias por popularidade (número de ocorrências) e em ordem alfabética
    sorted_categories = sorted(category_count.items(), key=lambda x: (-x[1], x[0]))

    # Retorna as cinco categorias mais populares
    return [category for category, _ in sorted_categories[:5]]

