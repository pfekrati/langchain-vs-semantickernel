from langchain_azureopenai_test import main as langchain_azureopenai_test_main
from langchain_groq_test import main as langchain_groq_test_main
from langchain_tool_azureopenai_agent_test import main as langchain_tool_azureopenai_agent_test_main
from langchain_planandexecute_azureopenai_test import main as langchain_planandexecute_azureopenai_test_main
from sk_azureopenai_test    import main as sk_azureopenai_test_main
from sk_groq_test           import main as sk_groq_test_main
from sk_tool_azureopenai_test import main as sk_tool_azureopenai_test_main
from sk_planandexecute_azureopenai_test import main as sk_planandexecute_azureopenai_test_main
import asyncio
import timeit

log = False
nubmerOfTests : int = 10
#####################################################################################################
#####################################################################################################
# performance test using mocked azure open ai endpoint 
#####################################################################################################
#####################################################################################################
print(f"testing the performance of chat compeletion using mocked azure open ai endpoint")

# runner.bench_async_func("Langchain compeletion using mocked azure open ai endpoint",
#             langchain_azureopenai_test_main)

result = timeit('sk_azureopenai_test_main()', setup='from sk_azureopenai_test import main as sk_azureopenai_test_main', number=nubmerOfTests)
print(f'Took {result:.3f} seconds')

# runner.timeit(name="compeletion using mocked azure open ai endpoint",
#               stmt="asyncio.run(langchain_azureopenai_test_main(log))",
#               setup="log = False")

# langchain_azureopenai_average_time = timeit.timeit(stmt="await langchain_azureopenai_test_main(log)", number=nubmerOfTests)
# sk_azureopenai_average_time = timeit.timeit(stmt="await sk_azureopenai_test_main(log)", number=nubmerOfTests)

# Calculate the percentage difference
# azureopenai_test_percentage_difference = ((langchain_azureopenai_average_time - sk_azureopenai_average_time) / sk_azureopenai_average_time) * 100
# Print the results
# print(f"Langchain Average: {langchain_azureopenai_average_time}")
# print(f"SK Average: {sk_azureopenai_average_time}")
# print(f"Percentage Difference: {azureopenai_test_percentage_difference:.2f}%")

#####################################################################################################
#####################################################################################################
# performance test using groq endpoint 
#####################################################################################################
#####################################################################################################
# print(f"testing the performance of chat compeletion using groq endpoint")
# sk_groq_average_time1 = await sk_groq_test_main(log)
# langchain_groq_average_time1 = await langchain_groq_test_main(log)

# await asyncio.sleep(5)

# langchain_groq_average_time2 = await langchain_groq_test_main(log)
# sk_groq_average_time2 = await sk_groq_test_main(log)

# # Calculate the averages
# langchain_groq_test_average = (langchain_groq_average_time1 + langchain_groq_average_time2) / 2
# sk_groq_test_average = (sk_groq_average_time1 + sk_groq_average_time2) / 2
# # Calculate the percentage difference
# groq_test_percentage_difference = ((langchain_groq_test_average - sk_groq_test_average) / sk_groq_test_average) * 100
# # Print the results
# print(f"Langchain Average: {langchain_groq_test_average}")
# print(f"SK Average: {sk_groq_test_average}")
# print(f"Percentage Difference: {groq_test_percentage_difference:.2f}%")

# #####################################################################################################
# #####################################################################################################
# # performance test of tool calling using azure open ai endpoint 
# #####################################################################################################
# #####################################################################################################

# print(f"testing the performance of tool calling using azure open ai endpoint")
# langchain_tool_azureopenai_agent_average_time1 = await langchain_tool_azureopenai_agent_test_main(log)
# sk_tool_azureopenai_average_time1 = await sk_tool_azureopenai_test_main(log)

# await asyncio.sleep(5)

# sk_tool_azureopenai_average_time2 = await sk_tool_azureopenai_test_main(log)
# langchain_tool_azureopenai_agent_average_time2 = await langchain_tool_azureopenai_agent_test_main(log)

# # Calculate the averages
# langchain_tool_azureopenai_agent_test_average = (langchain_tool_azureopenai_agent_average_time1 + langchain_tool_azureopenai_agent_average_time2) / 2
# sk_tool_azureopenai_average_test_average = (sk_tool_azureopenai_average_time1 + sk_tool_azureopenai_average_time2) / 2
# # Calculate the percentage difference
# tool_azureopenai_test_percentage_difference = ((langchain_tool_azureopenai_agent_test_average - sk_tool_azureopenai_average_test_average) / sk_tool_azureopenai_average_test_average) * 100
# # Print the results
# print(f"Langchain Average: {langchain_tool_azureopenai_agent_test_average}")
# print(f"SK Average: {sk_tool_azureopenai_average_test_average}")
# print(f"Percentage Difference: {tool_azureopenai_test_percentage_difference:.2f}%")

# #####################################################################################################
# #####################################################################################################
# # performance test of plan and execute using azure open ai endpoint 
# #####################################################################################################
# #####################################################################################################

# print(f"testing the performance of plan and execute using azure open ai endpoint")
# sk_planandexecute_azureopenai_average_time1 = await sk_planandexecute_azureopenai_test_main(log)
# langchain_planandexecute_azureopenai_agent_average_time1 = await langchain_planandexecute_azureopenai_test_main(log)

# await asyncio.sleep(5)

# langchain_planandexecute_azureopenai_agent_average_time2 = await langchain_planandexecute_azureopenai_test_main(log)
# sk_planandexecute_azureopenai_average_time2 = await sk_planandexecute_azureopenai_test_main(log)

# # Calculate the averages
# langchain_planandexecute_azureopenai_agent_test_average = (langchain_planandexecute_azureopenai_agent_average_time1 + langchain_planandexecute_azureopenai_agent_average_time2) / 2
# sk_planandexecute_azureopenai_average_test_average = (sk_planandexecute_azureopenai_average_time1 + sk_planandexecute_azureopenai_average_time2) / 2
# # Calculate the percentage difference
# planandexecute_azureopenai_test_percentage_difference = ((langchain_planandexecute_azureopenai_agent_test_average - sk_planandexecute_azureopenai_average_test_average) / sk_planandexecute_azureopenai_average_test_average) * 100
# # Print the results
# print(f"Langchain Average: {langchain_planandexecute_azureopenai_agent_test_average}")
# print(f"SK Average: {sk_planandexecute_azureopenai_average_test_average}")
# print(f"Percentage Difference: {planandexecute_azureopenai_test_percentage_difference:.2f}%")