# importing csv module
import pandas as pd

FOLDER = "Data/"

rows = []
type = []


class Extract:
    def __init__(self, name):
        self.FileName = FOLDER + name
        self.df = pd.read_csv(self.FileName)

    # row is int, column is string
    def findData(self, row, column):
        try:
            i = self.df.values(row, column)
            pass
        except ValueError:
            print("Error")
            return None
        return i


"""
    def findColumn(self, column):
        try:
            self.df
"""
