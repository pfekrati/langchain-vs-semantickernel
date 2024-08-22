from semantic_kernel.functions.kernel_function_decorator import kernel_function
from typing import Annotated
from tools.emaildirectory import search_email as search_email_tool

class EmailSearchPlugin:
    @kernel_function(name="search_email",description="use this tool to find the email address of a person using their name")
    def search_email(self, name: Annotated[str, "The name of the person whose email address you want to find"]) -> str:
        return search_email_tool(name)