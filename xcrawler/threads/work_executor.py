
try:
    import Queue as queue
except ImportError:
    import queue

from xcrawler.threads.thread_factory import ThreadFactory


class WorkExecutor(object):
    """Manages a process of visiting web pages.
    
    """
    def __init__(self,
                 config,
                 page_queue=queue.Queue(),
                 item_queue=queue.Queue(),
                 thread_factory=ThreadFactory()):
        self.config = config
        self.page_queue = page_queue
        self.item_queue = item_queue
        self.item_processor = None
        self.thread_factory = thread_factory
        self.spawn_worker_threads()

    def spawn_worker_threads(self):
        self.spawn_page_queue_threads()
        self.spawn_item_queue_thread()
    
    def spawn_page_queue_threads(self):
        for _ in range(self.config.number_of_threads):
            t = self.thread_factory.create_page_processor(self.config, self.page_queue, self.item_queue)
            t.daemon = True
            t.start()
            
    def spawn_item_queue_thread(self):
            self.item_processor = self.thread_factory.create_item_processor(self.config, self.item_queue)
            self.item_processor.daemon = True
            self.item_processor.start()
        
    def execute_work(self, start_pages):
        self.item_processor.open_output_file_if_needed()
        self.add_pages_to_queue(start_pages)
        self.wait_until_work_is_done()
        self.item_processor.close_output_file_if_needed()
    
    def add_pages_to_queue(self, start_pages):
        for page in start_pages:
            self.page_queue.put(page)

    def wait_until_work_is_done(self):
        self.page_queue.join()
        self.item_queue.join()




class WorkExecutorFactory(object):
    """Creates an instance of the WorkExecutor class.

    """
    def __init__(self):
        pass

    def create_work_executor(self, config):
        work_executor = WorkExecutor(config)
        return work_executor
