Tech News - Busca de Notícias sobre Tecnologia 📰🔍
Bem-vindo ao repositório do Tech News, um projeto desenvolvido como parte do curso da Trybe! Aqui você encontrará uma aplicação que realiza a busca de notícias sobre tecnologia, além de outras funcionalidades relacionadas.
![image](https://github.com/Mixchelle/python-projeto-tech-news/assets/110858556/45dbb35b-41b4-4f56-be1d-f83c0e1fd374)

Funcionalidades Implementadas 🚀
1. Função fetch
A função fetch é responsável por realizar uma requisição HTTP ao site e obter o conteúdo HTML da página.
Ela respeita um Rate Limit de 1 requisição por segundo para evitar problemas de sobrecarga no servidor.
Caso a requisição seja bem sucedida com Status Code 200 (OK), retorna o conteúdo HTML da resposta.
Caso a resposta tenha um código de status diferente de 200, retorna None.
Caso a requisição não receba resposta em até 3 segundos, a função retorna None.
2. Função scrape_updates
A função scrape_updates faz o scrape da página Novidades do blog da Trybe para obter as URLs das páginas de notícias.
Retorna uma lista contendo as URLs das notícias listadas nos cards da página Novidades.
A função exclui a notícia em destaque da primeira página para evitar duplicatas.
3. Função scrape_next_page_link
A função scrape_next_page_link realiza o scrape da página Novidades para obter o link da próxima página.
Retorna a URL da próxima página de notícias.
Caso não encontre o link da próxima página, a função retorna None.
4. Função scrape_news
A função scrape_news faz o scrape do conteúdo HTML da página de uma única notícia.
Retorna um dicionário contendo informações relevantes sobre a notícia, como título, URL, data, autor, tempo de leitura, resumo e categoria.
5. Função get_tech_news
A função get_tech_news busca as últimas n notícias sobre tecnologia no site da Trybe.
Utiliza as funções fetch, scrape_updates, scrape_next_page_link e scrape_news para buscar e processar as notícias.
Insere as notícias no banco de dados MongoDB e retorna as mesmas notícias.
6. Classe ReadingPlanService
A classe ReadingPlanService coleta as notícias do banco de dados e as organiza em agrupamentos "readable" e "unreadable".
As notícias "readable" são divididas em subgrupos com somas de tempos de leitura menores que o tempo disponível para leitura.
7. Função search_by_title
A função search_by_title busca notícias no banco de dados por título.
Retorna uma lista de tuplas contendo o título e a URL das notícias encontradas.
A busca é case insensitive.
8. Função search_by_date
A função search_by_date busca notícias no banco de dados por data.
Recebe uma data no formato ISO AAAA-mm-dd como parâmetro.
Retorna uma lista de tuplas contendo o título e a URL das notícias encontradas.
A busca é case insensitive.
9. Função search_by_category
A função search_by_category busca notícias no banco de dados por categoria.
Recebe o nome completo da categoria como parâmetro.
Retorna uma lista de tuplas contendo o título e a URL das notícias encontradas.
A busca é case insensitive.
Requisitos Bônus ✔️
10. Função top_5_categories
A função top_5_categories lista as cinco categorias com maior ocorrência no banco de dados.
Calcula a "popularidade" de cada categoria com base no número de ocorrências.
As categorias são retornadas em uma lista, ordenadas da mais popular para a menos popular.
Em caso de empate, a ordenação é feita por ordem alfabética de categoria.
Caso haja menos de cinco categorias no banco de dados, são retornadas todas as categorias existentes.
Caso não haja categorias disponíveis, a função retorna uma lista vazia.
Como Executar o Projeto 🏃‍♂️
Clone o repositório em sua máquina local.
Certifique-se de ter o Python 3 instalado.
Instale as dependências do projeto:
Copy code
pip install -r requirements.txt
Certifique-se de ter o MongoDB instalado e rodando. Você pode usar o Docker para executar o MongoDB através do arquivo docker-compose.yml.
Para popular o banco de dados com as notícias, execute o comando:
mathematica
Copy code
python3 -m tech_news.scraper get_tech_news N
Substitua N pelo número de notícias que deseja buscar.
Para executar a interface de busca das notícias, utilize a CLI:
Copy code
tech-news-analyzer
Observações 📝
Lembre-se de que este projeto é apenas uma simulação e as notícias podem não ser reais. O scraper está configurado para funcionar corretamente com o blog da Trybe, mas pode ser necessário ajustá-lo para outros sites.

Obrigado por utilizar o Tech News para buscar notícias sobre tecnologia! Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato. Bom uso! 😃🚀
