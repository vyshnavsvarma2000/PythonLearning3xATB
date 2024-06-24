#real example of decorator
import time
def note_time_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time taken is ", str(end_time-start_time))
    return wrapper
@note_time_decorator
def time_func():
    time.sleep(5)
    print(" print logs of time taken")
time_func()
@note_time_decorator
def reporting_time():
    time.sleep(2)
    print("Report time taken ")
reporting_time()