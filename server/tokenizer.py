from typing import List
from nltk.tokenize import word_tokenize
import nltk
import pandas as pd
import numpy as np


class Tokenizer:
    def __init__(self) -> None:
        df = pd.read_csv("emails.csv")
        nltk.download("punkt")
        self.token_map = dict()
        self.row_arr = self.__trim_rows(df.columns.values.tolist())
        self.__populate_token_map()

    def tokenize_string(self, str_: str) -> pd.DataFrame:
        str_ = str_.lower()
        tokenized = word_tokenize(str_)
        print(tokenized)
        for i in tokenized:
            if i in self.row_arr:
                print(i)
                self.token_map[i] += 1

    def __trim_rows(self, rows: List[str]) -> List[str]:
        rows.remove("Email No.")
        rows.remove("Prediction")
        return rows

    def __populate_token_map(self) -> None:
        for row in self.row_arr:
            self.token_map[row] = 0
