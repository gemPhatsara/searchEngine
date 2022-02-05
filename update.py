import pymongo
from faker import Faker

fake = Faker()


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["cliche"]
mycol = mydb["se"]


list = mycol.find()
for row in list:
    desc = fake.text()

    url = 'www.'+row['domain']+'.com'
    x = mycol.update(
        { '_id': row['_id'] },   
        {                     
                'domain': row['domain'],
                'desc': desc,
                'url': url,
                'keyword':''
        },
        True
    )