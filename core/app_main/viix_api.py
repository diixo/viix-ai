import json
from urllib.parse import urlparse
import requests
from pathlib import Path


class ViixApi:

    def __init__(self):
        pass


    def ai_search(self, search_request: str):
        url = "http://127.0.0.1:8001/ai-search"

        try:
            #response = requests.post(url, headers={'Content-type': 'application/json'}, data=json.dumps(params))
            response = requests.post(url, json={ "search_request": search_request })
            response.raise_for_status()
            ###
            return response.json()
        except requests.RequestException as e:
            return {"error": f"RequestException: {e}"}


    def page_to_index(self, search_request: str):
        url = "http://127.0.0.1:8001/page-to-index"

        try:
            #response = requests.post(url, headers={'Content-type': 'application/json'}, data=json.dumps(params))
            response = requests.post(url, json={ "search_request": search_request })
            response.raise_for_status()
            ###
            return response.json()
        except requests.RequestException as e:
            return {"error": f"RequestException: {e}"}


######################################################################
viix_api = ViixApi()


def get_api():
    global viix_api
    return viix_api
