

from xcrawler.threads.executors.work_executor import WorkExecutor


class ExecutorFactory:
    """Creates a multi-threaded executors.

    """
    def __init__(self):
        pass

    def create_work_executor(self, config):
        work_executor = WorkExecutor(config)
        return work_executor

