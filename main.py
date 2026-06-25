import requests

payload ={
    "eventType":"messageReceived"
}

response = requests.post("http://127.0.0.1:8000/wati/webhook",json=payload)

print(response.status_code)
print(response.json())