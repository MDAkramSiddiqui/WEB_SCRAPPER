import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook 
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = None
ctx.verify_mode = ssl.CERT_NONE

url = 'https://news.ycombinator.com/'

fhand = urllib.request.urlopen(url, context=ctx).read()
raw_html = BeautifulSoup(fhand, 'html.parser')

items = raw_html.findAll("tr", {"class" : "athing"});
subtext = raw_html.findAll("td", {"class" : "subtext"})

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("News Sheet")

sheet.write(0, 0, 'HEADING')
sheet.write(0, 1, 'SCORE')
sheet.write(0, 2, 'TIME')
sheet.write(0, 3, 'AUTHOR')
sheet.write(0, 4, 'LINK')


for i in range(len(items)):
    heading_container = items[i].find("a", {"class" : "storylink"})
    _heading = heading_container.text
    _heading_link = heading_container.get("href")


    _heading_author = subtext[i].a.text
    score_container = subtext[i].find("span", {"class" : "score"})
    _heading_score = score_container.text
    age_container = subtext[i].find("span", {"class" : "age"})
    _heading_age = age_container.a.text

    print(_heading)
    print(_heading_score)
    print(_heading_age)
    print(_heading_author)
    print(_heading_link + "\n")

    sheet.write(i+1, 0, _heading)
    sheet.write(i+1, 1, _heading_score)
    sheet.write(i+1, 2, _heading_age)
    sheet.write(i+1, 3, _heading_author)
    sheet.write(i+1, 4, _heading_link)

    
workbook.save('News.xls')
