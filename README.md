# Xassistant

The goal of this project is to create a chatbot able to answer questions about the Cycle Ingenieur of Ecole Polytechnique (also called l'X).

## Setup
Install the Pyhton dependencies 
```
pip install -r requirements.txt
```

Create a `.env` file and write your OpenAI API key in it.
```
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

## Run

You can ask questions using the `ask()` function in `ask.py`.

## To use it on another PDF file
Put the PDF file in the `data/` folder.
In `setup.py`, change the path to include the name of your file.
```
loader = PyPDFLoader("data/NAME_OF_YOUR_PDF_FILE")
```

Run the `setup.py` script.


The database will be saved in the `db/` folder.

### Tools used 

Langchain


Chroma