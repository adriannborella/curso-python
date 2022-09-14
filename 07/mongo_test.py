# python -m pip install pymongo
# pip install "pymongo[srv]"

import pymongo
import ipdb

client = pymongo.MongoClient(
    "mongodb+srv://educando:python2022@cluster0.ppjibfy.mongodb.net/\
?retryWrites=true&w=majority")

print("Bases de datos disponibles:", client.list_database_names())

ipdb.set_trace()
db = client.test
print("Colecciones disponibles:", db.list_collection_names())

mycol = db.other_collection

mydict = {"name": "John", "address": "Highway 37"}
# mydict = {"name": "Adrian", "address": "ROsario 123"}
# mydict = {"name": "Juan", "address": "Calle 345"}
# mydict = {"name": "Pedro", "address": "Chicago 789"}
x = mycol.insert_one(mydict)
print(x.inserted_id)

primero = mycol.find_one()
print(primero)

for record in mycol.find():
    print(record)

for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

for x in mycol.find({}, {"address": 0}):
    print(x)

ipdb.set_trace()

myquery = {"address": "Calle 345"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

myquery = {"address": {"$gt": "H"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

myquery = {"address": {"$regex": "^C"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

mydoc = mycol.find().sort("name")
for x in mydoc:
    print(x)

mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)

myquery = {"address": "Chicago 789"}
mycol.delete_one(myquery)

myquery = {"address": {"$regex": "^R"}}
result = mycol.delete_many(myquery)
print(result.deleted_count, " documents deleted.")

result = mycol.delete_many({})
print(result.deleted_count, " documents deleted.")

myquery = {"address": "Calle 345"}
newvalues = {"$set": {"address": " Canyon 123"}}

for record in mycol.find():
    print(record)

mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)

myquery = {"address": {"$regex": "^C"}}
newvalues = {"$set": {"name": "Minnie"}}

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

myresult = mycol.find().limit(2)

#print the result:
for x in myresult:
    print(x)
