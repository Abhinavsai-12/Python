# '''
# Process:
# The process is a program (set of instructions) in execution
# Process cannot share the memory


# Thread:
# Thread is light-weight processes
# Threads can be used to perform complicated tasks in the background without interrupting the main program.
# Threads can Share the memory






# run():is the entry point for a thread.

# start():method starts a thread by calling the run method.

# join([time]):waits for threads to terminate.

# isAlive():method checks whether a thread is still executing.

# getName():method returns the name of a thread.

# '''



# import threading
# from threading import * 
# from time import sleep 

# class First_thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 1st Thread")
#             sleep(2)

# class Second_thread(Thread):
#     def run(self):
#         for i in range(1,10):
#             print(i,"This is 2nd Thread")
#             sleep(2)
           

# t1=First_thread()
# t2=Second_thread()

# t1.start()
# print(t1.is_alive())
# t2.start()
# print(t2.is_alive())
# t1.join()
# t2.join()
# print(t1.is_alive())
# print(t2.is_alive())


# import threading
# print(threading.current_thread().getName())


