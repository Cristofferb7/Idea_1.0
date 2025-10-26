import requests

BASE_URL = "http://localhost:8000"

def test_root():
    try:
        response = requests.get(f"{BASE_URL}/")
        print("Root endpoint:", response.json())
    except Exception as e:
        print("Root endpoint error:", str(e))

def test_fighter():
    try:
        response = requests.get(f"{BASE_URL}/api/fighter/ryu")
        print("\nFighter endpoint (Ryu):", response.json())
    except Exception as e:
        print("\nFighter endpoint error:", str(e))

def test_login():
    try:
        response = requests.post(f"{BASE_URL}/api/login", json={"username": "test", "password": "test"})
        print("\nLogin endpoint:", response.json())
    except Exception as e:
        print("\nLogin endpoint error:", str(e))

if __name__ == "__main__":
    test_root()
    test_fighter()
    test_login()

def test_root():
    response = client.get("/")
    print("Root endpoint:", response.json())

def test_fighter():
    response = client.get("/api/fighter/ryu")
    print("\nFighter endpoint (Ryu):", response.json())

def test_login():
    response = client.post("/api/login", json={"username": "test", "password": "test"})
    print("\nLogin endpoint:", response.json())

if __name__ == "__main__":
    test_root()
    test_fighter()
    test_login()