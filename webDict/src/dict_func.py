from bs4 import BeautifulSoup
import requests as rq
import urllib3

def yahoo(cb):
    url = "https://hk.dictionary.search.yahoo.com/search?p={}".format(cb)

    http = urllib3.PoolManager()
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    headers = { 'User-Agent' : user_agent }

    # creating request
    req = http.request('GET',url,headers=headers)
    soup = BeautifulSoup(req.data.decode('utf-8'), "lxml")

    defination = ""
    pural = None

    lis = soup.select("div > ul > .lh-22")
    for li in lis:
        divs = li.find_all("div")
        for div in divs:
            text = div.text.strip()
            if text.endswith("複數"):
                pural = text.split('的')[0]
            defination += text
            defination += "\t"

        defination += "\n"

    if pural is not None:
        defination += yahoo(pural)

    return defination


def howjsay(word):
    url = "https://howjsay.com/how-to-pronounce-{}".format(word)

    http = urllib3.PoolManager()
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    headers = { 'User-Agent' : user_agent }

    # creating request
    req = http.request('GET',url,headers=headers)
    soup = BeautifulSoup(req.data.decode('utf-8'), "lxml")

    audio_source = ""
    source = soup.select("source")
    if len(source) > 0:
        audio_source = source[0]['src']

    return audio_source

