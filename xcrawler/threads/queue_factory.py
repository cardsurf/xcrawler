
try:
    import Queue as queue
except ImportError:
    import queue


class QueueFactory:
    """Creates a queue of threads.

    """
    def __init__(self):
        pass

    def create_queue(self):
        instance_queue = queue.Queue()
        return instance_queue
