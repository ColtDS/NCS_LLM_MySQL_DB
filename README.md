# NCS_LLM_MySQL_DB
This is an end to end LLM project based on OpenAI and Langchain. We are building a system that can talk to MySQL database. User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and then executing that query on MySQL database.

**Project Highlights**

 a t shirt store that sells Adidas, Nike, Van Heusen and Levi's t shirts

Their inventory, sales and discounts data is stored in a MySQL database
We will build an LLM based question and answer system that will use following,


    OPEN AI LLM
    Hugging face embeddings
    Streamlit for UI
    Langchain framework
    Chromadb as a vector store
    Few shot learning
    In the UI, store manager will ask questions in a natural language and it will produce the answers



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
