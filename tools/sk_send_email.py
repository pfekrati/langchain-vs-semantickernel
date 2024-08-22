from semantic_kernel.functions.kernel_function_decorator import kernel_function
from typing import Annotated
from tools.sendemail import send_email as send_email_tool

class SendEmailPlugin:
    @kernel_function(name="send_email", description="use this tool to send emails")
    def send_email(self, subject:Annotated[str, "the subject of the email"], text:Annotated[str, "the body of the email"], email:Annotated[str, "email address of the recipient"]):
        send_email_tool("SK", subject, text, email)