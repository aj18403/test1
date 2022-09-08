import pymongo

client = pymongo.MongoClient("mongodb+srv://adityajadhav:9665514445@cluster0.p0tgwlp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name" : "sudhanshu" ,
    "email" : "sudhanshu@ineuron.ai" ,
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)