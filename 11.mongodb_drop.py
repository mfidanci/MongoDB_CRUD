from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.

print(db.list_collection_names())

collection_name = input("Silinecek koleksiyon adını giriniz: ")
if collection_name in db.list_collection_names():
    collection = db[collection_name]     # Yeni bir koleksiyon oluştur
    collection.drop()
    print(f"{collection_name} isimli koleksiyon silindi.")
else:
    print(f"{collection_name} isimli bir koleksiyon mevcut değil.")

print(client.list_database_names())

# Database düşürmek
db_name = input("Silinecek database ismi: ")
if db_name in client.list_database_names():
    client.drop_database(db_name)
    print(f"{db_name} isimli database silindi.")
else:
    print(f"{db_name} isimli bir database mevcut değil.")

client.close()