from tkinter import *
import tkinter.font as tkFont
import backend 
#Note (even) is a special pararemeter 
def get_selected(event):
    global selected_index
    if list_box.curselection(): #makes sure user actually clicks something 
        #index returns a tuple of the selected element. We convert it to an int by indexing 0 or the first number in the tuple 
        index = list_box.curselection()[0]
        selected_index = list_box.get(index)
        isbn = selected_index[4]
        year = selected_index[3]
        author = selected_index[2]
        title = selected_index[1]
        #updating each entry click when clicked 
        title_entry.delete(0, END)
        title_entry.insert(0, title)
        author_entry.delete(0, END)
        author_entry.insert(0, author)
        year_entry.delete(0, END)
        year_entry.insert(0, year)
        isbn_entry.delete(0, END)
        isbn_entry.insert(0, isbn)

def view_command():
    list_box.delete(0,END)
    for row in backend.view():
        list_box.insert(END, row)
def search_entry():
    list_box.delete(0,END)
    for item in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list_box.insert(END, item)
def add_entry():
    #add conditional to make sure entry doesn't already exists 
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.delete(0,END)
    list_box.insert(END,f" New Entry Added Title: {title_text.get()} Author: {author_text.get()} Year: {year_text.get()}  ISBN: {isbn_text} ")
def delete_entry():
    backend.delete(selected_index[0])
    list_box.delete(0,END)
    for row in backend.view():
        list_box.insert(END, row)
def update_entry():
    #takes the ID of the entry and then changes it by getting the new text from each of the entries
    backend.update(selected_index[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    #selected index is the actual index from the list box while the text.get's are from the entry's
    print(selected_index[0], selected_index[2], selected_index[3], selected_index[4])
    list_box.delete(0,END)
    for row in backend.view():
        list_box.insert(END, row)
def close_window():
    window.destroy()
window = Tk()
window.wm_title("Kosausrk's BookStore")
fontStyle = tkFont.Font(family="Roboto", size=15)
canvas = Canvas(window, height = 500, width = 600)
canvas.pack()
#title
title_text = StringVar()
title_label = Label(window, text= "Title", font= fontStyle)
title_label.place(relx=0,rely=0)
title_entry = Entry(window, textvariable = title_text)
title_entry.place(relx = 0.075, rely= 0, relheight = 0.06, relwidth = 0.24)
#year
year_text = StringVar()
year_label = Label(window, text= "Year", font= fontStyle)
year_label.place(relx=0,rely=0.1)
year_entry = Entry(window, textvariable = year_text)
year_entry.place(relx = 0.075, rely= 0.1, relheight = 0.06, relwidth = 0.24)
#author 
author_text = StringVar()
author_label = Label(window, text= "Author", font= fontStyle)
author_label.place(relx=0.35,rely=0)
author_entry = Entry(window, textvariable = author_text)
author_entry.place(relx = 0.45, rely= 0, relheight = 0.06, relwidth = 0.24)
#ISBN 
isbn_text = StringVar()
isbn_label = Label(window, text= "ISBN", font= fontStyle)
isbn_label.place(relx=0.35,rely=0.1)
isbn_entry = Entry(window, textvariable = isbn_text)
isbn_entry.place(relx = 0.45, rely= 0.1, relheight = 0.06, relwidth = 0.24)
#scroll bar and list box 
scroll_bar = Scrollbar(window)
scroll_bar.place(relx=0.65, rely= 0.2, relheight = 0.65)
list_box = Listbox(window, yscrollcommand= scroll_bar.set, font =fontStyle)
list_box.place(relx = 0.01, rely = 0.2, relwidth = 0.6, relheight = 0.65)
list_box.insert(1,"Press view all to view all titles")
list_box.bind("<<ListboxSelect>>", get_selected)
scroll_bar.config(command=list_box.yview)



#view button 
view_button = Button(window, text = "View All", font = fontStyle, width = 12, height = 2, command = view_command)
view_button.place(relx = 0.7, rely = 0.2)
#Search entry 
search_button = Button(window, text = "Search Entry", font = fontStyle, width = 12, height = 2, command  = search_entry)
search_button.place(relx = 0.7, rely = 0.3)
#Add Entry 
add_button = Button(window, text = "Add Entry", font = fontStyle, width = 12, height = 2, command = add_entry)
add_button.place(relx = 0.7, rely = 0.4)
#Update 
update_button = Button(window, text = "Update", font = fontStyle, width = 12, height = 2, command = update_entry)
update_button.place(relx = 0.7, rely = 0.5)
#Delete 
delete_button = Button(window, text = "Delete", font = fontStyle, width = 12, height = 2, command = delete_entry) #w = 12, h =2
delete_button.place(relx = 0.7, rely = 0.6) #relx = 0.7, rely = 0.5
#Close 
close_button = Button(window, text = "Close", font = fontStyle, width = 12, height = 2,command = close_window)  
close_button.place(relx = 0.7, rely = 0.7)

window.mainloop()