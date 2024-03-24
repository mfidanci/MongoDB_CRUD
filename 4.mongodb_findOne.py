from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.
collection = db["customers"]    # Collection'ı seçiyorum.

# Bir Query (sorgu) olmaksızın find_one()
result = collection.find_one()
print(result)   # result: dict (document) formatında

print(f"Name : {result['name']}\nAddress : {result['address']}\nSalary : {result['salary']}")

# Bir Query (sorgu) ile find_one()
query = {"age": 56}   # Filtreleme yapıyorum
result = collection.find_one(query)     # Sadece tek doküman
print(f"Name : {result['name']}\nAddress : {result['address']}\nSalary : {result['salary']}")

client.close()