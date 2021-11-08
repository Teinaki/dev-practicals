# Answer the questions below
#
#   1. What is parallelism? A complex computation can be divided into multiple parts that be run in parallel, using the CPU cores
#   2. When the following cell is executed, what is happening? 
#  creates a list of process, 5, loop through the process list, that process calls the sleeping function with an arg of 5, 
# this will print the going to sleep and sleep for 5seconds then prints woke up, process are called concurrently, loops through each process in the list, calling the perf_counter()
# also loops through with the join to block the calling process until the process is completed, then uses the perf_counter to calculate elapsed time and print that.
#   3. What does the multiprocessing function start do?
#   4. What does the multiprocessing function join do?
##########


from multiprocessing import Process
from time import perf_counter, sleep

def sleeping(secs):
    print(f'Going to sleep for {secs} second(s)')
    sleep(secs)
    print(f'Woke up after {secs} second(s)')

def main():     
    start = perf_counter()

    processes = [Process(target=sleeping, args=[5]) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')

if __name__ == '__main__':
    main()
