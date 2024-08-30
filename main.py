from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from dotenv import load_dotenv

from tools.sql import run_query_tool, list_tables, describe_tables_tool

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=(
                "You are an AI that has access to a SQLite database. \n"
                f"The database has tables of: {tables}\n"
                "Do not make any assumptions about what tables exists "
                "or what columns exist. Instead, us the 'describe_tables' function"
            )
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(
            variable_name="agent_scratchpad"
        ),  # This is similar to memory and is used to keep track of previous messages sent
    ]
)

tools = [run_query_tool, describe_tables_tool]

agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=[
        run_query_tool,
    ],
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=[
        run_query_tool,
    ],
)

agent_executor("How many addresses are in the database?")
