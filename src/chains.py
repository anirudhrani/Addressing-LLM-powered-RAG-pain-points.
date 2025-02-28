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
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from IPython.display import display
from IPython.display import Markdown
import textwrap

# def _to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def run_basic_chain(query, llm, mongo_vecto_db, doc_retriever= True):
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=mongo_vector_db.as_retriever(search_kwargs={'k':5}),
        return_source_documents=True
    )
    result = qa_chain({"query": query})
    if doc_retriever:
        docs_retr = result["source_documents"]
        print(f'Total Docs retrieved are: {len(docs_retr)} \n Docs: {docs_retr}')
        return Markdown(result["result"])
    return Markdown(result["result"])

def run_role_chain(query, llm, mongo_vecto_db):

    role = """Your name is CSE 598 Project Bot. Utilize the provided context to respond to the forthcoming question.
    If the answer is unknown, simply acknowledge the lack of information, refrain from speculating. Keep responses brief, concluding with
    "Thank you so much for asking me, but unfortunately the documents on which I am trained on are not relevant to your question!"
    {context}
    Question: {question}
    Helpful Answer:"""

    QA_CHAIN_PROMPT = PromptTemplate.from_template(role) 
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=mongo_vector_db.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})
        
    result = qa_chain({"query": question})
    return result["result"]