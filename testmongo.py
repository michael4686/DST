from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client['phones_db']
collection = db['phones']
document = collection.find_one()
print(document)
for key, value in document.items():
        print(f"{key}: {value}")