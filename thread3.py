from time import sleep
from threading import Thread

def print_num():
    for i in range(1,6):
        print(i)
        sleep(1)

def print_letters():
    for letter in ['a','b','c','d','e']:
        print(letter)
        sleep(1)
#create thread
t1 = Thread(target=print_num)
t2 = Thread(target=print_letters)
#start thread
t1.start()
t2.start()
#run together
t1.join()
t2.join()
