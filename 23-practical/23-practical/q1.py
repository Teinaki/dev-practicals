# Answer the questions below
# 1. What is concurrency? 
# If our process is waiting on I/O, Concurrency does something else while waiting
# 2. What is the difference between CPU bound & I/O bound? 
# Waiting for I/O (I/O bound), Heavy computational load (CPU bound)
# 3. When the following code is executed, what is happening?
#  creates a list of threads, 5, loop through the thread list, that thread calls the sleeping function with an arg of 5, 
# this will print the going to sleep and sleep for 5seconds then prints woke up, threads are called concurrently, loops through each thread in the list, calling the perf_counter()
# also loops through with the join to block the calling threads until the thread is completed, then uses the perf_counter to calculate elapsed time and print that.
# 4. The Thread object s constructed below with two arguments. What are these
#    arguments & their purpose? target is the function and args is the arguments passed to the function
# 5. What does the threading function start do? Once a thread object is created, its activity must be started by calling the thread’s start() method
# 6. What does the threading function join do? Join is a synchronization method that blocks the calling thread (that is, the thread that calls the method) until the thread whose Join method is called has completed
##########

from threading import Thread
from time import perf_counter, sleep

def sleeping(secs):
    print(f'Going to sleep for {secs} second(s)')
    sleep(secs)
    print(f'Woke up after {secs} second(s)')

def main():
    start = perf_counter()

    threads = [Thread(target=sleeping, args=[5]) for _ in range(5)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')

if __name__ == '__main__':
    main()
