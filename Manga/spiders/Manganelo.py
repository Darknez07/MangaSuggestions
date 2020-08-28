# -*- coding: utf-8 -*-
import scrapy


class ManganeloSpider(scrapy.Spider):
    name = 'Manganelo'
    allowed_domains = ['manganelo.com']
    start_urls = ['http://manganelo.com/']

    def parse(self, response):
        for name in response.xpath("//div[@class='content-homepage-item-right']"):
            link = name.xpath("//a[@class='content-homepage-more a-h']/@href").get()
            yield scrapy.Request(url=link, callback=self.parse_on,
                                 headers={
                                     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                                 })
    def parse_on(self, response):
        for manga in response.xpath("//div[@class='genres-item-info']"):
            final = dict({
                'Name': manga.xpath("./h3/a/text()").get(),
                'Latest Chapter': manga.xpath("./a[1]/text()").get(),
                'Dated Released' : manga.xpath("./p/span[2]/text()").get()
            })
            yield scrapy.Request(url=manga.xpath("./h3/a/@href").get(),
                                 callback=self.continued,meta=final)
        yield scrapy.Request(url=response.xpath("//div[@class='group-page']//a/@href").getall()[-2],
                            callback=self.parse_on,
                            headers={
                                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                            })
    def continued(self, response):
        # p = len(response.xpath("//table[@class='variations-tableInfo']//tr").getall())
        final = response.request.meta
        final['Link'] = response.request.url
        final['Genre'] = []
        for resp in response.xpath("//table[@class='variations-tableInfo']"):
            for i in resp.xpath(".//td[@class='table-value']"):
                if i.xpath("./text()").get() not in [None,'\n','']:
                        final['Status'] = i.xpath("normalize-space(./text())").get()
        for tableinf in response.xpath("//div[@class='story-info-right-extent']"):
                final['Rating']= tableinf.xpath(".//em[@property='v:average']/text()").get()
        for tabs in response.xpath("//table//i[@class='info-genres']//following::td/a"):
            final['Genre'].append(tabs.xpath("./text()").get())
        final['img-link'] = response.xpath("//span[@class='info-image']/img/@src").get()
        return final