import json
import web.search as search
import excel.build as build

def run() -> None:
    config_path = "./config/setting.json"

    with open(config_path) as f:
        config = json.load(f)

    browser = search.Crawler(link=config["link"], headers=config["headers"])
    browser.run()
    browser.build_json()
    excel = build.Excel(dictionary=browser.get_dictionary())
    excel.run()

if __name__ == "__main__":
    run()
