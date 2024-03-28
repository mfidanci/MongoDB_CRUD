from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")   # "Connection String" ile bağlantı açıyorum.
db = client["mydb"]     # Database'i seçiyorum.

#Yeni bir koleksiyon oluştur
collection = db["programs"]

program = {
    "name": "MongoDB",
    "type": "Database",
    "initial_release": 2009,
    "scalability": "High",
    "performance":"Fast",
}

# Dokumanı ekleyelim
mydoc = collection.insert_one(program)
print("Inserted Document ID: ", mydoc.inserted_id)

# Bir çok dokümanı eklemek
programs = [
    {
        "name": "Python",
        "type": "Programming Language",
        "initial_release": 1991,
        "scalability": "High",
        "performance": "High",
        "creator": "Guido van Rossum"
    },
    {
        "name": "Java",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "High",
        "performance": "Medium",
        "creator": "James Gosling"
    },
    {
        "name": "JavaScript",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Brendan Eich"
    },
    {
        "name": "C++",
        "type": "Programming Language",
        "initial_release": 1985,
        "scalability": "High",
        "performance": "High",
        "creator": "Bjarne Stroustrup"
    },
    {
        "name": "MySQL",
        "type": "Database",
        "initial_release": 1995,
        "scalability": "High",
        "performance": "High",
        "creator": "MySQL AB"
    },
    {
        "name": "Ruby",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Yukihiro Matsumoto"
    },
    {
        "name": "PHP",
        "type": "Programming Language",
        "initial_release": 1995,
        "scalability": "Medium",
        "performance": "Medium",
        "creator": "Rasmus Lerdorf"
    },
    {
        "name": "TensorFlow",
        "type": "Machine Learning Library",
        "initial_release": 2015,
        "scalability": "High",
        "performance": "High",
        "creator": "Google Brain Team"
    },
    {
        "name": "Apache CouchDB",
        "type": "Database",
        "initial_release": 2005,
        "scalability": "High",
        "performance": "High",
        "creator": "Apache Software Foundation"
    }
]

mydocs = collection.insert_many(programs)
print(mydocs)

# Tüm dokümanları getirin
print("All Documents:")

for doc in collection.find({}, {"_id":0, "name": 1}):
    print(doc)

# type alanı ("field") "Database" veya "Machine Learning Library" olan dokümanları bulun. "in" kullanarak
types = ["Database","Machine Learning Library"]
query = {"type":{"$in":types}}
projection = {"_id":0, "name":1, "type":1}
mydocs = collection.find(query, projection)

for mydoc in mydocs:
    print(mydoc)


# type alanı ("field") "Database" veya "Machine Learning Library" olan dokümanları bulun. "or" kullanarak
query = {
    "$or":[
        {"type":"Database"},
        {"type":"Machine Learning Library"}
    ]
}
projection = {"_id":0, "name":1, "type":1}
mydocs = collection.find(query, projection)

for mydoc in mydocs:
    print(mydoc)

