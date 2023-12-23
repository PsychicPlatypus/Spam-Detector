from typing import List
from nltk.tokenize import word_tokenize
import nltk
import pandas as pd


class Tokenizer:
    def __init__(self) -> None:
        df = pd.read_csv("emails.csv")
        nltk.download("punkt")
        self.token_map = dict()
        self.row_arr = self.__trim_rows(df.columns.values.tolist())
        self.__populate_token_map()

    def tokenize_string(self, str_: str):
        str_ = str_.lower()
        tokenized = word_tokenize(str_)

        for i in tokenized:
            if i in self.row_arr:
                self.token_map[i] += 1

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.token_map, index=[0])

    def __trim_rows(self, rows: List[str]) -> List[str]:
        rows.remove("Email No.")
        rows.remove("Prediction")
        return rows

    def __populate_token_map(self) -> None:
        for row in self.row_arr:
            self.token_map[row] = 0
