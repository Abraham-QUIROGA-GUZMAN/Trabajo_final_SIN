from twisted.internet import reactor 
from twisted.internet.task import LoopingCall 
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider



class ExtractorClima(Spider):
    name = "MiCrawlerDeClima"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 20,
        'LOG_ENABLED': True 
    }


    start_urls = [
        "https://www.accuweather.com/es/bo/la-paz/33655/weather-forecast/33655",
        "https://www.accuweather.com/es/bo/cochabamba/32716/weather-forecast/32716",
        "https://www.accuweather.com/es/bo/oruro/34377/weather-forecast/34377"
    ]

    def parse(self, response):
        ciudad = response.xpath('//h1/text()').get()
        current = response.xpath('//div[contains(@class, "cur-con-weather-card__panel")]//div[@class="temp"]/text()').get()
        real_feel = response.xpath('//div[contains(@class, "cur-con-weather-card__panel")]//div[@class="real-feel"]/text()').get()

        
        ciudad = ciudad.replace('\n', '').replace('\r', '').strip()
        current = current.replace('°', '').replace('\n', '').replace('\r', '').strip()
        real_feel = real_feel.replace('RealFeel®', '').replace('°', '').replace('\n', '').replace('\r', '').strip()
        
        
        f = open("./datos_clima_scrapy.docx", "a")
        f.write(ciudad + "," + current + "," + real_feel + "\n")
        f.close()
        print(ciudad)
        print(current)
        print(real_feel)
        print()

runner = CrawlerRunner()
task = LoopingCall(lambda: runner.crawl(ExtractorClima)) 
task.start(20) 
reactor.run()
