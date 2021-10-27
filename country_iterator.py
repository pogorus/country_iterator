import json
import re

with open('countries.json') as f:
    data = json.load(f)

class CountryIterator:
    def __iter__(self):
        self.country_list = [country['name']['common'] for country in reversed(data)]
        return self

    def __next__(self):
        if not self.country_list:
            raise StopIteration
        country = self.country_list.pop()
        link = r'https://en.wikipedia.org/wiki/' + re.sub(r' ', '_', country)
        country_wiki_page = f'{country} - {link}'

        def write_to_file():
            with open('country_wiki_page.txt', 'ab') as f:
                f.write(country_wiki_page.encode('utf-8'))
            with open('country_wiki_page.txt', 'a') as f:
                f.write('\n')
        return write_to_file()

for country in CountryIterator():
    pass