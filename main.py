from langchain_openai import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.agents.initialize import initialize_agent

import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

db = SQLDatabase.from_uri("sqlite:///db/users.db")

llm = OpenAI(
    openai_api_key=openai_api_key, 
    model_name="gpt-3.5-turbo-instruct",
    temperature=0)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = initialize_agent(
    toolkit.get_tools(),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Step 6: Define the natural language query
query = "List all users who signed up in the past 7 days."

# Step 7: Run the ReAct agent to convert text query to SQL and execute
result = agent_executor.invoke(query)

# Step 8: Output the result
print(result)
