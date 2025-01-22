import uvicorn
import sys
import os
import json
import requests
from fastapi import FastAPI
from server.searching_server import SearchingServer
from server.schemas import StrRequestModel, ContentItemModel
from typing import List
import logging


app = FastAPI()

searching_server_global = SearchingServer()


######################################################
def searching_server():
    global searching_server_global
    return searching_server_global


@app.post("/ai-search", response_model=List[ContentItemModel])
async def ai_search(input_request: StrRequestModel):
    return searching_server().search(input_request.search_request)


@app.post("/page-to-index")
async def page_to_index(input_request: StrRequestModel):
    searching_server().page_to_index(input_request.search_request)
    return { "status": "200" }



if __name__ == "__main__":
    try:
        uvicorn.run(
            "server_api:app",
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8001)),
            log_level="info")
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        print(f"Exception with force stop: {e}", file=sys.stderr)
        #parsing_server_global.stop()
