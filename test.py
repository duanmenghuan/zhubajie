import requests
from lxml import etree

url = "https://qhd.zbj.com/search/f/?kw=cms"
resp = requests.get(url)
html = etree.HTML(resp.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]")
for div in divs:
    jiage = div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')
    biaoti = div.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[2]/div[2]/div[2]/p/text()')
    mingcheng = div.xpath('//*[@id="utopia_widget_76"]/a[1]/div[1]/p/text()')
    print(mingcheng)




