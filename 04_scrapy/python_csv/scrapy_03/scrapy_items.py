fetch('https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25')
response.flags
response
response
response.css('.product-tile-inner > a')
response.css('.product-tile-inner > a').extract()
response.css('.product-tile-inner > a:text').extract()
response.css('.product-tile-inner > a::text').extract()
response.css('.product-tile-inner > a.name::text').extract()
clear
contenedor = response.css('product-tile-inner')
titulo = contenedor.css('a.name::text')
contenedor.css('div.detail > a.image').extract()
contenedor.css('div.detail > a.image')
contenedor.css('.detail > .image')
contenedor
contenedor
contenedor = response.css('product-tile-inner')
titulo = contenedor.css('a.name::text')
contenedor = response.css('.product-tile-inner')
titulo = contenedor.css('a.name::text')
titulo
clear
contenedor = response.css('.product-tile-inner')
titulo = contenedor.css('a.name::text')
contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src').extract_first()
contenedor.css('div.detail > a.image > #gImg').extract_first()
url = contenedor.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
clear
class ProductoFydeca(scrapy.Item)
clear
class ProductoFydeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field()
first_product = P
class ProductoFydeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field()
clea
clear
class ProductoFydeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field()
first_product = ProductoFydeca()
first_product['titulo'] = titulo.extract_first()
first_product['imagen'] = url.extract_first()
firs_product
first_product
clear
def transformar_url_imagen(texto):
    url = 'https://www.fydeca.com'
    cadena_a_reemplazar= '../..'
    return texto.replace(cadena_a_reemplazar,url)
from scrapy.loader.processors import MapCompose
class ProductoFydeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen) 
    )
first_product = ProductoFydeca()
first_product['titulo'] = titulo.extract_first()
first_product['imagen'] = url.extract_first()
first_product
from scrapy.loader import ItemLoader
il = ItemLoader(item=ProductoFydeca())
il.add_value('titulo',titulo.extract_first())
il.add_value('imagen',url.extract_first())
il.load_item()
pwd
ls
%history -f scrapy_items.py
