import sqlite3

DB_PATH = './todo.db'   # Update this path accordingly

#Delete Item from the Database with sr number 
def delete_item(sr):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where sr=?', (sr))
        conn.commit()
        return {'sr': sr}
    except Exception as e:
        print('Error: ', e)
        return None