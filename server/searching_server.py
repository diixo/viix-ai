
import logging
from server.smart_search import SmartSearch

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
logger = logging.getLogger()
#logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


path_db_index = "server/db-storage/db-index.bin"


class SearchingServer:

    def __init__(self):
        self.smart_search = SmartSearch()

    def search(self, str_reuest):
        return [], []
    
    def page_to_index(self, str_request):
        pass
