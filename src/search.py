from pymongo.mongo_client import MongoClient
from langchain.document_loaders import Docx2txtLoader, PyPDFLoader
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import UnstructuredPowerPointLoader
import os, json, warnings
import pandas as pd
from dotenv import load_dotenv
from pymongo.errors import OperationFailure
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import src.doc_ingestion as di
import src.pymongo as rp

def create_vector_search():
    vector_search = MongoDBAtlasVectorSearch.from_connection_string(
        connection_string,
        f"{db_name}.{collection_name}",
        embeddings,
        index_name="vector_index"
    )
    return vector_search

def perform_similarity_search(query, top_k=3):
    """
    This function performs a similarity search within a MongoDB Atlas collection.
    It leverages the capabilities of the MongoDB Atlas Search, which under the hood,
    may use the `$vectorSearch` operator, to find and return the top `k` documents that
    match the provided query semantically.

    :param query: The search query string.
    :param top_k: Number of top matches to return.
    :return: A list of the top `k` matching documents with their similarity scores.
    """

   # Get the MongoDBAtlasVectorSearch object
    vector_search = create_vector_search()

    # Execute the similarity search with the given query
    results = vector_search.similarity_search_with_score(
        query=query,
        k=top_k,
    )

    return results

