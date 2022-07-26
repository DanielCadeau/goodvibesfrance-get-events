import requests
from pprint import pprint
from xml.etree import ElementTree

async def fetch():
    url = "https://www.touslesfestivals.com/rss"
    data = get_feed(url)
    return {
        "hits": len(data),
        "festivals": data,
    }

def get_source(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
    except requests.exceptions.RequestException as e:
        pprint(e)

def get_feed(url):
    response = get_source(url)
    festivals = []
    if response:
        xml = ElementTree.fromstring(response.content)
        for item in xml.findall("channel/item"):
            title = item.find("title").text
            link = item.find("link").text
            guid = item.find("guid").text
            description = item.find("description").text
            pub_date = item.find("pubDate").text
            festivals.append({"title": title, "link": link, "description": description, "pub_date": pub_date, "guid": guid})
    return festivals