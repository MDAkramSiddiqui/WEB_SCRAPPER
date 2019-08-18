import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = None
ctx.verify_mode = ssl.CERT_NONE

url = 'https://news.ycombinator.com/'

fhand = urllib.request.urlopen(url, context=ctx).read()
raw_html = BeautifulSoup(fhand, 'html.parser')

items = raw_html.findAll("tr", {"class" : "athing"});
subtext = raw_html.findAll("td", {"class" : "subtext"})

filename = "newc.xls"
f = open(filename, "w")
headers = "HEADING , SCORE , TIME , AUTHOR , LINK\n"
f.write(headers)

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

    f.write(_heading.replace(",", "-") + "," + _heading_score + "," + _heading_age + "," + _heading_author + "," + _heading_link + "\n")
    
f.close()
