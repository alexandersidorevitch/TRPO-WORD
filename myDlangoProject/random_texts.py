from bs4 import BeautifulSoup

def get_url(self, sort='prc.a'):
    return f'{self.url}&sort={sort}'


def get_html(self, url, params=None):
    import requests
    return requests.get(url, headers=self.HEADERS, params=params)


def get_content(self, html):
    from bs4 import BeautifulSoup as bs

    soup = bs(html, 'lxml')
    print(soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['name']),
          soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['price']),
          soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['href']),
          soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['place']),
          soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['time']), sep='\n')
    data = [{'Название': name.text, 'Цена': price.text, 'Ссылка': href.get('href'), 'Место': place.text,
             'Дата и время публикации': time.text} for
            name, price, href, place, time in
            zip(soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['name']),
                soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['price']),
                soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['href']),
                soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['place']),
                soup.select(self.CLASSES[self.NUMBER_OF_CLASSES]['time']))]
    return data