# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class FiltrarSoloTabletas(object):

    def process_item(self, item, spider):
        print("que se yo item")
        print(item)
        
        titulo = item['titulo']
        #print("que se yo item")
        #print(item)
        if 'capsula' not in titulo:
            raise DropItem('No tiene capsula en el titulo')
        
        else:
            return item


class TransformarTituloMinusculas(object):
    def process_item(self,item,spider):
        item['titulo'] = item['titulo'].lower() 




