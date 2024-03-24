from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.
collection = db["customers"]    # Collection'ı seçiyorum.

# Bir doküman oluşturmak
mydict = {
    "name": "John",
    "address": "Highway 37",
    "salary": 50_000
}

# Koleksiyona bir doküman eklemek
mydoc = collection.insert_one(mydict)
print(mydoc)
print(type(mydoc))
print(mydoc.inserted_id)

mydict2 ={
    "name":"Peter",
    "address":"Lowstreet 27",
    "salary": 60_000,
    "age":53
}

mydict3 ={
    "name":"Nurten",
    "address":"Eryaman 56",
    "salary": 55_000,
    "age":56
}

mydoc = collection.insert_one(mydict3)

# Databaseleri listelemek
print(client.list_database_names())

print(db.list_collection_names())
client.close()  # Bağlantıyı kapatıyorum.