import getpass
import os
import asyncio
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from credentials.groq import add_groq_env_variables
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

async def main(log:bool=False):
    add_groq_env_variables()

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

    await asyncio.sleep(1)



if __name__ == "__main__":
    asyncio.run(main())