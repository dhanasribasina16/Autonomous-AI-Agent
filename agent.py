import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool

# Load API key
load_dotenv()

# -------- Tools (actions agent can perform) --------

def calculator(query: str):
    """Simple calculator tool"""
    try:
        return str(eval(query))
    except:
        return "Invalid calculation"


tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for solving math calculations"
    )
]

# -------- LLM --------

llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo"
)

# -------- Agent --------

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)


def run_agent(task: str):
    return agent.run(task)
