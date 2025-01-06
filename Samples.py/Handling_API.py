import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json() 
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        name_title = user_data["name"]["title"]
        name_first = user_data["name"]["first"]
        name_last = user_data["name"]["last"]
        gender = user_data["gender"]
        username = user_data["login"]["username"]
        street_number = user_data["location"]["street"]["number"]
        street_name = user_data["location"]["street"]["name"]
        country = user_data["location"]["country"]
        
        return username , country , name_title , name_first , name_last  , gender , street_number , street_name
    else:
        raise Exception("unable to fetch user data") 

def fetch_user_data():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    user_obj = {}
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_obj["title"] = user_data["name"]["title"]
        user_obj["first"] = user_data["name"]["first"]
        user_obj["last"] = user_data["name"]["last"]
        user_obj["gender"] = user_data["gender"]
        user_obj["username"] = user_data["login"]["username"]
        user_obj["number"] = user_data["location"]["street"]["number"]
        user_obj["name"] = user_data["location"]["street"]["name"]
        user_obj["country"] = user_data["location"]["country"]
        
        return user_obj
    else:
        raise Exception("unable to fetch user data")
def main():

        try:
            user_obj = fetch_user_data()
            print("Title:", user_obj["title"])
        except Exception as e :
            print(str(e))

if __name__ == "__main__":
    main()

