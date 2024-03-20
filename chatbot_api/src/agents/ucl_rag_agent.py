import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, Tool, AgentExecutor
from langchain import hub
from chains.ucl_cypher_chain import ucl_cypher_chain


UCL_AGENT_MODEL = os.getenv("UCL_AGENT_MODEL")

ucl_agent_prompt = hub.pull("hwchase17/openai-functions-agent")

tools = [
    Tool(
        name="Graph",
        func=ucl_cypher_chain.invoke,
        description="""Useful for answering questions about players, teams, and their relationships. Use the entire prompt as input to the tool. For instance, if the prompt is "Which team does this player play for?", the input should be "Which team does this player play for?".""",
    ),
]

chat_model = ChatOpenAI(
    model=UCL_AGENT_MODEL,
    temperature=0,
)

ucl_rag_agent = create_openai_functions_agent(
    llm=chat_model,
    prompt=ucl_agent_prompt,
    tools=tools,
)

ucl_rag_agent_executor = AgentExecutor(
    agent=ucl_rag_agent,
    tools=tools,
    return_intermediate_steps=True,
    verbose=True,
)
