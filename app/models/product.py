import requests
from bs4 import BeautifulSoup
from opinion import Opinion
from utils import default_selectors, extract_element

class Product():
    def __init__(self, selectors = default_selectors, product_id = '0'):
        self.product_id = product_id
        self.selectors = selectors
        self.opinions_list = []
    
    def get_keys(self):
        return [key for key in self.selectors.keys()]

    def get_selectors(self):
        return [self.selectors[key] for key in default_selectors.keys()]
    
    def create_opinions_list(self):

        current_page = (f'https://www.ceneo.pl/{self.product_id}/opinie-1')
        while current_page != None:
            respons = requests.get(current_page)
            page_dom = BeautifulSoup(respons.text, 'html.parser')
            opinions = page_dom.select('div.js_product-review')

            for opinion in opinions:
                self.opinions_list.append(Opinion())
                for key, args in self.selectors.items():
                    self.opinions_list[-1].set_data(key, extract_element(opinion, *args))

                self.opinions_list[-1].set_data('opinion_id', opinion['data-entry-id'])
                self.opinions_list[-1].set_data('stars', float(self.opinions_list[-1].get_data_key('stars').split('/')[0].replace(',', '.')))
                self.opinions_list[-1].set_data('recommendation', True if self.opinions_list[-1].get_data_key('recommendation') == 'Polecam' else False if self.opinions_list[-1].get_data_key('recommendation') == 'Nie Polecam' else None)
                self.opinions_list[-1].set_data('purchased', bool(self.opinions_list[-1].get_data_key('purchased')))
                self.opinions_list[-1].set_data('useful', int(self.opinions_list[-1].get_data_key('useful')))
                self.opinions_list[-1].set_data('useless', int(self.opinions_list[-1].get_data_key('useless')))
                
            try:
                current_page = 'https://www.ceneo.pl' + page_dom.select('a.pagination__next').pop()['href']
            except IndexError:
                current_page = None
            print(current_page)

h = Product(product_id = 85936012)
print(h.get_keys())
print(h.get_selectors())
h.create_opinions_list()
print(h.opinions_list[0])