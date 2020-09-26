import pandas as pd
import os


class Creator:
    def __init__(self):
        self.FILENAME = input('write the name of file: ') + '.csv'
        self.file = open(self.FILENAME, 'a')

    def create_header(self):
        header = ['author_name', 'note', 'rating']
        self.file.writelines(str(header) + os.linesep)
        self.file.close()
        return 'Header is Created!\nTry to read or write something in file!'


    @property
    def dF(self):
        self.df = pd.read_csv(self.FILENAME, header=0)
        self.df.columns = ['author_name', 'note', 'rating']
        self.df['rating'] = self.df['rating'].apply(lambda x: x[1:-1])
        self.df['author_name'] = self.df['author_name'].apply(lambda x: x[2:-1])
        self.df['note'] = self.df['note'].apply(lambda x: x[2:-1])
        self.df['rating'] = self.df['rating'].apply(pd.to_numeric)
        return self.df


class WorkWithFile(Creator):

    def dataFrame(self):
        self.df = pd.read_csv(self.FILENAME, header=0)
        self.df.columns = ['author_name', 'note', 'rating']
        self.df['rating'] = self.df['rating'].apply(lambda x: x[1:-1])
        self.df['author_name'] = self.df['author_name'].apply(lambda x: x[2:-1])
        self.df['note'] = self.df['note'].apply(lambda x: x[2:-1])
        self.df['rating'] = self.df['rating'].apply(pd.to_numeric)
        return self.df

    def write_to_file(self):
        author = input('Add_author: ')
        note = input('Add_note: ')
        rating = float(input('Add_rating(0.0-1.0): '))
        if 0.0 <= rating <= 1.0:
            rating = rating
        elif rating > 1.0:
            while rating > 1.0:
                rating = float(input("Введіть коректні дані:"))
            rating = 1.0
        elif rating < 0.0:
            while rating < 1.0:
                rating = float(input("Введіть коректні дані:"))
        iterator = [author, note, rating]
        self.file.writelines(str(iterator) + os.linesep)
        self.file.close()
        return 'Add to the file:' + self.FILENAME

    def read_file(self):
        self.file = open(self.FILENAME)
        return self.file.read()


class Functions(Creator):
    def max_rating(self):
        return self.dF.rating.max()

    def min_rating(self):
        return float(self.dF.rating.min())

    def avg_rating(self):
        return self.dF.rating.mean()



a = Creator()
print(a.create_header())
