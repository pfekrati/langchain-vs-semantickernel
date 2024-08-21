import asyncio
import os
import time
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
from semantic_kernel.prompt_template import PromptTemplateConfig
from semantic_kernel.contents import ChatHistory
from credentials.azureopenai_mock import add_azure_openai_env_variables
from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import AzureChatPromptExecutionSettings
from semantic_kernel.connectors.ai.function_call_behavior import FunctionCallBehavior
import json

async def main(log:bool=False) -> float:
    add_azure_openai_env_variables()
    execution_times = []

    for _ in range(11):

        # Start benchmarking
        start_time = time.time()

        kernel = Kernel()

        chat_service =   AzureChatCompletion(
            api_key=  os.environ["AZURE_OPENAI_KEY"],
            endpoint= os.environ["AZURE_OPENAI_ENDPOINT"],
            deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
        )
        kernel.add_service(chat_service)

        history = ChatHistory()
        history.add_system_message("Translate the following from English into Italian")
        history.add_user_message("hi!")

        chat_completion : AzureChatCompletion = kernel.get_service(type=ChatCompletionClientBase)
        execution_settings = AzureChatPromptExecutionSettings()
        response = (await chat_completion.get_chat_message_contents(
                    chat_history=history,
                    kernel=kernel,
                    settings=execution_settings,
                    arguments=KernelArguments(),
                ))
        if log:
            print(str(response[0]))
        
        # End benchmarking
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        if log:
            print(f"SK Execution time: {execution_time} seconds")
        await asyncio.sleep(0.2)

    execution_times.pop(0)
    average_time = sum(execution_times) / len(execution_times)
    if log:
        print(f"SK Average execution time: {average_time} seconds")
    return average_time
    

if __name__ == "__main__":
    asyncio.run(main())
