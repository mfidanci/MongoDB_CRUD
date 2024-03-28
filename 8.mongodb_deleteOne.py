from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.
collection = db["customers"]    # Collection'ı seçiyorum.

# deleteOne() query'le eşleşen ilk dokümanı siler.

query = {"address":"Eryaman 56"}
result = collection.delete_one(query)

print("Deletion Acknowledged: ", result.acknowledged)
print("Number of Documents Deleted: ", result.deleted_count)

# deleteOne() ile spesifik bir dokümanı silmek için _id alanı (field) quey'de kullanılmalıdır.
result = collection.delete_one({"_id": 7})
print("Deletion Acknowledged: ", result.acknowledged)
print("Number of Documents Deleted: ", result.deleted_count)

client.close()
