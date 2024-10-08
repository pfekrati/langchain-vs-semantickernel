import getpass
import os
import asyncio
import time
from langchain_openai import AzureChatOpenAI
from credentials.azureopenai import add_azure_openai_env_variables
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from tools.langchain_websearch import search_web_tool
from tools.langchain_email_search import search_email
from tools.langchain_send_email import send_email
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



async def main(numberOfTests:int,log:bool=False) -> float:
    add_azure_openai_env_variables()

    execution_times = []

    for _ in range(numberOfTests + 1):
        # Start benchmarking
        start_time =  time.perf_counter()

        model = AzureChatOpenAI(
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
            openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            api_key=os.environ["AZURE_OPENAI_KEY"],
        )

        tools = [search_web_tool, search_email, send_email]


        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", """You are an AI agent who can help find information on the web and send emails."""),
                MessagesPlaceholder("chat_history", optional=True),
                ("human", "{input}"),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )
        
        agent = create_openai_functions_agent(model, tools, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

        response = await agent_executor.ainvoke({"input": "search the web, find out who won the 2024 super bowl and then send a one line email to Bob and tell him . Use the search_email tool to find his email"})
        if log:
            print(response['output'])

        # End benchmarking
        end_time =  time.perf_counter()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        if log:
            print(f"Langchain Execution time: {execution_time} seconds")
        await asyncio.sleep(1)

    execution_times.pop(0)
    average_time = sum(execution_times) / len(execution_times)
    if log:
        print(f"Langchain Average execution time: {average_time} seconds")
    return average_time


if __name__ == "__main__":
    asyncio.run(main(True))