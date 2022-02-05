import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["cliche"]
mycol = mydb["search"]

str_search = "video"

myquery = {"$or": [
    {"title": {"$regex": str_search}},
    {"url": {"$regex": str_search}},
    {"description": {"$regex": str_search}},
]}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
