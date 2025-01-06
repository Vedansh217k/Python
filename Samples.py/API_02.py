import requests
def fetch_details():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data"  in data :
        user_data = data["data"] 

        details = []
        for user in user_data["data"]:
            user_obj = {}
            user_obj["email"] = user["email"]
            user_obj["phone"] = user["phone"]
            user_obj= details["email"]
            details.append(user_obj)
            return details

    else:
        print("Unable to fetch detials")
def main():
    detail = fetch_details
    print(detail)

if __name__ == "__main__":
    main()
   
