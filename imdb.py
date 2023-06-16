import scrapy

# .titleColumn - pega a caixa com nome e ano do filme
# .titleColumn a - pega o nome do filme
# .secondaryInfo - Anos
# strong - avaliação

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/top/"]

    def parse(self, response):
        for index, filmes in enumerate(response.css('.titleColumn')):
            yield {
                'titulo': filmes.css('.titleColumn a ::text').get(),
                'ano': filmes.css('.secondaryInfo ::text').get()[1:-1],
                'avaliacao': response.css('strong ::text')[index].get()
            }

        pass
