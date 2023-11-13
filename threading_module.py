from threading import Thread
import time

def display_time(thread_name):
    while True:
        print("Now working {}".format(thread_name))
        time.sleep(3)
        print("Thread {} stopped".format(thread_name))

def neverending_counter(thread_name):
    i = 0
    while True:
        print("Now working {}".format(thread_name))
        i += 1
        time.sleep(4)
        print(i)
        print("Thread {} stopped".format(thread_name))

thread_list = []
thread_list.append(Thread(target=display_time, args=('Timer',)))
thread_list.append(Thread(target=neverending_counter, args=('Counter',)))

for x in thread_list:
    x.start()