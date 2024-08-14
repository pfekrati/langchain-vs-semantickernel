from langchain_core.tools import tool
from tools.bingsearch import bing_search
 
@tool
def search_web_tool(query:str) -> str:
    """use this tool when you need tosearch the web for information
    
    Args:
        query (str): the query to search for
    """
    return bing_search(query)
