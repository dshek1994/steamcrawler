import scrapy

class SteamSpider(scrapy.Spider):
    name = "profiles"
    start_url = [
        'https://steamcommunity.com/id/dsdude233max/',
    ]

    def parse(self, response):
        with open('profile.html', 'wb') as html_file:
            html_file.write(response.body)