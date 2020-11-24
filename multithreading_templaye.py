import threading

def thread_1():
    print("Code 1")

def thread_2():
    print("Code 2")

# declaring and starting threads

thread_1 = threading.Thread(target=thread_1)
thread_2 = threading.Thread(target=thread_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
