"""
Name: Hajira Fathima
Date: May 14 2022
Class: CIS 2532 NET01
Description: Program that demonstrates relational databases and SQL.
"""

##Import all tools
import sqlite3
import os.path
import pandas as pd

##Specify path
path = "C:\\Users\\COD_User\\Desktop\\ch17\\"
database = path + 'books.db'
connection = sqlite3.connect(database)

#print("Connection Successful",connection)
#connection = sqlite3.connect('books.db')

##Format as per preferences
print("----------A----------")
print(pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection))
print("")
print("----------B----------")
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection))
print("")
print("----------C----------")
print(pd.read_sql("""SELECT title, copyright, titles.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn ORDER BY title""", connection).head())
print("")
print("----------D----------")
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Daniel', 'Liang')""")
print(pd.read_sql('SELECT first, last FROM authors', connection))
print("")
print("----------E----------")
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO author_ISBN (id,isbn) VALUES ('10','1292221879')""")
cursor = cursor.execute("""INSERT INTO titles (isbn,title,edition,copyright) VALUES ('1292221879','Introduction to Java Programming','11','2019')""")
print(pd.read_sql('SELECT * FROM titles',connection))
