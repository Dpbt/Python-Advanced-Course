import sys
import time
import multiprocessing
import codecs


def process_main(conn_out, conn_in, messages_in, start, queue):
    for message_in in messages_in:
        conn_out.send(message_in)
    while conn_in.poll(timeout=7):
        message_recv = conn_in.recv()
        queue.put([time.time() - start, message_recv])


def process_a(conn_out, conn_in, queue):
    while conn_in.poll(timeout=0.05):
        new_massage = conn_in.recv()
        queue.put(new_massage)
    while not queue.empty():
        conn_out.send(queue.get().lower())
        time.sleep(5)


def process_b(conn_out, conn_in):
    while conn_in.poll(timeout=6):
        new_massage = conn_in.recv()
        new_massage = codecs.encode(new_massage, 'rot_13')
        conn_out.send(new_massage)


if __name__ == '__main__':
    file = open("Ex4_3_processes.txt", "w")

    messages = [line for line in sys.stdin.readlines()]

    file.write("Input from keyboard:\n")
    for message in messages:
        file.write(message)
    file.write("\n")

    a_conn1, main_conn1 = multiprocessing.Pipe()
    b_conn1, a_conn2 = multiprocessing.Pipe()
    main_conn2, b_conn2 = multiprocessing.Pipe()
    queue_a = multiprocessing.Queue()
    queue_main = multiprocessing.Queue()  # Очередь для выгрузки сообщений из main процесса,
    # так как с записью сообщений в файл внутри процесса непонятные мне проблемы

    start_time = time.time()
    main = multiprocessing.Process(target=process_main,
                                   args=(main_conn1, main_conn2, messages, start_time, queue_main,))
    pr_a = multiprocessing.Process(target=process_a, args=(a_conn2, a_conn1, queue_a,))
    pr_b = multiprocessing.Process(target=process_b, args=(b_conn2, b_conn1,))

    main.start()
    pr_a.start()
    pr_b.start()

    main.join()
    pr_a.join()
    pr_b.join()

    file.write("Output from main process:\n")

    while not queue_main.empty():
        message = queue_main.get()
        file.write(f"Message:\"{message[1].rstrip("\n")}\", Time from start: {message[0]}, \n")
