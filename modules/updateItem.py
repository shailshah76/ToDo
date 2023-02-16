import sqlite3

DB_PATH = './todo.db'   # Update this path accordingly

#Update the status of the todo
def update_status(item, status):
    # Check if the passed status is a valid value
    if (status.lower().strip() == 'not started'):
        status = "NOTSTARTED"
    elif (status.lower().strip() == 'in progress'):
        status = "INPROGRESS"
    elif (status.lower().strip() == 'completed'):
        status = "COMPLETED"
    else:
        print("Invalid Status: " + status)
        return None

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update items set status=? where item=?', (status, item))
        conn.commit()
        return {item: status}
    except Exception as e:
        print('Error: ', e)
        return None
    
#Update the task of the todo
def update_task(sr, item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        print("in q")
        c.execute('update items set item=? where sr=?', (item, sr))
        conn.commit()
        return {sr: item}
    except Exception as e:
        print('Error: ', e)
        return None