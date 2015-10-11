
from xcrawler.threads.page_processor import PageProcessor
from xcrawler.threads.item_processor import ItemProcessor


class ThreadFactory(object):
    """Creates a thread.

    """
    def __init__(self):
        pass

    def create_page_processor(self, config, page_queue, item_queue):
        thread = PageProcessor(config, page_queue, item_queue)
        return thread

    def create_item_processor(self, config, item_queue):
        thread = ItemProcessor(config, item_queue)
        return thread

