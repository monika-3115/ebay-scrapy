import scrapy


class EbayScrapperSpider(scrapy.Spider):
    name = "ebay_scrapper"
    allowed_domains = ["www.ebay.com"]
    start_urls = ["https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=2",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=3",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=4",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=5",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=6",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=7",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=8",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=9",
                  "https://www.ebay.com/b/Vision-Care-Products/31414/bn_1865451?rt=nc&_pgn=10",
                ]

    def parse(self, response):
        PRODUCT_SELECTOR = "li.s-item.s-item--large"
        IMAGE_SELECTOR = "img.s-item__image-img::attr('src')"
        NAME_SELECTOR = "h3.s-item__title::text"
        PRICE_SELECTOR = "span.s-item__price::text"
        # NEXT_SELECTOR = ""

        for product in response.css(PRODUCT_SELECTOR):
            yield{
                "image" : product.css(IMAGE_SELECTOR).extract_first(),
                "product_name" : product.css(NAME_SELECTOR).extract_first(),
                "price" : product.css(PRICE_SELECTOR).extract_first()
            }
        
        # next_page = response.css(NEXT_SELECTOR).extract_first()
        # if next_page:
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #     )   





