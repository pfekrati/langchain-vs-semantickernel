import getpass
import os
import asyncio
import time
from langchain_openai import AzureChatOpenAI
from credentials.azureopenai import add_azure_openai_env_variables
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from tools.langchain_websearch import search_web_tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

async def main():
    add_azure_openai_env_variables()

    execution_times = []

    for _ in range(20):
        # Start benchmarking
        start_time = time.time()

        model = AzureChatOpenAI(
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
            openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            api_key=os.environ["AZURE_OPENAI_KEY"],
        )

        tools = [search_web_tool]


        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", """You are an AI agent who can help find information on the web and answer questions."""),
                MessagesPlaceholder("chat_history", optional=True),
                ("human", "{input}"),
                MessagesPlaceholder("agent_scratchpad"),
            ]
        )
        
        agent = create_openai_tools_agent(model, tools, prompt)

        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

        response = await agent_executor.ainvoke({"input": "who won the 2024 super bowl?"})
        print(response['output'])

        # End benchmarking
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        print(f"Langchain Execution time: {execution_time} seconds")
        await asyncio.sleep(1)

    print(f"Langchain Average execution time: {sum(execution_times) / len(execution_times)} seconds")



if __name__ == "__main__":
    asyncio.run(main())