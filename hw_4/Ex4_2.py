import math
import concurrent.futures
import logging
import os
import time


logging.basicConfig(filename="Ex4_2_integration_log.log", level=logging.INFO, format="%(asctime)s - %(message)s")


def integrate(f, a, b, n_jobs=1, n_iter=10000000, executor_type="sync"):
    acc = 0
    step = (b - a) / n_iter
    if n_jobs == 1:
        logging.info("Starting integration with 1 job(s) inside thread/process")
        for i in range(n_iter):
            acc += f(a + i * step) * step
        return acc
    else:
        lis = [(a + i * (b - a) / n_jobs, a + (i + 1) * (b - a) / n_jobs) for i in range(n_jobs)]
        if executor_type == "ThreadPoolExecutor":
            with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
                logging.info(f"Starting integration with {n_jobs} job(s) using {n_jobs} ThreadPoolExecutor")
                futures = [executor.submit(integrate, f, a, b, n_jobs=1, n_iter=n_iter // n_jobs, executor_type="sync")
                           for (a, b) in lis]
                for future in concurrent.futures.as_completed(futures):
                    acc += future.result()
            return acc
        if executor_type == "ProcessPoolExecutor":
            with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
                logging.info(f"Starting integration with {n_jobs} job(s) using {n_jobs} ProcessPoolExecutor")
                futures = [executor.submit(integrate, f, a, b, n_jobs=1, n_iter=n_iter // n_jobs, executor_type="sync")
                           for (a, b) in lis]
                for future in concurrent.futures.as_completed(futures):
                    acc += future.result()
            return acc


if __name__ == '__main__':
    file = open("Ex4_2_threads_processes_times.txt", "w")
    cpu_num = os.cpu_count()
    n_jobs_list = range(1, cpu_num*2 + 1)

    for n_jobs_num in n_jobs_list:
        logging.info(f"n_jobs = {n_jobs_num}")
        file.write(f"n_jobs = {n_jobs_num}\n")

        start_time_threads = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs_num, n_iter=10000000, executor_type="ThreadPoolExecutor")
        file.write(f"Threads time: {time.time() - start_time_threads}\n")

        start_time_processes = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs_num, n_iter=10000000, executor_type="ProcessPoolExecutor")
        file.write(f"Process time: {time.time() - start_time_processes}\n")

    file.close()
