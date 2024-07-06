import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

COUNT = 200000000
SLEEP = 10


def io_bound(sec):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{pid} * {process_name} * {thread_name} ---> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {process_name} * {thread_name} ---> Fnish sleeping...")


def cpu_bound(n):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{pid} * {process_name} * {thread_name} ---> Start counting...")
    while n > 0:
        n -= 1

    print(f"{pid} * {process_name} * {thread_name} ---> Fnish counting...")


def part1():
    io_bound(SLEEP)
    io_bound(SLEEP)


def part2():
    t1 = Thread(target=io_bound, args=(SLEEP,))
    t2 = Thread(target=io_bound, args=(SLEEP,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def part3():
    cpu_bound(COUNT)
    cpu_bound(COUNT)


def part4():
    t1 = Thread(target=cpu_bound, args=(COUNT,))
    t2 = Thread(target=cpu_bound, args=(COUNT,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def part5():
    p1 = Process(target=cpu_bound, args=(COUNT,))
    p2 = Process(target=cpu_bound, args=(COUNT,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def part6():
    p1 = Process(target=io_bound, args=(SLEEP,))
    p2 = Process(target=io_bound, args=(SLEEP,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def main():
    start = time.time()
    # Start
    # part1()
    # part2()
    # part3()
    # part4()
    # part5()
    # part6()
    # End
    end = time.time()
    print("Time taken in seconds - ", end - start)


if __name__ == "__main__":
    main()
