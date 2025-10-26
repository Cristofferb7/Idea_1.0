import subprocess
import time
import requests
import sys
from pathlib import Path

def start_server():
    python_path = sys.executable
    server_process = subprocess.Popen(
        [python_path, "-m", "uvicorn", "main:app", "--reload"],
        cwd=Path(__file__).parent
    )
    # Wait for server to start
    time.sleep(2)
    return server_process

def test_endpoints():
    BASE_URL = "http://localhost:8000"
    
    # Test root endpoint
    try:
        response = requests.get(f"{BASE_URL}/")
        print("Root endpoint:", response.json())
    except Exception as e:
        print("Root endpoint error:", str(e))

    # Test fighter endpoint
    try:
        response = requests.get(f"{BASE_URL}/api/fighter/ryu")
        print("\nFighter endpoint (Ryu):", response.json())
    except Exception as e:
        print("\nFighter endpoint error:", str(e))

    # Test login endpoint
    try:
        response = requests.post(
            f"{BASE_URL}/api/login",
            json={"username": "test", "password": "test"}
        )
        print("\nLogin endpoint:", response.json())
    except Exception as e:
        print("\nLogin endpoint error:", str(e))

if __name__ == "__main__":
    server = start_server()
    try:
        test_endpoints()
    finally:
        server.terminate()
        server.wait()