"""
Generate the embeding of a the PDF file and save it to a database
"""

from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA

# take environment variables from .env.
load_dotenv()  


loader = PyPDFLoader("data/Brochure_Cycle_ingenieur_polytechnicien.pdf")
pages = loader.load_and_split()

# Embed and store the texts
# Supplying a persist_directory will store the embeddings on disk
persist_directory = 'db'

embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=pages, embedding=embedding, persist_directory=persist_directory)

# save embedings to disk
vectordb.persist()
vectordb = None