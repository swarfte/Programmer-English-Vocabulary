import pandas


class Excel(object):
    def __init__(self, dictionary: dict) -> None:
        self.df = pandas.DataFrame(dictionary.items(), columns=["English", "Chinese"])
        self.excel_path = "./excel/words.xlsx"

    def run(self) -> None:
        self.df.to_excel(self.excel_path, sheet_name="words", index=False)
