import requests
from parsers import myparser
from discovery.constants import *


class search_threatcrowd:

    def __init__(self, word):
        self.word = word.replace(' ', '%20')
        self.results = ""
        self.totalresults = ""
        self.server = "www.google.com"
        self.hostname = "www.google.com"
        self.quantity = "100"
        self.counter = 0

    def do_search(self):
        try:
            urly = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=" + self.word
        except Exception as e:
            print(e)
        headers = {'User-Agent': getUserAgent()}
        try:
            r = requests.get(urly, headers=headers)
        except Exception as e:
            print(e)
        self.results = r.text
        self.totalresults += self.results

    def get_hostnames(self):
        rawres = myparser.parser(self.results, self.word)
        return rawres.hostnames()

    def process(self):
        self.do_search()
        print("\tSearching Threatcrowd results..")
