import scrapy
from scrapy.spiders import CrawlSpider, Rule
"""from scrapy.linkextractors import LinkExtractor

from scrapy_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_fydeca'  # Heredado (conservar nombre)
    
    allowed_domains = [  # Heredado (conservar nombre)
        'fybeca.com'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf'
    ]


    



  
    
   # todos los links con cat=238

   rules = (
       Rule(LinkExtractor(allow=('cat=238')),callback='parse_item')
   ) 


    def parse_page(self, response):
        productos = response.css('div.product-tile-inner')
       # print("que se yo")
        #print(f" hola {len(productos)}")
        for producto in productos:
            existe_producto = len(producto.css('div.detail'))
            print(f"existe producto? {existe_producto}")
            if existe_producto>0:
                with open('prueba.txt','a+') as f:
                    f.write(producto.extract())

                producto_loader= ItemLoader(
                    item=ProductoFybeca(),
                    selector=producto
                )

                producto_loader.default_output_processor = TakeFirst() 
                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                    )

                
                
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'

                )

                yield producto_loader.load_item()
                """