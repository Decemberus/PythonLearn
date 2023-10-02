# -*- coding: UTF-8 -*-

from multiprocessing import Pool
import time

def Foo(i):
    time.sleep(2)
    return i + 100

def Bar(arg):
    print('-->exec done:', arg)

if __name__ == '__main__':
    pool = Pool(5)  # Allow up to 5 processes in the pool

    results = []  # Store results to pass to the callback

    for i in range(10):
        result = pool.apply_async(func=Foo, args=(i,))

        results.append(result)

    # Close the pool and wait for all processes to complete
    pool.close()
    pool.join()

    # Retrieve and print the results
    for result in results:
        result_value = result.get()  # Get the result of the corresponding process
        Bar(result_value)

    print('end')