import pymongo
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch

def get_mongo_collection(c_string, db_name, collection_name):
    connection_string = c_string
    # Connect to your MongoDB database
    client = pymongo.MongoClient(connection_string)
    db = client["dataset"]
    collection = db["deep_learning_research_papers"]

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    print(f'There are {collection.count_documents({})} documents in the collection.')
    return collection

def delete_all_embeddings(collection):
    print('Deleting all embeddings from collection...')
    try:
        collection.delete_many({})
    except Exception as e:
        print(f'Error deleting embeddings from collection: {e}')
    print('Done!')
# delete_all_embeddings(collection)

def upload_to_vector_db(chunked_docs):
    print('Loading vector database with chunked documents and embeddings...')
    try:
        vector_db = MongoDBAtlasVectorSearch.from_documents(
            chunked_docs,
            embeddings,
            collection=collection
        )
    except Exception as e:
        print(e)
    print('Done!')

def mongodb_vector_search(connection_string, db_name, collection_name, embeddings):
    mongo_vector_db = MongoDBAtlasVectorSearch.from_connection_string(
        connection_string,
        f"{db_name}.{collection_name}",
        embeddings,
        index_name="vector_index"
    ) 
    return mongo_vector_db