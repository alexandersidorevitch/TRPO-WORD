from functools import reduce


class RandomTexts:
    def get_url(self, count_paragraphs):
        return f'https://fish-text.ru/get?format=html&type=paragraph&number={count_paragraphs}&self=true'

    def get_html(self, url, params=None):
        import requests
        return requests.get(url, params=params)

    def get_content(self, html):
        from bs4 import BeautifulSoup as bs

        soup = bs(html, 'lxml')
        data = reduce(lambda x, y: f'{x}\n     {y}', map(lambda el: el.text, soup.select('p')))
        return data

    def get_random_text(self, count_paragraphs):
        try:
            html = self.get_html(self.get_url(count_paragraphs))
            if html.ok:
                return self.get_content(html.text)
            else:
                print('Что-то сломалось')
        except:
            print('Проблема с интернет соединением')
