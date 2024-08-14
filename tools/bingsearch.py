import requests
import os
import sys
import inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from  credentials.bing import add_bing_env_variables


def bing_search(query):
    add_bing_env_variables()
    bing_api_key = os.environ["BING_API_KEY"]
    bing_api_endpoint =  os.environ["BING_API_ENDPOINT"]

    headers = {
        'Ocp-Apim-Subscription-Key': bing_api_key
    }

    params = {
        'q': query,
        'count': 1  # Number of search results to retrieve
    }

    response = requests.get(bing_api_endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    return search_results["webPages"]["value"][0]["snippet"]