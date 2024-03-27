import time
from threading import Thread
from multiprocessing import Process


def fib_number(n):
    fib1 = 0
    fib2 = 1
    num = 0
    while num < n - 2:
        fib_sum = fib1 + fib2
        fib1, fib2 = fib2, fib_sum
        num += 1
    return fib2


if __name__ == '__main__':
    file = open("Ex4_1_threads_processes_sync_times.txt", "w")
    n_f = 1000000

    start_time_threads = time.time()
    threads = [Thread(target=fib_number, args=(n_f,)) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    file.write(f"10 Therads time: {time.time() - start_time_threads}\n")

    start_time_processes = time.time()
    processes = [Process(target=fib_number, args=(n_f,)) for _ in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    file.write(f"10 Processes time: {time.time() - start_time_processes}\n")

    start_time_sync = time.time()
    for i in range(10):
        fib_number(n_f)
    file.write(f"10 sync time: {time.time() - start_time_sync}\n")
