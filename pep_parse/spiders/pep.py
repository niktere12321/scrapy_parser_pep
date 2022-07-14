import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_peps = response.css('a[href^="/pep-"]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('title::text').get()
        page_title = page_title.replace('| peps.python.org', '').split('–')
        data = {
            'number': page_title[0].split()[-1],
            'name': page_title[-1].strip(),
            'status': response.css('dt:contains("Status") + dd::text').get(),
        }
        yield PepParseItem(data)
