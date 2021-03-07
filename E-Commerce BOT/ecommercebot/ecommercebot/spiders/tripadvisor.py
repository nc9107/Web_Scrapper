# import scrapy
# from selenium.webdriver.common.keys import Keys
# import selenium
# from ..items import TripAdvisorItem
#
# driver = webdriver.Chrome('C:\\Users\\nisha\Downloads\\chromedriver_win32\\chromedriver')
#
# class TripadvisorSpider(scrapy.Spider):
#     name = 'tripadvisorbot'
#     allowed_domains = ['https://www.tripadvisor.com/']
#
#     url = 'https://www.tripadvisor.com/'
#     driver.get('https://www.tripadvisor.com/')
#     user_input = input("What place are you looking to explore?")
#     things_to_do = driver.find_element_by_xpath('//*[@id="lithium-root"]/main/div[1]/div[2]/div/div/div[3]/a')
#     things_to_do.send_keys(user_input)
#     things_to_do.send_keys(Keys.RETURN)
#     new_url = driver.current_url
#     start_urls = [new_url]
#
#     def parse(self, response):
#
#
#
#         driver.close()
