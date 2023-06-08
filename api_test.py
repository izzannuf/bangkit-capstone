import requests

# Set the URL of your FastAPI application
url = "http://localhost:8000/predict"

# Set the request payload
payload = {
    "category": "emas",
    "latitude": -6.221877,
    "longitude": 106.846261
}

# Make the POST request
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Request was successful
    predictions = response.json()
    print(predictions)
else:
    # Request failed
    print("Request failed with status code:", response.status_code)