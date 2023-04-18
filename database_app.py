#database app created with mysql, tkinter, using album and tracks as data
from tkinter import *
import tksheet as ts
import mysql.connector 

#Creating an app front end to interact with a music based mysql data base

#function to connect to database and SELECT all entries from the table album

def init_album():
    mydb = mysql.connector.connect(
        host = "*****",
        user = "*****",
        password = "*****",
        database = "*****"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM album")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult
    
def show_all_album(sheet):
    mydb = mysql.connector.connect(
        host = "*****",
        user = "*****",
        password = "*****",
        database = "*****"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM album;")
    myresult = mycursor.fetchall()
    sheet.set_sheet_data(data=myresult)
    mydb.close()

def select_album(sheet, ent):
    mydb = mysql.connector.connect(
        host = "*****",
        user = "*****",
        password = "*****",
        database = "*****"
    )
    mycursor = mydb.cursor()
    select_state = 'SELECT * FROM album WHERE ALBUM_TITLE LIKE ' + '"%' +  ent.get() + '%";'
    #print(select_state)
    mycursor.execute(select_state)
    myresult = mycursor.fetchall()
    sheet.set_sheet_data(data=myresult)
    mydb.close()

#function to open window that allows you to add a new album entry
def open_add_window_album(root):
    album_window = Toplevel(root)
    album_window.title("Add new Album")
    album_window.geometry("400x300")
    entry_title = Entry(album_window, text="", borderwidth=5)
    entry_title.grid(row=0, column = 0, ipadx=50)
    entry_artist = Entry(album_window, text="", borderwidth=5)
    entry_artist.grid(row=1, column = 0, ipadx=50)
    entry_year = Entry(album_window, text="", borderwidth=5)
    entry_year.grid(row=2, column = 0, ipadx=50)
    entry_image = Entry(album_window, text="", borderwidth=5)
    entry_image.grid(row=3, column = 0, ipadx=50)
    entry_des = Entry(album_window, text="", borderwidth=5)
    entry_des.grid(row=4, column = 0, ipadx=50, ipady=20)
    confirm = Button(album_window, text="Confirm album", padx=40, pady=10, command=lambda:
                    album_commit(entry_title.get(), entry_artist.get(), entry_year.get(), entry_image.get(), entry_des.get()))
    confirm.grid(row=5, column=0)

    #description labels
    titel_label = Label(album_window, text="Album Titel")
    titel_label.grid(row=0, column=1, ipadx=20)
    artist_label = Label(album_window, text="Artist")
    artist_label.grid(row=1, column=1, ipadx=20)
    year_label = Label(album_window, text="Year of Release")
    year_label.grid(row=2, column=1, ipadx=20)
    image_label = Label(album_window, text="Link to Image")
    image_label.grid(row=3, column=1, ipadx=20)
    des_label = Label(album_window, text="Description")
    des_label.grid(row=4, column=1, ipadx=20)


#function to insert a new album into the db
def album_commit(title, artist, year, image, des):
    mydb = mysql.connector.connect(
        host = "*****",
        user = "*****",
        password = "*****!",
        database = "*****"
    )
    mycursor = mydb.cursor()
    sel = "INSERT INTO album (ALBUM_TITLE, ARTIST, YEAR, IMAGE_NAME, DESCRIPTION) VALUES (%s,%s,%s,%s,%s)"
    val = (title, artist, year, image, des)

    mycursor.execute(sel, val)
    mydb.commit()
    mydb.close()

#delete Album entry
def open_delete_window_album(root):
    window = Toplevel(root)
    window.title("Delete Album")
    window.geometry("600x400")
    retu = init_album()
    options= []
    for i in retu:
        options.append(i[1])
    current = StringVar()
    current.set(options[0])
    drop = OptionMenu(window, current, *options)
    drop.grid(row=0, column=0)
    sheet = ts.Sheet(window, data=start_query(current.get()))
    sheet.grid(row=1, column = 0, ipadx=100)
    select_button = Button(window, text="Show Selected Album", padx=10, pady=5, command=lambda:select_album(sheet, current))
    select_button.grid(row=2, column=0)
    delete_button = Button(window, text="Delete Selected Album", padx=10, pady=5, command=lambda:delete_album(current.get()))
    delete_button.grid(row=3, column=0)

#query to get first entry for the sheet on delete window pop up
def start_query(string):
    mydb = mysql.connector.connect(
        host = "*****",
        user = "*****",
        password = "*****!",
        database = "*****"
    )
    mycursor = mydb.cursor()
    select_state = 'SELECT * FROM album WHERE ALBUM_TITLE LIKE ' + '"%' +  str(string) + '%";'
    #print(select_state)
    mycursor.execute(select_state)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

#takes the album name, then query to get the index and delete via primary key
def delete_album(name):
    album = start_query(name)
    #album = album[0]
    mydb = mysql.connector.connect(
        host = "*****",
        user = "*****",
        password = "*****!",
        database = "*****"
    )
    mycursor = mydb.cursor()
    dele = "DELETE FROM album WHERE ID = %s"
    wh = list(str(album[0][0]))

    mycursor.execute(dele,wh)
    mydb.commit()
    mydb.close()



#main loop found in main.py
