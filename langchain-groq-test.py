import getpass
import os
import asyncio
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from credentials.groq import add_groq_env_variables
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

async def main():
    add_groq_env_variables()

    execution_times = []

    for _ in range(20):
        # Start benchmarking
        start_time = time.time()

        model = ChatGroq(temperature=0, groq_api_key=os.environ["GROQ_API_KEY"], model_name=os.environ["GROQ_MODEL_ID"])

        messages = [
            SystemMessage(content="Translate the following from English into Italian"),
            HumanMessage(content="hi!"),
        ]

        parser = StrOutputParser()
        chain = model | parser

        response = await chain.ainvoke(messages)
        print(response)

        # End benchmarking
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        print(f"Langchain Execution time: {execution_time} seconds")
        await asyncio.sleep(1)

    print(f"Langchain Average execution time: {sum(execution_times) / len(execution_times)} seconds")



if __name__ == "__main__":
    asyncio.run(main())