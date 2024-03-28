from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.
collection = db["customers"]    # Collection'ı seçiyorum.

# Adresi S ile başlayan dokümanları hepsini silelim
query = {"address":{"$regex":"^S"}}

result = collection.delete_many(query)

print("Number of Documents Deleted: ", result.deleted_count)    # Silinen doküman sayısı
print("Deletion Acknowledged: ", result.acknowledged)       # Silme işleminin başarısı : True/False
print("Raw Result: ", result.raw_result)        # İşlwmin sonucu --> Raw Result:  {'n': 4, 'ok': 1.0}

client.close()
