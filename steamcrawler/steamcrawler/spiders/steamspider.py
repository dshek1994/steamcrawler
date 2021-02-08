import scrapy

class SteamSpider(scrapy.Spider):
    name = "profiles"
    start_urls = [
        'https://steamcommunity.com/id/dsdude233max/',
    ]

    def parse(self, response):
        yield {
            'alias': response.xpath("//span[@class='actual_persona_name']/text()").get(),
            'avatar': response.xpath("//div[@class='playerAvatarAutoSizeInner']//img/@src").get(),
            'friend_link': response.xpath("//div[@class='profile_friend_links profile_count_link_preview_ctn responsive_groupfriends_element']//@href").get(),
        }

        url = response.xpath("//div[@class='profile_friend_links profile_count_link_preview_ctn responsive_groupfriends_element']//@href").get()
        yield scrapy.Request(url, callback = self.parseFriends)
    
    def parseFriends(self, response):
        friend_urls = response.xpath("//div[@class='friends_container']//@href").getall()
        
        for url in friend_urls:
            yield scrapy.Request(url, callback = self.parse)
        # yield {
        #     'friends': response.xpath("//div[@class='friends_container']//@href").getall()
        # }



    # def parse(self, response):
    #     with open('profile.html', 'wb') as html_file:
    #         html_file.write(response.body)