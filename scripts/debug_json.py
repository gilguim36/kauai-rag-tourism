import json

with open("data/kauai.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    print(f"Name: {item['name']} | Category: {item['category']}")