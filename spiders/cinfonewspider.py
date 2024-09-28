from typing import Iterable, Any
from urllib.parse import urljoin
import scrapy
from scrapy import Request
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor

class Cinfonewspider(scrapy.Spider):
    name = "cinfonewspider"

    allowed_domains = ['domain']

    start_urls = ['start url']

    def parse(self, response):
        link_extractor=LinkExtractor(restrict_css='.CMSSiteMapLink')
        links=link_extractor.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url,callback=self.parse_data,meta={'playwright':True})

    def parse_data(self,response):
        cname=response.css('.h2::text').get()
        cphone=response.css('#p_lt_ctl02_pageplaceholder_p_lt_ctl00_TeamHero_linkPhoneBranch::text').get(),
        cemail=response.css('#p_lt_ctl02_pageplaceholder_p_lt_ctl00_TeamHero_linkEmailBranch::text').get()
        caddress=response.css('.address-info.h4 span::text').getall(),
        loanofficer = response.xpath('//div[@id="p_lt_ctl02_pageplaceholder_p_lt_ctl00_TeamMembers_ltTeamMembersWapper"]/ul/li/article/div[2]/header/h3/span/text()').getall(),
        yield {
            'name':cname,
            'phone':cphone,
            'email':cemail,
            'address':caddress,
            'loanofficer':loanofficer,
            'link':response.url


        }

