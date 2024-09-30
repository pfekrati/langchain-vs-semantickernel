import getpass
import os
import asyncio
import time
from langchain_openai import AzureChatOpenAI
from credentials.azureopenai_mock import add_azure_openai_env_variables
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

async def main(log:bool=False):
    add_azure_openai_env_variables()

    model = AzureChatOpenAI(
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        api_key=os.environ["AZURE_OPENAI_KEY"],
    )

    messages = [
        SystemMessage(content="Translate the following from English into Italian"),
        HumanMessage(content="hi!"),
    ]

    parser = StrOutputParser()
    chain = model | parser

    response = await chain.ainvoke(messages)
    if log:
        print(response)

    await asyncio.sleep(0.2)


if __name__ == "__main__":
    asyncio.run(main())