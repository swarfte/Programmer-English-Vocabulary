import json
import web.search as search

def run() -> None:

    config_path = "./config/setting.json"

    with open(config_path) as f:
        config = json.load(f)

    browser = search.Crawler(link = config["link"],headers=config["headers"])
    browser.run()


if __name__ == "__main__":
    run()
