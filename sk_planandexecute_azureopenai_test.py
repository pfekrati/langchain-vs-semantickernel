import asyncio
import os
import time
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
from semantic_kernel.prompt_template import PromptTemplateConfig
from semantic_kernel.contents import ChatHistory
from credentials.azureopenai import add_azure_openai_env_variables
from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import AzureChatPromptExecutionSettings
from semantic_kernel.connectors.ai.function_call_behavior import FunctionCallBehavior
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from tools.sk_websearch import BingWebSearchPlugin
from tools.sk_email_search import EmailSearchPlugin
from tools.sk_send_email import SendEmailPlugin


async def main(numberOfTests:int,log:bool=False):
    add_azure_openai_env_variables()
    execution_times = []

    for _ in range(numberOfTests+1):

        # Start benchmarking
        start_time =  time.perf_counter()

        kernel = Kernel()

        chat_service =   AzureChatCompletion(
            api_key=  os.environ["AZURE_OPENAI_KEY"],
            endpoint= os.environ["AZURE_OPENAI_ENDPOINT"],
            deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
        )
        kernel.add_service(chat_service)

        kernel.add_plugin(BingWebSearchPlugin(), plugin_name="BingWebSearchPlugin")
        kernel.add_plugin(EmailSearchPlugin(), plugin_name="EmailSearchPlugin")
        kernel.add_plugin(SendEmailPlugin(), plugin_name="SendEmailPlugin")

        history = ChatHistory()
        history.add_system_message("You are an AI agent who can help find information on the web and send emails.")
        history.add_user_message("search the web, find out who won the 2024 super bowl and then send a one line email to Bob and tell him . Use the search_email tool to find his email")

        chat_completion : AzureChatCompletion = kernel.get_service(type=ChatCompletionClientBase)
        execution_settings = AzureChatPromptExecutionSettings()
        execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

        response = (await chat_completion.get_chat_message_contents(
                    chat_history=history,
                    kernel=kernel,
                    settings=execution_settings,
                    arguments=KernelArguments(),
                ))[0]

        if log:
            print(str(response))

        # End benchmarking
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        if log:
            print(f"SK Execution time: {execution_time} seconds")
        await asyncio.sleep(1)

    execution_times.pop(0)
    average_time = sum(execution_times) / len(execution_times)
    if log:
        print(f"SK Average execution time: {average_time} seconds")
    return average_time
    

if __name__ == "__main__":
    asyncio.run(main(True))
