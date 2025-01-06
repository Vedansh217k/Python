import json
import requests
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
           test = json.load(file)
           print(type(test))
           return test
    except FileNotFoundError:
        return []
    
def save_data_helper(vedios):
    with open('youtube.txt', 'w') as file:
        json.dump(vedios, file)

def list_all_todos():
    url = "https://api.freeapi.app/api/v1/todos"
    response = requests.get(url)
    data = response.json() 
    if data["success"] and "data" in data:
        print("\n")
        print("*"*70)
        todos_data = data["data"]
        for todo_data in todos_data:
            print(todo_data)
        print("\n")
        print("*"*70)
    
    
def add_todos():
    url = "https://api.freeapi.app/api/v1/todos/"
    title = input("Enter title name: ")
    description = input("Enter description: ")
    
    input_obj={
        "title": title,         
        "description": description , # The description of the todo
        #"isComplete": True
    }
    adding_todo = requests.post(url , json=input_obj)

def update_todo():
    list_all_todos()
    id = input("enter the todo ID to update")
    title = input("Enter title name: ")
    description = input("Enter description: ")
    url = "https://api.freeapi.app/api/v1/todos/"+ id
    input_obj={
        "title": title,         
        "description": description , # The description of the todo
        #"isComplete": True
    }
    update_todo = requests.patch(url , json=input_obj)
    print("The updated todo is:" , update_todo)
 
def delete_vedio():
    list_all_todos()
    id = input("Enter the ID of todo to delete:")

    url = "https://api.freeapi.app/api/v1/todos/" + id 
    deleted_todo = requests.delete(url)
    print(deleted_todo)
    

def main():
    vedios = load_data()

    while True:
        print("\n Todo List Manager | choose an option ")
        print("1. list all todos ")
        print("2. Add a todo ")
        print("3. Update a todo ")
        print("4. Delete a todo ")
        print("5. Exit the app ")
        choice = input("Enter the choice: ")
        print(vedios)
        match choice:
            case '1':
                list_all_todos()
            case '2':
                add_todos()
            case '3':
                update_todo()
            case '4':
                delete_vedio()
            case '5':
                break


if __name__ == "__main__":
    main()
