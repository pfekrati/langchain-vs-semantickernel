import getpass
import os
import asyncio
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from credentials.groq import add_groq_env_variables
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

async def main(log:bool=False) -> float:
    add_groq_env_variables()

    execution_times = []

    for _ in range(11):
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
        if log:
            print(response)

        # End benchmarking
        end_time = time.time()
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
    asyncio.run(main())