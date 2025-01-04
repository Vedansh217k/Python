import sqlite3

conn = sqlite3.connect('youtube_vedios.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vedio(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               
    )
''')

def list_vedios():
    cursor.execute("SELECT * FROM vedio")
    for row in cursor.fetchall():
        print(row)

def add_vedios(name , time):
    cursor.execute("INSERT INTO vedio (name, time) VALUES (? ,?)", (name, time))
    conn.commit()

def update_vedio(vedio_id, new_name, new_time):
    cursor.execute("UPDATE vedio SET name = ?, time = ? WHERE id = ?", (new_name, new_time, vedio_id))
    conn.commit() 
       
def delete_vedio(vedio_id):
    conn.execute("DELETE FROM vedio where id = ? ",(vedio_id,))
  
    
    conn.commit()
def main():
    while True:
        print("\n Youtube manger app with DB")

        print("1. list all youtube vedios ")
        print("2. Add a youtube vedio ")
        print("3. Update a youtube vedio details ")
        print("4. Delete a vedio ")
        print("5. Exit the app ")
        choice = input("Enter the choice: ")

        if choice == '1':
            list_vedios()
        elif choice == '2':
            name = input("Enter vedio name: ")
            time = input("Enter vedio time: ")
            add_vedios(name , time)
        elif choice == '3':
            vedio_id = input("Enter vedio ID to Update:")
            name = input("Enter thenew vedio name:")
            time = input("Enter the new time:")
            update_vedio(vedio_id, name , time)
        elif choice == '4':
            vedio_id = input("Enter the vedio ID to delete:")
            delete_vedio(vedio_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")    
    conn.close()
        
if __name__ == "__main__":
    main()