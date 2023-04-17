import database_app as da
from tkinter import *
import  tksheet as ts


if __name__ == "__main__":
    root = Tk()
    root.title("Database music manager")
    root.geometry("800x600")

    #set up labels and buttons
    button_show_all_albums = Button(root, text="Show all albums", padx=10, pady=5, command=lambda: da.show_all_album(album_result_sheet))
    button_show_all_albums.grid(row=0, column=5)

    filler_label = Label(root, text="Filler")
    filler_label.grid(row=0, column=0, columnspan = 3)

    #set up entry widget as text field for search
    album_entry = Entry(root, text="", borderwidth=5)
    album_entry.grid(row=0, column = 1, ipadx = 50, ipady=10)
    
    #button to update album_result_sheet with a SELECT Statement containing the searched keyword
    album_entry_button = Button(root, text="Search", padx=20, command=lambda: da.select_album(album_result_sheet, album_entry))
    album_entry_button.grid(row=1, column=1, columnspan=2, ipadx=30)

    
    album_result_sheet = ts.Sheet(root, data = da.init_album())
    album_result_sheet.grid(row=1, column=5, rowspan = 5, columnspan = 10, ipadx = 100)

    #button to add a new album entry
    album_add_button = Button(root, text="Add new Album", padx=10, pady=5, command=lambda:da.open_add_window_album(root))
    album_add_button.grid(row=0, column=6)

    root.mainloop()