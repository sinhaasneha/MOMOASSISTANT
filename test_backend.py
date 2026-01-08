import requests

res = requests.post(
    "http://localhost:5000/api/momo",
    json={"message": "hello"}
)

print(res.status_code)
print(res.text)
