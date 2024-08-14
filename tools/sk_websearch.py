from semantic_kernel.functions.kernel_function_decorator import kernel_function
from tools.bingsearch import bing_search

class BingWebSearchPlugin:
    @kernel_function(name="search_web_tool", description="use this tool when you need tosearch the web for information")
    def search_web_tool(self, query:str) -> str:
        return bing_search(query)