openapi_key = ''

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

name = llm('what is langchain')

print(name)

pip install langchain==0.0.316

pip install openai==0.28.1

from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db_user = "root"
db_password = "root"
db_host = "localhost"
db_name = "ncs_tshirts"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

print(db.table_info)