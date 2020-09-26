import pandas as pd
import os


class WorkWithFile:
    def __init__(self):
        self.FILENAME = input('write the name of file: ') + '.csv'
        self.file = open(self.FILENAME, 'a')

    def create_headers(self):
        header = ['author_name', 'note', 'rating']
        self.file.writelines(str(header) + os.linesep)
        return 'Header is Created!\nTry to read or write something in file!'

    def dataFrame(self):
        df = pd.read_csv(self.FILENAME, header=0)
        df.columns = ['author_name', 'note', 'rating']
        df['rating'] = df['rating'].apply(lambda x: x[1:-1])
        df['author_name'] = df['author_name'].apply(lambda x: x[2:-1])
        df['note'] = df['note'].apply(lambda x: x[2:-1])
        df['rating'] = df['rating'].apply(pd.to_numeric, errors='coerce')

        return df

    def write_to_file(self):
        author = input('Add_author: ')
        if author != '':
            author = author
        else:
            author = 'NaN'
        note = input('Add_note: ')
        if note != '':
            note = note
        else:
            note = 'NaN'
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

        return 'Add to the file:' + self.FILENAME

    def read_file(self):
        self.file = open(self.FILENAME)
        return self.file.read()


class Functions(WorkWithFile):
    def max_rating(self):
        return self.dataFrame().rating.max()

    def min_rating(self):
        return self.dataFrame().rating.min()

    def avg_rating(self):
        return self.dataFrame().rating.mean()
