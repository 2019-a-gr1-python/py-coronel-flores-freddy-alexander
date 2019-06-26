fetch('https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=447&s=0&pp=25')


product_names = response.css('.product-tile-inner > .name::text').extract()
product_names
import numpy as np
product_names = np.array(product_names)
product_names

precio_original = list(map(lambda x: x.split(')')[0][12:] , response.css('div.side > div.price::attr(data-bind)').extract()))
precio_original
len(precio_original)
precio_original = np.array(precio_original,dtype='float32')
precio_original


precio_descuento = list( map(lambda x: x.split(')')[0][12:],response.css('div.price-member > div::attr(data-bind)').extract()))
precio_descuento
precio_descuento = np.array(precio_descuento,dtype='float32')
precio_descuento
descuentos = precio_original - precio_descuento

descuentos

producto_mayor_Descuento = product_names[descuentos==descuentos.max()]
producto_mayor_Descuento

precio_original[product_names==producto_mayor_Descuento[0]] 

precio_descuento[product_names==producto_mayor_Descuento[0]]  
%history -f deber.py
