from pymongo.mongo_client import MongoClient
from langchain.document_loaders import Docx2txtLoader, PyPDFLoader
from langchain.vectorstores.mongodb_atlas import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
import json
import pandas as pd
from pymongo.errors import OperationFailure

def process_files_in_directory(KB_DIR):
    print('Chunking documents...')
    chunked_docs = []
    unable_to_chunk = []

    # loaders for different file types
    loaders = {
        '.docx': Docx2txtLoader,
        '.pdf': PyPDFLoader,
        '.pptx': UnstructuredPowerPointLoader
    }

    for root, dirs, files in os.walk(KB_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)

            extension = os.path.splitext(filename)[1]
            print(extension)
            if extension in loaders:
                loader = loaders[extension](filepath)
                chunked_docs.extend(process_document(filename, loader))
            else:
                unable_to_chunk.append(filename)
                print(f"No loader available for file type {extension}, filename {filename}")

    print('Done!')
    return chunked_docs, unable_to_chunk


def process_document(filename, document_loader):
    # load the document and split it into sections
    sections = document_loader.load_and_split()
    max_section_length = max(len(section.page_content.split()) for section in sections)
    print(f'{filename} has been divided into {len(sections)} sections. The longest section contains {max_section_length} words')

    return sections

def get_embeddings(model, api_key, task_type="SEMANTIC_SIMILARITY"):
    embeddings = GoogleGenerativeAIEmbeddings(model=model, google_api_key=api_key, task_type=task_type)
    return embeddings