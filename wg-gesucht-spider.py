import scrapy

class QuotesSpider(scrapy.Spider):
    name = "wg-gesucht"
    start_urls = [
                  'https://www.wg-gesucht.de/wohnungen-in-Stuttgart.124.2.1.0.html?csrf_token=e2e6f0c444420ad8813a2ec51fc035c303049693&offer_filter=1&sort_column=0&noDeact=1&city_id=124&category=2&rent_type=0&rMax=650&radAdd=70569+Stuttgart%2C+Germany&radDis=4000'
            ]
    def parse(self, response):
        for quote in response.css('div.offer_list_item::attr(data-id)').extract():
            yield {
                "data-id": quote
                    }

