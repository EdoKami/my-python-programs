import requests

def send_data():
    server_url = "http://192.168.51.253:5000/receive_data"  # Replace with the actual IP address of the server

    data = {"data": "Hello, server!"}
    response = requests.post(server_url, data=data)

    print(f"Server response: {response.text}")

if __name__ == "__main__":
    send_data()
