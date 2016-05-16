import scrapy
from swissraces.items import SwissracesItem
from scrapy.http import Request


FILES_STORE = '/Users/vmac/SCRAPY16/swissraces/data/'




class ChSpider(scrapy.Spider):
    name = "swiss"
    allowed_domains = ["http://www.iena.ch"]
    start_urls = [
        "http://www.iena.ch/courses/resultats/archives",
        "http://www.iena.ch/fileadmin/user_upload/Documents/Suisse_Trot/Archives"
    ]

    def save_pdf(self, response):
        url = response.meta['url']
        path = FILES_STORE + '/' + url
        print("path in save pdf %s" % url)  
        with open(path, "wb") as f:
            f.write(response.body)

    def parse(self, response):
        print(response.url)
        # items = []
        
        i = SwissracesItem()
        file_urls = response.xpath("//a[contains(@href, '.pdf')]/@href").extract()
        print(len(file_urls))
        i['file_urls'] = file_urls
        i['file_names'] = file_urls
        # [x.split('/')[-1] for x in file_urls ]
        yield i
        # for url in file_urls:
        #     i = SwissracesItem()
        #     i['file_urls'] = url
        #     i['file_names'] = url.split('/')[-1]
        #     items.append(i)
        # return items


        # file_urls = response.xpath("//a[contains(@href, '.pdf')]/@href").extract()
        # for url in file_urls:
        #     i = SwissracesItem()
        #     i['body'] = response.body
        #     i['url'] = response.url

        # # alt way 
        # file_urls = response.xpath("//a[contains(@href, '.pdf')]/@href").extract()
        # for url in file_urls:
        #     with open(path, "wb") as f:
        #         f.write(response.body)
        #     return item    
            # request = Request(url, callback=self.save_pdf)
            # request.meta['url'] = url
            # yield request
            



        # # get all as with href containing .pdf
        # file_urls = response.xpath("//a[contains(@href, '.pdf')]/@href").extract()
        # i['file_urls'] = file_urls
        # print(len(file_urls))
        # return i

        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)