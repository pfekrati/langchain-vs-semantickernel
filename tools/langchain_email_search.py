from langchain_core.tools import tool
from tools.emaildirectory import search_email as search_email_tool
 
@tool
def search_email(name:str) -> str:
    """use this tool to find the email address of a person
    
    Args:
        name (str): name of the person you want to find the email address of
    """
    return search_email_tool(name)
