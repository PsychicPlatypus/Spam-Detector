from typing import List
import pandas as pd
import numpy as np


class Utils:
    def __init__(self) -> None:
        self.token_map = dict()
        self.__generate_token_map()
        pass

    def __generate_token_map(self):
        df = pd.read_csv("emails.csv")

        row_arr = df.columns.values.tolist()
        row_arr.remove("Email No.")
        row_arr.remove("Prediction")

        for row in row_arr:
            self.token_map[row] = 0
