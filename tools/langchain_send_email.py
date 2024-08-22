from langchain_core.tools import tool
from tools.sendemail import send_email as send_email_tool
 
@tool
def send_email(subject:str, text:str, email:str):
    """use this tool to send emails
    
    Args:
        subject (str): email subject
        text (str): email content
        name (str): email address of the recipient
    """
    send_email_tool("LangChain", subject, text, email)
