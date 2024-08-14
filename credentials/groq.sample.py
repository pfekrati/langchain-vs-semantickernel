import os

def add_groq_env_variables():
    os.environ["GROQ_ENDPOINT"] = ""
    os.environ["GROQ_API_KEY"] = ""
    os.environ["GROQ_MODEL_ID"] = ""