import _thread
import time


def print_time(thread_name, delay):
    # count = 0

    while 1:
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))

    '''
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))
    '''


try:
    _thread.start_new_thread(print_time, ("thread_01", 1,))
    _thread.start_new_thread(print_time, ("thread_02", 3,))
except:
    print("线程启动异常")

while 1:
    pass
