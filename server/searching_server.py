
import logging
from server.smart_search import SmartSearch
from server.schemas import ContentItemModel
from typing import List


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
logger = logging.getLogger()
#logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


path_db_index = "server/db-storage/db-index.bin"


class SearchingServer:

    def __init__(self):
        self.smart_search = SmartSearch()


    def search(self, str_reuest: str) -> List[ContentItemModel]:
        logger.info(f"search-request:{str_reuest}")
        result = []
        indices, distances = self.smart_search.search(str_reuest.lower())
        return result


    def page_to_index(self, url: str):
        logger.info(f"page_to_index:{url}")
        some_text = "some text"
        self.smart_search.create_index([some_text])
        self.smart_search.write_index(path_db_index)

