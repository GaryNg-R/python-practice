import time
import logging
from concurrent.futures import ThreadPoolExecutor
import threading
import random


def process_recod():
    print('do something')


def task():
    print("Executing our Task")
    result = 0
    i = 0
    for i in range(10):
        result = result + i
    print("I: {}".format(result))
    print("Task Executed {}".format(threading.current_thread()))


def main():
    log_name = "bot.log"
    total_lines = 0
    start_time = time.time()

    logging.basicConfig(filename=log_name, level=logging.DEBUG,
                        format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.info('Log Entry Here.')

    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)


if __name__ == '__main__':
    main()


# https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/
