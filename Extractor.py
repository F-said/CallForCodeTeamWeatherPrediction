# importing csv module
import pandas as pd
import io

FOLDER = "Data/"




class Extract:
    def __init__(self, name):
        self.FileName = FOLDER + name
        self.df = pd.read_csv(self.FileName, na_values=['.'], header=None)



    def head(self):
        return self.df.iloc[0]


    # row is int, column is string
    def findData(self, date, column):
        try:
            fileColumn = self.findColumn(column)
            fileRow = self.findRow(date)

            i = self.df.values(row, column)
            return i
        except ValueError:
            print("Error")
            return None


    def findDates(self, date):
        dateArray = self.df.index[date]
        return dateArray


    def findColumn(self, column):
        headArray = self.df.head()
        for i in headArray:
            if i == column:
                return i
        return None



    def columnData(self, column):
        try:
            x = self.findData(column)
            return self.df.values[:,x]
        except ValueError:
            return None
            pass


