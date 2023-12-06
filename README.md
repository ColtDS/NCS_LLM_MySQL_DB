# NCS_LLM_MySQL_DB

**Overview**

This project leverages OpenAI's LLM, Hugging Face embeddings, Streamlit, the Langchain framework, ChromaDB, and few-shot learning to build a natural language processing system. This system is designed to interact with a MySQL database for a t-shirt store selling brands like Adidas, Nike, Van Heusen, and Levi's. It allows the store manager to query inventory, sales, and discounts data using natural language, which the system then translates into SQL queries to fetch the relevant information.

**Project Highlights**

 a t shirt store that sells Adidas, Nike, Van Heusen and Levi's t shirts

Their inventory, sales and discounts data is stored in a MySQL database
We will build an LLM based question and answer system that will use following,



    Natural Language Interface: Users can ask questions in natural language to retrieve data from the MySQL database.
    Integration with OpenAI LLM: Utilizes OpenAI's language models for processing and understanding queries.
    Hugging Face Embeddings: Leverages Hugging Face's powerful embeddings for language understanding.
    Streamlit UI: Provides an easy-to-use web interface for interaction.
    Langchain Framework: Utilizes the Langchain framework for efficient language model operations.
    ChromaDB: Employs ChromaDB as a vector store for managing data.
    Few-Shot Learning: Incorporates few-shot learning techniques for enhanced performance.



**Installation**

Install the required dependencies using pip:

pip install -r requirements.txt

Acquire an api key through https://openai.com/ and put it in .env file

OPENAPI_KEY ="your_api_key_here"

**Usage**

Run the Streamlit app by executing:

streamlit run main.py

**Project Structure**


main.py: The main Streamlit application script.

langchain_helper.py: This has all the langchain code

requirements.txt: A list of required Python packages for the project.

few_shots.py: Contains few shot prompts

.env: Configuration file for storing your Google API key.
