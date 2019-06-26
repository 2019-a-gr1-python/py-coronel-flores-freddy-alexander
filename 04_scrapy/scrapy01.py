type(response)
type(response.css('title'))
clear
response.xpath('html/head/title')
type(response.xpath('html/head/title'))
rescleawr
clear
type(response.css('title').extract())
response.css('title').extract()
response.css('title').extract()[0]
response.css('.quote').extract()[0]
response.css('.quote > .text').extract()[0]
type(response.css('.quote').extract()[0])
response.css('.quote').extract_first()
%history -f scrapy01.py
response
clear
response.xpath('//span').extract()
response.xpath('//text').extract()
%history -f scrapy01.py
clear
clear
response.xpath("//span[contains(@class,'text')]").extract_first()
response.xpath("//span[contains(@class,'text')]/text()").extract_first()
response.xpath("//span[contains(@class,'tag')]/text()").extract()
response.xpath("//span[contains(@class,'tag')])").extract()
response.xpath("//span[contains(@class,'tag-item')]").extract()
response.xpath("//span[contains(@class,'tag-item')]/text()").extract()
response.xpath("//span[contains(@class,'tag-item')]").extract()
response.xpath("//a[contains(@class,'tag')]").extract()
response.xpath("//span[contains(@class,'tag-item')]").extract()
response.css(".tag-item > .tag").extract()
response.css(".tag-item > .tag /text()").extract()
response.css(".tag-item > .tag").extract()
response.css(".tag-item > .tag").getall()
response.css(".tag-item > .tag").extract_first()
response.css(".tag-item > .tag::text")
response.css(".tag-item > .tag")
response.css(".tag-item > .tag").extract()
response.css(".tag-item > .tag::text()").extract()
response.css(".tag-item > .tag::text").extract()
response.xpath("//span[contains(@class,'tag-item')]/text()").extract()
response.xpath("//span[contains(@class,'tag-item')]/a[contains(@class,'a')]").extract()
response.xpath("//span[contains(@class,'tag-item')]/a[contains(@class,'a')/text()]").extract()
response.xpath("//span[contains(@class,'tag-item')]/a[contains(@class,'a')]/text()").extract()
response.css(".tag-item > .tag::text").extract()
response.xpath("//span[contains(@class,'tag-item')]/a[contains(@class,'a')]/text()").extract()
%history -f scrapy01.py
response.css(".quote > span > a::text").extract()
response.css(".quote > span > a").extract()
response.css(".quote > span > a:attr('href')").extract()
response.css(".quote > span > a").extract()
response.css(".quote > span > a::attr(href)").extract()
clear
response.css(".quote > span > a::attr(href)").extract()
response.xpath("//div[contains(@class,'quote')]/
"

efd
]
response.css(".quote > span > a::attr(href)").extract()
response.xpath("//div[containst(class,'quote')]/span/a")
response.xpath("//div[containst(@class,'quote')]/span/a").extract()
response.xpath("//div[containst(class,'quote')]/span/a")
response.xpath("//div[containst(@class,'quote')]/span/a")
response.xpath("//div[containst(@class,'quote')]/span/a").extract()
response.xpath("//div[contains(@class,'quote')]/span/a").extract()
response.xpath("//div[contains(@class,'quote')]/span/a::href").extract()
response.xpath("//div[contains(@class,'quote')]/span/a::attr(href)").extract()
response.xpath("//div[contains(@class,'quote')]/span/a::attr(href)").extract()
response.css(".quote > span > a::attr(href)").extract()
response.xpath("//div[contains(@class,'quote')]/span/a/text").extract()
response.xpath("//div[contains(@class,'quote')]/span/a/@src").extract()
response.xpath("//div[contains(@class,'quote')]/span/a/@href").extract()
response.css(".quote > span > a::attr(href)").extract()
response.xpath("//div[contains(@class,'quote')]/span/a/@href").extract()
%history -f scrapy01.py
