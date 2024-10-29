import sqlite3

connect = sqlite3.connect("Ramashka.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS to_do_list(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    status BOOLEAN NOT NULL DEFAULT FALSE, 
    date DATE
     )
     """)

def register():
    description = input("Введите задачу: ")
    status = bool(input("Введите статус задачи: "))
    date = input("Введите дату: ")
    
    cursor.execute("""INSERT INTO to_do_list
                    (description, status, date)
                    VALUES (?, ?, ?)""", (description, status, date))
    connect.commit()
    
def update_status(new_status, task_id):
    cursor.execute("""UPDATE to_do_list
                   SET status = ?
                   WHERE id = ? """, (new_status, task_id))
    connect.commit()
    
    
def delete_task(task_id):
    cursor.execute("DELETE FROM to_do_list WHERE id = ?", (task_id,))
    connect.commit()
    
def all_tasks():
    cursor.execute("SELECT * FROM to_do_list")
    tasks = cursor.fetchall()
    print(tasks)
    
def find(status):
    if 
    
# register()
# update_status("Сделано", 1)
# all_tasks()
# delete_task(3)

    
    
    
    
    