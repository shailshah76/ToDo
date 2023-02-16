import sqlite3

DB_PATH = './todo.db'   # Update this path accordingly
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

#Create the Database
def create_db():
    conn = sqlite3.connect(DB_PATH)

    # Once a connection has been established, we use the cursor
    # object to execute queries
    c = conn.cursor()

    print("Opened database successfully")

    c.execute('CREATE TABLE IF NOT EXISTS "items" ( "sr" INTEGER PRIMARY KEY AUTOINCREMENT, "item" TEXT NOT NULL, "status" TEXT NOT NULL);')
    print("Table created successfully")
    conn.commit()
    conn.close()