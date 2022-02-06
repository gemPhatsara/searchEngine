import pymongo
import csv
import json
from faker import Faker

faker = Faker()
myclient = pymongo.MongoClient("mongodb+srv://gemPhatsara:lFXvlkSGRujYyR4J@cluster0.aqf8z.mongodb.net/cliche?retryWrites=true&w=majority")

mydb = myclient["cliche"]
mycol = mydb["searchengine"]
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath):
    mylist = []
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            dict =  {
                "title": row['domain'],
                "desc": faker.sentence(15),
                "url": "https://www."+row['domain']+".com/",
                "domain": row['domain'],
            }
            mylist.append(dict)
            #add this python dict to json array

        x = mycol.insert_many(mylist)
        
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'final_15million.csv'

# Call the make_json function
make_json(csvFilePath)

