from time import sleep
from threading import Thread

class A(Thread):
    def run(self):
        for i in range(3):
            print("me")
            sleep(1)

class B (Thread):
    def run(self):
        for i in range(3):
            print("you")
            sleep(1)
#create thread
t1 = A()
t2 = B()

#start thread
t1.start()
t2.start()

#run together
t1.join()
t2.join()
