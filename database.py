from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    print("Connected to mongodb!")
    return client

def insert_document(collection, document):
    # Insert document into the specified collection
    collection.insert_one(document)

def find_documents(collection, query):
    # Find documents in the specified collection based on the query
    return collection.find(query)
