from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.
collection = db["customers"]

# Spesifik bir adresi bulup bu adresi güncellemek
query = {"address":"Valley 345"}    # filtreliyoruz
new_value = {"$set":{"address":"Canyon 123"}}   # güncelleme operatörü kullanıyoruz

result = collection.update_one(query, new_value)
print("Eşleşen dokümanların saysısı: ", result.matched_count)
print("Değiştirilen dokümanların sayısı: ", result.modified_count)

client.close()