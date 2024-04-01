import time
import multiprocessing
from threading import Thread
import codecs


def process_main(conn_out, conn_in, start, queue):
    def sending():
        stdin = open(0)
        for line in stdin:
            conn_out.send(line)
            queue.put(f"Time from start:{time.time() - start}: process_main sent \"{line[:-2]}\"\n")

    def printing():
        while conn_in.poll(timeout=60):
            message_recv = conn_in.recv()
            queue.put(f"Time from start:{time.time() - start}: process_main get \"{message_recv[:-2]}\"\n")

    therad_sending = Thread(target=sending, args=())
    therad_printing = Thread(target=printing, args=())
    therad_sending.start()
    therad_printing.start()
    therad_sending.join()
    therad_printing.join()


def process_a(conn_out, conn_in, start, queue):
    def getting():
        while conn_in.poll(timeout=60):
            new_message = conn_in.recv()
            queue.put(new_message)

    def sending():
        while not queue.empty():
            message_out = queue.get()
            conn_out.send(message_out)
            time.sleep(5)

    therad_getting = Thread(target=getting, args=())
    therad_getting.start()
    while therad_getting.is_alive():
        therad_sending = Thread(target=sending, args=())
        therad_sending.start()
        therad_sending.join()
    therad_getting.join()


def process_b(conn_out, conn_in, start):
    while conn_in.poll(timeout=60):
        new_massage = conn_in.recv()
        new_massage = codecs.encode(new_massage, 'rot_13')
        conn_out.send(new_massage)


if __name__ == '__main__':
    file = open("Ex4_3_processes.txt", "w")

    a_conn1, main_conn1 = multiprocessing.Pipe()
    b_conn1, a_conn2 = multiprocessing.Pipe()
    main_conn2, b_conn2 = multiprocessing.Pipe()
    queue_a = multiprocessing.Queue()
    queue_main = multiprocessing.Queue()  # Очередь для выгрузки сообщений из main процесса,
    # так как с записью сообщений в файл внутри процесса непонятные мне проблемы

    start_time = time.time()
    main = multiprocessing.Process(target=process_main,
                                   args=(main_conn1, main_conn2, start_time, queue_main,))
    pr_a = multiprocessing.Process(target=process_a, args=(a_conn2, a_conn1, start_time, queue_a,))
    pr_b = multiprocessing.Process(target=process_b, args=(b_conn2, b_conn1, start_time,))

    main.start()
    pr_a.start()
    pr_b.start()

    main.join()
    pr_a.join()
    pr_b.join()

    while not queue_main.empty():
        message = queue_main.get()
        file.write(message)
