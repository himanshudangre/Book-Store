import sqlite3

#connection to db
def create_table():
    #connection object
    conn = sqlite3.connect('books.db')
    #defining the cursor object
    curr = conn.cursor()
    #execute
    curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER)")
    #commit
    conn.commit()
    #close connection
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('INSERT INTO book VALUES(NULL,?,?,?,?)',(title,author,year,isbn))
    conn.commit()
    conn.close()

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('SELECT * FROM book WHERE title=? or author=? or year=? or isbn=?',(title,author,year,isbn))
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('SELECT * FROM book') #returns a tuple
    rows = curr.fetchall()
    conn.close()
    return rows

create_table()
print(view())
