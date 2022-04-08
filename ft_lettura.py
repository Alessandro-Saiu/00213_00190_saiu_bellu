import requests
from bs4 import BeautifulSoup
import urllib.parse
from crawler import FinancialTimes_class
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import pandas as pd

"""------------------------------------------------------------------------------------------------------------------"""


# questa classe serve per estrarre il contenuto di un articolo dal Financial times


class Estrattore:

    def __init__(self, href=[]):
        self.href = href

    def __iter__(self):
        return self.href

    def __next__(self):
        self._indice += 1
        if self._indice >= len(self.href):
            self._indice = -1
            raise StopIteration
        else:
            return self.href[self._indice]

    i = 0
    profile_path = r'C:\Users\Alessandro\AppData\Roaming\Mozilla\Firefox\Profiles\klopbxgh.default-release'
    # ff_profilo = webdriver.FirefoxProfile(profile_path)
    # driver = webdriver.Firefox(firefox_profile=ff_profilo)
    ffOptions = Options()
    ffOptions.add_argument("-profile")
    ffOptions.add_argument(profile_path)
    driver = webdriver.Firefox(options=ffOptions)

    # C:\Users\Alessandro\AppData\Local\Programs\Python\Python310\geckodriver.exe

    # Questo metodo crea una url completa partendo dalla lista di url parziali generati dal crawler e gli applica
    # direttamente la funzione request

    def creazione_richieste(self):
        url_base = 'https://www.ft.com'
        try:
            print('\nselezionata pagina')
            url_completa = [urllib.parse.urljoin(url_base, articolo) for articolo in self.href[self.i]]
            for item in url_completa:
                print(item)
            lista_url = [requests.get(x) for x in url_completa]
            print('\ncreato URL per 26 articoli')
            return lista_url
        except Exception as e:
            return print(e)

    # Questo metodo prende una lista di richieste e permette di navigare nei contenuti della pagina tramite la
    # libreria beautiful soup per estrarre il testo vero e proprio che viene infine inserito come stringa in una
    # lista 'risultato'

    def creazione_soup(self, lista_url=[]):
        try:
            risultato = []
            for pagina in lista_url:
                for articolo in pagina:
                    soup = BeautifulSoup(articolo.content, 'html.parser')
                    if soup.find('div', class_="article__content-body n-content-body js-article__content-body"):
                        print("\nutilizzo beautiful soup")
                        contenuto = []
                        tmp = soup.find('div', class_="article__content-body n-content-body js-article__content-body")
                        tmp = tmp.find_all('p')
                        for _ in tmp[1:]:
                            contenuto.append(_.text)
                        definitivo = ''.join(contenuto)
                        print(definitivo)
                        risultato.append([definitivo])

                    # buona parte degli articoli sono protetti da un paywall ho quindi proceduto a visualizzare il
                    # contenuto tramite il pc nel quale ho accesso agli stessi creando per ogni articolo una sessione
                    # sul mio browser

                    elif soup.select('div', class_="article__content-body n-content-body js-article__content-body"):
                        try:
                            print("\nutilizzo selenium")
                            contenuto = []
                            url = articolo.url
                            self.driver.get(url)
                            # t = Timer(20.0, )
                            # t.start()
                            gate = True
                            self.driver.set_page_load_timeout(10)
                            self.driver.implicitly_wait(10)
                            while gate:
                                # necessario refresh per assicurarsi che parta l'estensione per accettare
                                # automaticamente i cookies
                                self.driver.refresh()
                                # faccio scorrere la pagina
                                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var "
                                                           "lenOfPage=document.body.scrollHeight;return lenOfPage;")
                                corpo = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]'
                                                                           '/article/div[3]/div[3]')
                                paragrafo = corpo.find_elements(By.XPATH, '/html/body/div/div[2]/div/div/div['
                                                                          '2]/article/div[3]/div[3]/div/p')

                                # self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]'
                                # '/article/div[3]/div[3]')
                                for item in paragrafo:
                                    contenuto.append(item.text.strip('\n'))
                                definitivo = ''.join(contenuto)
                                print(definitivo)
                                risultato.append([definitivo])
                                gate = False
                        except NoSuchElementException:
                            print('\nnon ho trovato il contenuto')
                            continue
                        except TimeoutException:
                            print('\ntroppo lento')
                            continue

                    else:
                        print('\nformato html non riconosciuto')
            print(len(risultato))
            return risultato
        except Exception as e:
            return print(e)


"""------------------------------------------------------------------------------------------------------------------"""
# la classe viene fatta iterare fra le diverse pagine della sezione europa del financial times così da inserire in un
# unica lista tutti gli url di diverse pagine che verranno passate al metodo di estrazione

lista_url_def = []

FT = Estrattore(FinancialTimes_class.ciclo_pagine())

for lista in FT.href:
    lista_url_def.append(FT.creazione_richieste())
    FT.i += 1

articoli_FT = FT.creazione_soup(lista_url_def)  # da chiamare nel main

df = pd.DataFrame(articoli_FT)
df.to_markdown('Articoli FT_100.md')

# html.js.enhanced.js-focus-visible.mnkdtba.lvpfwhgzuyj body.o-ads-no-mpu.o-ads-no-mpu1.o-ads-no-third-mpu div.n-layout div.n-layout__row.n-layout__row--content
# div div div.article-content article#site-content.article.article-grid.article-grid--no-full-width-graphics div.article__content.p402_premium div.article__content-body.n-content-body.
# js-article__content-body div.article__content-body.n-content-body.js-article__content-body p
