# pip install pymongo terminalde çalıştır.
from pymongo import MongoClient

# MongoDB server(sunucusuna) bağlan
connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)

# Bir veritabanı (database) oluşturmak ya da mevcut veritabanına erişmek
db = client["mydb"]

# Birkoleksiyon (collection) oluşturmak veya mevcut koleksiyona erişmek
collection = db["customers"]

# Sistemdeki veritabanlarının listesi
print(client.list_database_names())

# Veritabanındaki koleksiyonların listesi
print(db.list_collection_names())

client.close()