fetch('https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=447&s=0&pp=25')
response.css('div.price-member').extract_first()
response.css('div.price-member > div').extract_first()
response.css('div.price-member > div::text').extract()
response.css('div.price-member > div').extract_first()
response.css('div.price-member > div::attr(data-bind)').extract_first()
response.css('div.price-member > div::attr(data-bind)').extract()
len(response.css('div.price-member > div::attr(data-bind)').extract())
response.css('div.price').extract()
len(response.css('div.price > div::attr(data-bind)').extract())
clear
len(response.css('div.price-member > div::attr(data-bind)').extract())
response.css('div.price-member > div::attr(data-bind)').extract_first()
response.css('div.side > div.price::attr(data-bind)').extract_first()
response.css('div.side > div.price::text').extract_first()
response.css('div.side > div.price::attr(data-bind)').extract_first()
len(response.css('div.side > div.price::attr(data-bind)').extract())
response.css('div.side > div.price::attr(data-bind)').extract_first().split(' ')[2]
response.css('div.side > div.price::attr(data-bind)').extract_first().split(' ')[2].split('.')[0]
response.css('div.side > div.price::attr(data-bind)').extract_first()
response.css('div.price-member > div::attr(data-bind)').extract_first()
%histoclea
%history -f scrapy02.py
response.css('div.price-member > div::attr(data-bind)').extract_first()
response.css('div.side > div.price::attr(data-bind)').extract_first()
response.css('div.price-member > div::attr(data-bind)').extract_first()[11:16]
response.css('div.price-member > div::attr(data-bind)').extract_first()[12:16]
%history -f scrapy02.py
