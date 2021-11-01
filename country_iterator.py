import json
import re

class CountryIterator:
    def __init__(self):
        with open('countries.json') as f:
            self.data = json.load(f)
        self.country_list = [country['name']['common'] for country in reversed(self.data)]
        self.country_wiki_page = ''

    def write_to_file(self, country_wiki_page):
        with open('country_wiki_page.txt', 'ab') as f:
            f.write(country_wiki_page.encode('utf-8'))
        with open('country_wiki_page.txt', 'a') as f:
            f.write('\n')

    def __iter__(self):
        return self

    def __next__(self):
        if not self.country_list:
            raise StopIteration
        country = self.country_list.pop()
        link = r'https://en.wikipedia.org/wiki/' + re.sub(r' ', '_', country)
        self.country_wiki_page = f'{country} - {link}'
        return self.write_to_file(self.country_wiki_page)

for country in CountryIterator():
    pass