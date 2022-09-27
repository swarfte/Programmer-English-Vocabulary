import requests
import bs4
import json


class Crawler(object):
    def __init__(self, link: str, headers: dict = None) -> None:
        self.link = link
        self.headers = headers
        self.dictionary = {}
        self.json_path = "./config/words.json"

    def run(self) -> None:
        webpage = requests.get(url=self.link, headers=self.headers)
        webpage.encoding = "utf-8"  # set encoding to utf-8
        soup = bs4.BeautifulSoup(webpage.text, "html.parser")
        items = soup.find_all("div", class_="item")
        english_words = (item.find("div", class_="word").find("span").text for item in items)
        chinese_words = (item.find("div", class_="meaning").text for item in items)
        self.dictionary = dict(zip(english_words, chinese_words))

    def get_dictionary(self) -> dict:
        return self.dictionary

    def build_json(self) -> None:
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(self.dictionary, f, indent=4, ensure_ascii=False)
