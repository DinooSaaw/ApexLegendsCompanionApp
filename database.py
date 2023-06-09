from pymongo import MongoClient

def connect_to_mongodb():
    """Connect to MongoDB and return the client object.

    Returns:
        MongoClient: The MongoDB client object.

    """
    client = MongoClient("")
    print("Connected to MongoDB!")
    return client

def insert_document(collection, document):
    """Insert a document into the specified collection.

    Args:
        collection (Collection): The MongoDB collection to insert the document into.
        document (dict): The document to be inserted.

    """
    collection.insert_one(document)

def find_documents(collection, query):
    """Find documents in the specified collection based on the query.

    Args:
        collection (Collection): The MongoDB collection to search.
        query (dict): The query to filter the documents.

    Returns:
        Cursor: A cursor object pointing to the result documents.

    """
    return collection.find(query)
