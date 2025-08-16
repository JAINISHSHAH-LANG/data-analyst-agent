import requests

# API endpoint
url = "http://127.0.0.1:8000/api/"

# Files to send
files = {
    "questions": open("questions.txt", "rb"),   # <-- make sure this file exists
    "files": open("data.csv", "rb")             # <-- optional CSV file
}

# Send POST request
response = requests.post(url, files=files)

# Print response JSON
print(response.json())
