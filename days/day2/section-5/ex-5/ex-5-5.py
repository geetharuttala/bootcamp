from multiprocessing import Process

def compute():
    print("Running in a separate process")

p = Process(target=compute)
p.start()
p.join()
