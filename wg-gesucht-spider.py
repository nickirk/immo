import scrapy

class QuotesSpider(scrapy.Spider):
    name = "wg-gesucht"
    start_urls = [
                  'https://www.wg-gesucht.de/wg-zimmer-in-Berlin.8.0.1.0.html?user_filter_id=3881821&offer_filter=1&city_id=8&noDeact=1&sMin=15&wgSea=2&wgAge=28&img_only=1&ot=85079%2C163&categories%5B0%5D=0&rent_types%5B0%5D=2',
                #   'https://www.wg-gesucht.de/wg-zimmer-in-Berlin.8.0.1.0.html?user_filter_id=3881691&offer_filter=1&city_id=8&noDeact=1&radLat=52.5128597&radLng=13.424018242594&sMin=15&radAdd=An+der+Michaelbr%C3%BCcke+3%2C+Berlin%2C+Deutschland%2C+10179&radDis=2000&wgSea=2&wgAge=28&img_only=1&categories%5B0%5D=0&rent_types%5B0%5D=2',
            ]

    def parse(self, response):
        for quote in response.css('h3.truncate_title a::attr(href)').extract():
            if not 'airbnb.pvxt.net' in quote:
                yield {
                    "data-id": quote
                        }
