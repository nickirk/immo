import scrapy

class QuotesSpider(scrapy.Spider):
    name = "wg-gesucht"
    start_urls = [
                'https://www.wg-gesucht.de/1-zimmer-wohnungen-und-wohnungen-in-Muenchen.90.1+2.1.0.html?csrf_token=cce1ccca47e7b55b5cbd51144ec0dac1f5e7b4a8&offer_filter=1&city_id=90&sort_order=0&noDeact=1&dFr=1688238000&categories%5B%5D=1&categories%5B%5D=2&rent_types%5B%5D=0&sMin=25&rMax=1500',
            ]

    def parse(self, response):
        for quote in response.css('h3.truncate_title a::attr(href)').extract():
            if 'airbnb.pvxt.net' in quote or 'housinganywhere.com' in quote or 'roomlessrent' in quote or 'asset_id' in quote:
                pass
            else:
                yield {
                    "data-id": quote
                        }
