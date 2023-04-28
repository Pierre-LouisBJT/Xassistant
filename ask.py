"""
Main file to ask questions about the document embeded in the database 'db'
"""

from dotenv import load_dotenv

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA
from langchain.chains import RetrievalQA

from langchain.chains import ChatVectorDBChain # for chatting with the pdf


# Take environment variables from .env.
load_dotenv()  

# Supplying a persist_directory where the embeddings are stored on disk
persist_directory = 'db'

embedding = OpenAIEmbeddings()

# Now we can load the persisted database from disk, and use it as normal. 
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

pdf_qa = ChatVectorDBChain.from_llm(OpenAI(temperature=0, model_name="gpt-3.5-turbo"),
                                    vectordb, return_source_documents=False)


def ask(query, max_lenght=500):
    # Decline queries too long
    if len(query)>max_lenght:
        return('Maximum lenght of a question is 500 characters')

    else:
        #Make sure we only have informations that come from the document
        query = "Provide an answer only if it is in the document. " + query 
        result = pdf_qa({"question": query, "chat_history": ""})
        return(result["answer"])


