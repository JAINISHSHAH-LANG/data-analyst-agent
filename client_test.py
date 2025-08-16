import requests

url = "http://127.0.0.1:8000/api/"

files = {
    "questions": open("questions.txt", "rb"),
    "files": open("data.csv", "rb")
}

response = requests.post(url, files=files)
print(response.json())
