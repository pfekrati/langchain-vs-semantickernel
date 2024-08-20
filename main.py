from langchain_azureopenai_test import main as langchain_azureopenai_test_main
from langchain_groq_test import main as langchain_groq_test_main
from langchain_tool_azureopenai_agent_test import main as langchain_tool_azureopenai_agent_test_main
from sk_azureopenai_test    import main as sk_azureopenai_test_main
from sk_groq_test           import main as sk_groq_test_main
from sk_tool_azureopenai_test import main as sk_tool_azureopenai_test_main
import asyncio


async def main(log:bool = False):
    #####################################################################################################
    #####################################################################################################
    # performance test using mocked azure open ai endpoint 
    #####################################################################################################
    #####################################################################################################
    print(f"testing the performance of chat compeletion using mocked azure open ai endpoint")
    langchain_azureopenai_average_time_1 = await langchain_azureopenai_test_main(log)
    sk_azureopenai_average_time_1 = await sk_azureopenai_test_main(log)

    sk_azureopenai_average_time_2 = await sk_azureopenai_test_main(log)
    langchain_azureopenai_average_time_2 = await langchain_azureopenai_test_main(log)

    # Calculate the averages
    langchain_azureopenai_test_average = (langchain_azureopenai_average_time_1 + langchain_azureopenai_average_time_2) / 2
    sk_azureopenai_test_average = (sk_azureopenai_average_time_1 + sk_azureopenai_average_time_2) / 2
    # Calculate the percentage difference
    azureopenai_test_percentage_difference = ((langchain_azureopenai_test_average - sk_azureopenai_test_average) / sk_azureopenai_test_average) * 100
    # Print the results
    print(f"Langchain Average: {langchain_azureopenai_test_average}")
    print(f"SK Average: {sk_azureopenai_test_average}")
    print(f"Percentage Difference: {azureopenai_test_percentage_difference:.2f}%")

    #####################################################################################################
    #####################################################################################################
    # performance test using groq endpoint 
    #####################################################################################################
    #####################################################################################################
    print(f"testing the performance of chat compeletion using groq endpoint")
    sk_groq_average_time1 = await sk_groq_test_main(log)
    langchain_groq_average_time1 = await langchain_groq_test_main(log)

    langchain_groq_average_time2 = await langchain_groq_test_main(log)
    sk_groq_average_time2 = await sk_groq_test_main(log)

    # Calculate the averages
    langchain_groq_test_average = (langchain_groq_average_time1 + langchain_groq_average_time2) / 2
    sk_groq_test_average = (sk_groq_average_time1 + sk_groq_average_time2) / 2
    # Calculate the percentage difference
    groq_test_percentage_difference = ((langchain_groq_test_average - sk_groq_test_average) / sk_groq_test_average) * 100
    # Print the results
    print(f"Langchain Average: {langchain_groq_test_average}")
    print(f"SK Average: {sk_groq_test_average}")
    print(f"Percentage Difference: {groq_test_percentage_difference:.2f}%")

    #####################################################################################################
    #####################################################################################################
    # performance test of tool calling using azure open ai endpoint 
    #####################################################################################################
    #####################################################################################################

    print(f"testing the performance of tool calling using azure open ai endpoint")
    langchain_tool_azureopenai_agent_average_time1 = await langchain_tool_azureopenai_agent_test_main(log)
    sk_tool_azureopenai_average_time1 = await sk_tool_azureopenai_test_main(log)

    sk_tool_azureopenai_average_time2 = await sk_tool_azureopenai_test_main(log)
    langchain_tool_azureopenai_agent_average_time2 = await langchain_tool_azureopenai_agent_test_main(log)

    # Calculate the averages
    langchain_tool_azureopenai_agent_test_average = (langchain_tool_azureopenai_agent_average_time1 + langchain_tool_azureopenai_agent_average_time2) / 2
    sk_tool_azureopenai_average_test_average = (sk_tool_azureopenai_average_time1 + sk_tool_azureopenai_average_time2) / 2
    # Calculate the percentage difference
    tool_azureopenai_test_percentage_difference = ((langchain_tool_azureopenai_agent_test_average - sk_tool_azureopenai_average_test_average) / sk_tool_azureopenai_average_test_average) * 100
    # Print the results
    print(f"Langchain Average: {langchain_tool_azureopenai_agent_test_average}")
    print(f"SK Average: {sk_tool_azureopenai_average_test_average}")
    print(f"Percentage Difference: {tool_azureopenai_test_percentage_difference:.2f}%")

if __name__ == "__main__":
    asyncio.run(main(log=False))