
from pymongo.mongo_client import MongoClient
import certifi
#from os import environ
import os
from bson import json_util
import json
from flask import jsonify

#uri = os.getenv('MONGO_DB_CONN')
#uri=environ.get('MONGO_DB_CONN')
uri=os.environ["MONGO_DB_CONN"]

#print(os.getenv('MONGO_DB_CONN'))
# Create a new client and connect to the server
client = MongoClient(uri,tlsCAFile=certifi.where())

# Send a ping to confirm a successful connection
try:
    #client.admin.command('ping')
    #print("Pinged your deployment. You successfully connected to MongoDB!")

    db=client["SQLAuthority"]
    collection=db.get_collection("neworder")
    #print(collection.find_one({"orderno":"123"}))
except Exception as e:
    print(e)

#order={"item":"Chicken curry","orderno":5557,"category":"Main"}

def get_order(orderid):
    try:
        data=json_util.dumps(collection.find_one({'orderno':orderid}))
        return json.loads(data)
    except Exception as e:
        return f"exception in finding order {orderid}"
        #print(e)


def create_new_order(orderDict):
    try:
        result=collection.insert_one(jsonify(orderDict))
        print(result)
        
        return json.loads(json_util.dumps(result))
    except Exception as e:
        print("exception in creating new order")
        print(e)
#get_user("555")
#create_new_order(order)
