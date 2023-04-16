#database app created with mysql, tkinter, using album and tracks as data
from tkinter import *
import tksheet as ts
import mysql.connector 

#Creating an app front end to interact with a music based mysql data base

#function to connect to database and SELECT all entries from the table album

def init_album():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Train1235!",
        database = "music"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM album")
    myresult = mycursor.fetchall()
    return myresult
    
def show_all_album(sheet):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Train1235!",
        database = "music"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM album;")
    myresult = mycursor.fetchall()
    sheet.set_sheet_data(data=myresult)

def select_album(sheet, ent):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Train1235!",
        database = "music"
    )
    mycursor = mydb.cursor()
    select_state = 'SELECT * FROM album WHERE ALBUM_TITLE LIKE ' + '"%' +  ent.get() + '%";'
    #print(select_state)
    mycursor.execute(select_state)
    myresult = mycursor.fetchall()
    sheet.set_sheet_data(data=myresult)

#main loop moved to main.py
