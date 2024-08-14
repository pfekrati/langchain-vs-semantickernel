import os

def add_azure_openai_env_variables():
    os.environ["AZURE_OPENAI_ENDPOINT"] = ""
    os.environ["AZURE_OPENAI_KEY"] = ""
    os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] = ""
    os.environ["AZURE_OPENAI_API_VERSION"] = ""