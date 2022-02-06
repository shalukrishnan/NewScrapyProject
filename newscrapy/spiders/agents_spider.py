import scrapy 


class AgentsSpider(scrapy.Spider):
    name = "agents"
    

    start_urls = [
        'https://www.bhhsamb.com/agents?page=1/',
        'https://www.bhhsamb.com/agents?page=2/'

    ]
        



    def parse(self, response):

        #page = response.url.split('/')[-1]
        #filename = 'agents-%s.html' % page
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        #self.log(f'Saved file{filename}') 

        for quote in response.css('div.row'):
            yield {
                'agent-name': quote.css('div.agent-name::text').get(),
                'agent-title': quote.css('div.agent-title::text').get(),
                'agent-email': quote.css('div.agent-email::text').getall(),
                'agent-numbers': quote.css('div.agent-numbers::text').getall(),

            }


        next_page = response.css('li.pagelink a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)    
                 


    