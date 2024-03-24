from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.
collection = db["customers"]    # Collection'ı seçiyorum.

#Bir Query (Sorgu) olmaksızın find()
mydocs = collection.find()      # <class 'pymongo.cursor.Cursor'> iterable bir object

print("All Documents")
for doc in mydocs:
    print(doc['name'])      # iterate edince dictionary olarak yazıyor.
    print(type(doc))

# Bir Query ile find()
query = {"name":"Grace"}    # salary isimli field'i 50000 olanlar
mydocs = collection.find(query)

for doc in mydocs:
    print(doc['name'])      # iterate edince dictionary olarak yazıyor.

# Query ve Projection beraber kullanımı
query = {"salary":55000}    # Filtreleme yaptım
projection = {"_id": 0, "address": 1, "salary": 1, "name": 1, "age": 1}    # Field seçimi yaptım.
mydocs = collection.find(query, projection)

for doc in mydocs:
    print(doc)      # iterate edince dictionary olarak yazıyor.

# Bir sorgu daha
query = {"salary":55000}    # Filtreleme yaptım
projection = {"salary": 0}    # Field seçimi yaptım.
mydocs = collection.find(query, projection)

for doc in mydocs:
    print(doc)      # iterate edince dictionary olarak yazıyor.

# Bir sorgu daha
mydocs = collection.find({}, {"_id": 0, "name": 1, "salary": 1})
for doc in mydocs:
    print(doc)

# Bir sorgu daha
mydocs = collection.find({}, {"_id":0, "address": 0})
for doc in mydocs:
    print(doc)

client.close()