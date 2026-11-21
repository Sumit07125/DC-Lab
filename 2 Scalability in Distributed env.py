import time
import random
from queue import Queue
from threading import Thread

def worker(q, worker_id):
    while True:
        task = q.get()
        if task is None:
            q.task_done()
            break

        print(f"Worker {worker_id} processing: {task}")
        time.sleep(random.uniform(1, 3))
        print(f"Worker {worker_id} finished: {task}")
        q.task_done()

def main():
    q = Queue()
    threads = []

    for i in range(2):
        t = Thread(target=worker, args=(q, i))
        t.start()
        threads.append(t)

    for i in range(5):
        q.put(f"Task {i}")

    q.join()

    for _ in threads:
        q.put(None)

    q.join()

    for t in threads:
        t.join()

    print("All tasks processed.")

if __name__ == "__main__":
    main()