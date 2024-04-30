import requests

base_url = "http://127.0.0.1:8000"
def get_user(user_id):
    """ Envoie une requête GET pour récupérer les informations d'un utilisateur. """
    response = requests.get(f"{base_url}/items/user/{user_id}")
    return response.json()

def add_item(new_item):
    """ Envoie une requête POST pour ajouter un nouvel item. """
    response = requests.post(f"{base_url}/add-item/", json=new_item)
    return response.json()

def update_item(order_id, updated_item):
    """ Envoie une requête PUT pour mettre à jour un item. """
    response = requests.put(f"{base_url}/update-item/{order_id}", json=updated_item)
    return response.json()

def delete_item(order_id):
    """ Envoie une requête DELETE pour supprimer un item. """
    response = requests.delete(f"{base_url}/delete-item/{order_id}")
    return response.json()

if __name__ == "__main__":
    # Test GET
    print("GET Request:")
    print(get_user(1))
    # Test POST
    new_item = {
        "user_id": 100,
        "order_id": 500,
        "product_id": 300,
        "category_id": 7000,
        "category_code": "electronics.tablet",
        "brand": "samsung",
        "price": 150.75
    }
    print("POST Request:")
    print(add_item(new_item))
    # Test PUT
    updated_item = {
        "price": 200.00
    }
    print("PUT Request:")
    print(update_item(500, updated_item))
    # Test DELETE
    print("DELETE Request:")
    print(delete_item(500))
