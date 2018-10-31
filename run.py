
import pymongo
uri = "mongodb://aria:malkani28@ds139243.mlab.com:39243/gg-db"
client = pymongo.MongoClient(uri)
db = client.get_database()
tests = db['test']

test_info = {
    "name": "Aria", 
    "age": 18
}


tests.insert_one(test_info)
