#In the name of God
#challenge 1
from bs4 import BeautifulSoup
import requests
import wget
import re
inputted = input("please enter a url to download: ")


response = requests.get(inputted)
response_text = response.text

soup = BeautifulSoup(response_text,"html.parser")

parsed_links = soup.find_all(name="li",class_="menu-item-link link")

link = None
for parse in parsed_links:
    if(str(parse).__contains__("720")):
        link = parse
else:
    for parse in parsed_links:
        if(str(parse).__contains__("360")):
            link = parse
    else:
        link = parsed_links[0]

pattern = "href=\"(.+)\" "
parsed_link = re.findall(pattern, str(link))
url_parsed = parsed_link[0]

def bar_custom(current, total, width=80):
    print("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

wget.download(url_parsed,bar=bar_custom)
