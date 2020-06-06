import requests,sys
import os as system
import re as regex
from requests.utils import requote_uri as encode

if __name__ == '__main__':
    print("./dork.py \"your dork\".")
    sys.exit(1)

class MyDorker():

    def __init__(self, dork = ''):
        self.dork = encode(dork)
        self.reqs = requests.Session()
        self.token = 'partner-pub-2698861478625135:3033704849'
        self.head = {
            'Referer' : 'https://cse.google.com/cse?cx=' + self.token,
            'User-Agent' : 'Mozilla/5.0 (kompatibel; Googlebot/2.1; +http://www.google.com/bot.html)'
        }
        self.parse_info()

    def parse_info(self):
        text = self.get_info()
        cx = regex.compile(r'"cx": "(.*?)"')
        exp = regex.compile(r'"exp": \["(.*?)"\, "(.*?)"\]')
        cse_token = regex.compile(r'"cse_token": "(.*?)"')
        cselibVersion = regex.compile(r'"cselibVersion": "(.*?)"')
        resultSetSize = regex.compile(r'"resultSetSize": "(.*?)"')
        self.cx = cx.findall(text)
        self.exp = exp.findall(text)
        self.cse_token = cse_token.findall(text)
        self.resultSetSize = resultSetSize.findall(text)
        self.cselibVersion = cselibVersion.findall(text)

    def get_info(self):
        site = 'https://cse.google.com/cse.js?hpg=1&cx='
        reqs = self.reqs.get(url = site + self.token, headers = self.head)
        return reqs.text

    def google_dorker(self):
        iterate = 0
        found_url = []
        parse_found_cseurl = regex.compile(r'"clicktrackUrl": "(.*?)"', regex.I)
        parse_found_targeturl = regex.compile(r'&q=(.*?)&sa')

        while True:

            cse_google = "https://cse.google.com/cse/element/v1?rsz=" + self.resultSetSize[0] + \
            "&num=10&&start=" + str(iterate) + "&hl=en&source=gcsc&gss=.com&cselibv=" + self.cselibVersion[0] + \
            "&cx=" + self.cx[0] + "&q=" + self.dork + "&safe=off&cse_tok=" + self.cse_token[0] + "&exp=" \
            + self.exp[0][0] + "," + self.exp[0][1] + "&callback=google.search.cse.api16950"

            request = self.reqs.get(url = cse_google, headers = self.head)
            found = parse_found_cseurl.findall(request.text)

            if found:
                for cseurl in found:
                    found_url.append(parse_found_targeturl.findall(cseurl)[0])

                for url in found_url:
                    print(url)
                iterate += 10

            else:
                break

        return found_url

    def bing_dorker(self):
        page = 1
        pages = 1000
        parse = regex.compile(r'\<h2\>\<a href="(.*?)" h=".*?"\>')
        urls_found = set()
        self.head = {
            'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'
        }
        while(page <= pages):
            request = self.reqs.get(url = "https://bing.com/search?q=" + self.dork + "&first=" + str(page) + \
            "&form=PORE", headers = self.head)
            if request.status_code == 200:
                found = parse.findall(request.text)
                for url in found:
                    print(url)
                    urls_found.add(url)
            else:
                break
            page += 10
        return urls_found
