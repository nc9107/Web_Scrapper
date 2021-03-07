import scrapy

class TripAdvisorItem(scrapy.Item):
    place_name = scrapy.Field()
    place_star_rating = scrapy.Field()
    place_price = scrapy.Field()
    place_mage_link = scrapy.Field()
    place_popularity = scrapy.Field()
