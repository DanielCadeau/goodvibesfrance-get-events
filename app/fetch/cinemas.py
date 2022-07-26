import requests

async def fetch(city):
    url1 = "https://data.culture.gouv.fr/api/records/1.0/search/?dataset=etablissements-cinematographiques&q=&facet=unite_urbaine&refine.unite_urbaine=" + city.capitalize()
    url2 = "https://data.culture.gouv.fr/api/records/1.0/search/?dataset=etablissements-cinematographiques&q=&facet=commune&refine.commune=" + city.capitalize()
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    if response1.status_code == 200 and response2.status_code == 200:
        data = response1.json()
        data2 = response2.json()
        data["records"] += data2["records"]
        return data
    elif response1.status_code == 200:
        data = response1.json()
        return data
    elif response2.status_code == 200:
        data = response2.json()
        return data
    return 401