import requests

def create_item():
    URL = "https://qa-internship.avito.com/api/1/item"

    data = {
        "sellerID": 19986,
        "itemName": "Стул",
        "price": 10000
    }

    response = requests.post(URL, json=data)

    if response.status_code == 200:
        print("success")
        print(response.json())
    else:
        print(f"decline: {response.status_code}")
        print("Response content:", response.text)

def get_item():
    seller_id = 19986

    url = f'https://qa-internship.avito.com/api/1/{seller_id}/item'

    responce = requests.get(url=url)
    if responce.status_code == 200:
        print("yes")
        print(responce.json())
    else:
        print("decline")

def main():
    create_item()
    get_item()

if __name__ == "__main__":
    main()



    ### Извините за столь убогий код и малое его количество. Никак не успевал с работой и ремонтом в квартире родителей. Надеюсь меня хоть кто-то поймет :).