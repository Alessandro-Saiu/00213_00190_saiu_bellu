import requests
from bs4 import BeautifulSoup

"""------------------------------------------------------------------------------------------------------------------"""
# La classe crawler serve per esplorare la sezione europa sia del Financial Times sia del The Economist per poter
# estrarre gli href dei singoli articoli

visitate = set()


class Crawler:

    def __init__(self, url=''):
        self.url = url

    def ottieni_html(self):
        try:
            if self.url not in visitate:
                visitate.add(self.url)
                print('richiesta ok')
                return requests.get(self.url).content
        except Exception as e:
            return print(e)

    def estrai_link(self):
        try:
            if self.url.find('https://www.economist.com') != -1:
                soup = BeautifulSoup(self.ottieni_html(), 'html.parser')
                pagina = soup.find(class_='layout-section-collection ds-layout-grid')
                titoli = pagina.find_all('a', class_="headline-link")
                temp_href_economist = [titolo.get('href') for titolo in titoli if titolo.get('href') not in visitate]
                print('estrazione ok')
                return temp_href_economist
            elif self.url.find('https://www.ft.com') != -1:
                soup = BeautifulSoup(self.ottieni_html(), 'html.parser')
                pagina = soup.find_all(class_='o-teaser__heading')
                lst_pagina = list(pagina)
                lst_stringhe = [str(lista) for lista in lst_pagina]
                temp_href_financial = []
                for _ in lst_stringhe:
                    content_split = _.split('"')
                    for item in content_split:
                        if item.startswith('/content'):
                            temp_href_financial.append(item)
                print('estrazione ok')
                return temp_href_financial
            else:
                print('URL non riconosciuta')
        except Exception as e:
            return print(e)

# sostituendo il numero finale nell'url posso ciclare fra le pagine

    def ciclo_pagine(self):
        try:
            pagine = 1
            href = []
            while pagine <= 1:
                print(f"selezionata pagina: {pagine}")
                href.append(self.estrai_link())
                pagine += 1
                if self.url.find('https://www.economist.com') != -1:
                    self.url = self.url.replace(str(pagine - 1), str(pagine))
                elif self.url.find('https://www.ft.com') != -1:
                    self.url = self.url.replace(str(pagine - 1), str(pagine))
            return href
        except Exception as e:
            return print(e)


"""------------------------------------------------------------------------------------------------------------------"""

Economist = 'https://www.economist.com/europe?page=1'
FinancialTimes = 'https://www.ft.com/world/europe?page=1'

Economist_class = Crawler(Economist)
FinancialTimes_class = Crawler(FinancialTimes)

# il crawler verrà chiamato dalle classi specifiche delle singole testate





