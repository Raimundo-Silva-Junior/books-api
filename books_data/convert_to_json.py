import pandas as pd
import json

## https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata?resource=download

## Script to convert books.csv into a json file to dump to database

books = pd.read_csv(r"books_data\books.csv", sep=",")
books = books.fillna("")

columns = tuple(books.columns)

datas = []
for column in columns:
    datas.append(tuple(books[column]))
    

json_data = []
for pk, itens in enumerate(zip(*datas),start=1):
    
    fields = {column: value for column, value in zip(columns, itens)}
    json_data.append({
    "model": "books.Books",
    "pk": pk,
    "fields": fields
  }),

with open("books_data\data_dump.json", "w") as file:
    json.dump(json_data, file, indent=2)
    