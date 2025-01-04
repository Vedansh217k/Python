import json

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

def list_all_vedios(vedios):
    print("\n")
    print("*"*70)
    for index, vedio in enumerate(vedios, start = 1):
        print(f"{index}. {vedio['name']} , Duration: {vedio['time']}")
    print("\n")
    print("*"*70)

def add_vedio(vedios):
    name = input("Enter vedio name: ")
    time = input("Enter vedio time: ")
    vedios.append({'name': name , 'time': time})
    save_data_helper(vedios)

def update_vedio(vedios):
    list_all_vedios(vedios)
    index = int(input("enter the vedio number to update"))
    if 1 <= index <= len(vedios):
        name = input("Enter thenew vedio name")
        time = input("Enter the new time") 
        vedios[index - 1] = {'name': name , 'time': time} 
        save_data_helper(vedios)
    else:
        print("Invalid index selected.")    

def delete_vedio(vedios):
    list_all_vedios(vedios)
    index = int(input("enter the vedio number to be selected"))
    if 1 <= index <= len(vedios):
        del vedios[index-1]
        save_data_helper(vedios)
    else:

       print("Invalid vedio index") 

def main():
    vedios = load_data()

    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. list all youtube vedios ")
        print("2. Add a youtube vedio ")
        print("3. Update a youtube vedio details ")
        print("4. Delete a vedio ")
        print("5. Exit the app ")
        choice = input("Enter the choice: ")
        print(vedios)
        match choice:
            case '1':
                list_all_vedios(vedios)
            case '2':
                add_vedio(vedios)
            case '3':
                update_vedio(vedios)
            case '4':
                delete_vedio(vedios)
            case '5':
                break


if __name__ == "__main__":
    main()


