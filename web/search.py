import requests
import bs4


class Crawler(object):
    def __init__(self, link: str, headers: dict = None) -> None:
        self.link = link
        self.headers = headers

    def run(self) -> None:
        webpage = requests.get(url=self.link, headers=self.headers)
        soup = bs4.BeautifulSoup(webpage.text, "html.parser")
        english_word = soup.find("div", class_="item")
        print(english_word)
