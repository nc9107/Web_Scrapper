import scrapy
from ..items import EcommercebotItem

#####
"""
Selecting class attributes
CSS: .class_name
XPath: [@class= 'class_name']

Selecting img:
CSS:
XPath:

ID of an element:
CSS:#class_name
XPath: [@id='class_name']

"""

class AmazonbotSpider(scrapy.Spider):
    name = 'amazonbot'
    allowed_domains = ['www.amazon.com']
    your_keyword = input("What do you want to search today?")
    url = 'https://www.amazon.com/s?k={}'.format(your_keyword)
    #start_urls = ['https://www.amazon.com/s?k=shoes&ref=nb_sb_noss_2']
    start_urls = ['https://www.amazon.com/s?k={}'.format(your_keyword)]
    count = 0
    def parse(self, response):
        items = EcommercebotItem()
        product_blocks = response.css('.s-latency-cf-section .sg-col-4-of-20 .sg-col-inner')
        for product in product_blocks:
            product_brand = product.css('.s-line-clamp-1 .a-color-base').css('::text').extract()
            product_name= product.css('.a-color-base.a-text-normal').css('::text').extract()
            product_price = product.css('.a-price-whole::text').extract()
            product_rating = product.css('.aok-align-bottom').css('::text').extract()
            product_link = product.css('.a-link-normal s-no-outline::attr(href)').get()
            items['product_brand'] = product_brand
            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_rating'] = product_rating
            items['product_link'] =  product_link

            yield items

            nextpage = response.css('li.a-last a::attr(href)').get()
            print(nextpage)
            if nextpage is not None:
                yield response.follow(nextpage, callback=self.parse)

# if __name__ == "__main__":
#     print("Welcome to amazon web scrapper")
