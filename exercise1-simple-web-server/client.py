import requests

BASE_URL = "http://localhost:8000"

# ทดสอบ HTTP GET (ไม่มีพารามิเตอร์)
r = requests.get(BASE_URL)
print("GET /            ->", r.status_code, r.text)

# ทดสอบ HTTP GET พร้อมพารามิเตอร์ msg
r = requests.get(BASE_URL, params={"msg": "hello vasupon"})
print("GET /?msg=...    ->", r.status_code, r.text)

# ทดสอบ HTTP POST แบบ JSON
r = requests.post(BASE_URL, json={"name": "Student", "message": "Hello from requests (JSON)"})
print("POST (json)      ->", r.status_code, r.json())

# ทดสอบ HTTP POST แบบ form data
r = requests.post(BASE_URL, data={"message": "Hello from requests (form)"})
print("POST (form)      ->", r.status_code, r.json())
