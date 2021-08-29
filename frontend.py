from tkinter import *
from tkinter import messagebox
import backend
window = Tk()

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
def clear_entry_in_widget():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    #.get() is used to output a string object becoz it was StringVar()
    searched_array = backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    if searched_array:
        list1.delete(0, END)
        for row in searched_array:
            list1.insert(END,row)
        clear_entry_in_widget()
    else:
        messagebox.showinfo(title="BOOK STORE",
                            message=f"Item not found")

def add_command():
    if title_text.get()=="" or author_text.get()=="" or year_text.get()=="" or isbn_text.get()=="":
        messagebox.showinfo(title="BOOK STORE",
                                message=f"Please fill all the Entries")
    else:
        backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,END)
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
        clear_entry_in_widget()
        view_command()

def delete_command():
    try:
        if backend.view() and selected_tuple:
            title = selected_tuple[1]
            author = selected_tuple[2]
            year = selected_tuple[3]
            isbn = selected_tuple[4]
            is_ok = messagebox.askokcancel(title="BOOK STORE",
                                   message=f"These are the Details of Selected item: \nTitle: {title} \nAuthor: {author} \nYear: {year} \nISBN: {isbn} \nPress ok to confirm")
            if is_ok:
                backend.delete(selected_tuple[0])
            clear_entry_in_widget()
            view_command()
    except:
        messagebox.showinfo(title="BOOK STORE",
                            message=f"Nothing to Delete")

def update_command():
    try:
        if backend.view() and selected_tuple:
            backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
            clear_entry_in_widget()
            view_command()
    except:
        messagebox.showinfo(title="BOOK STORE",
                            message=f"Nothing to Update")


window.wm_title("BOOK STORE")

l1=Label(window,text="Title",fg="#17202a",font="arial 18 bold ")
l1.grid(row=0,column=0,pady=12)

l2=Label(window,text="Author",fg="#17202a",font="arial 18 bold")
l2.grid(row=0,column=2)

l3=Label(window,text="Year",fg="#17202a",font="arial 18 bold")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN",fg="#17202a",font="arial 18 bold")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text,width=45,bg="#f7dc6f")
e1.grid(row=0,column=1,ipady=5)

author_text=StringVar()
e2=Entry(window,textvariable=author_text,width=45,bg="#f7dc6f")
e2.grid(row=0,column=3,padx=10,ipady=5)

year_text=StringVar()
e3=Entry(window,textvariable=year_text,width=45,bg="#f7dc6f")
e3.grid(row=1,column=1,ipady=5)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text,width=45,bg="#f7dc6f")
e4.grid(row=1,column=3,ipady=5)

list1=Listbox(window, height=18,width=60,bg="#f7dc6f")
list1.grid(row=2,column=0,rowspan=6,columnspan=2,padx=10,pady=12)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,sticky=N+S+E+W,padx=27,pady=15)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# method of tkinter library to select an element tuple in list1, it binds a function to widget event.
list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=38,bg="#2ecc71",font="arial 9 bold",relief=RAISED,command=view_command)
b1.grid(row=2,column=3,ipady=4)

b2=Button(window,text="Search entry", width=38,bg="#2ecc71",font="arial 9 bold",relief=RAISED,command=search_command)
b2.grid(row=3,column=3,ipady=4)

b3=Button(window,text="Add entry", width=38,bg="#2ecc71",font="arial 9 bold",relief=RAISED,command=add_command)
b3.grid(row=4,column=3,ipady=4)

b4=Button(window,text="Update selected", width=38,bg="#2ecc71",font="arial 9 bold",relief=RAISED,command=update_command)
b4.grid(row=5,column=3,ipady=4)

b5=Button(window,text="Delete selected", width=38,bg="#2ecc71",font="arial 9 bold",relief=RAISED,command=delete_command)
b5.grid(row=6,column=3,ipady=4)

b6=Button(window,text="Close", width=38,bg="#2ecc71",font="arial 9 bold",relief=RAISED,command=window.destroy)
b6.grid(row=7,column=3,ipady=4)


window.mainloop()
