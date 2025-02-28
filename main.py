from pymongo.mongo_client import MongoClient
from langchain.document_loaders import Docx2txtLoader, PyPDFLoader
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import UnstructuredPowerPointLoader
import os, json, warnings
import pandas as pd
from dotenv import load_dotenv
from pymongo.errors import OperationFailure
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

import src.doc_ingestion as di
import src.pymongo as rp
import src.search as vs
import src.chains as chains
load_dotenv()

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Call the function
chunked_docs, unable_to_chunk = di.process_files_in_directory(os.getenv("KB_DIR"))

embeddings= di.get_embeddings(model= "models/embedding-001", api_key= os.getenv("google_api_key"))

collection= rp.get_mongo_collection(c_string= os.getenv("connection_string"),
                                    db_name="dataset", 
                                    collection_name="deep_learning_research_papers")
rp.delete_all_embeddings(collection)

rp.upload_to_vector_db(chunked_docs)

user_query= str(input())
search_results = vs.perform_similarity_search(user_query)

print(f"\nSearch results for your query: \n{search_results}")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",google_api_key=os.getenv("google_api_key",
                             temperature=0.2, convert_system_message_to_human=True, stream=True))

mongo_vector_db= rp.mongodb_vector_search(c_string= os.getenv("connection_string"),
                                        db_name="dataset", 
                                        collection_name="deep_learning_research_papers", 
                                        embeddings= embeddings)

print(f"Result: \n{chains.run_role_chain(query=user_query, llm=llm, mongo_vecto_db=mongo_vector_db)}")