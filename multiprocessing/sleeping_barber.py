# Based on code from https://github.com/Nohclu/Sleeping-Barber-Python-3.6-/blob/master/barber.py
import time
import random
import threading
from queue import Queue

EVENT = threading.Event()  # Event flag, keeps track of Barber/Customer interactions


class Shop:
    open = True
    seats = 15
    num_barbers = 3
    earnings = 0

    def __init__(self):
        self.barbers = []



class Customer(threading.Thread):  # Producer Thread
    customer_types = ["adult", "senior", "student", "child"]
    customer_rates = {"adult": 16,
                      "senior": 7,
                      "student": 10,
                      "child": 7}

    def __init__(self, queue: Queue) -> None:  # Constructor passes Global Queue (all_customers) to Class
        super().__init__()
        self.queue = queue
        self.rate = self.determine_rate()

    @staticmethod
    def determine_rate() -> int:
        t = random.choice(Customer.customer_types)
        print(t + " rate.")
        return Customer.customer_rates[t]

    def run(self):
        if not self.queue.full():  # Check queue size
            EVENT.set()  # Sets EVENT flag to True i.e. Customer available in the Queue
            EVENT.clear()  # Alerts Barber that there is a Customer available in the Queue
        else:
            # If Queue is full, Customer leaves.
            print("Queue full, customer has left.")

    def trim(self):
        print("Customer haircut started.")
        a = 3 * random.random()  # Retrieves random number.
        time.sleep(a)
        payment = self.rate
        # Barber finished haircut.
        print(f"Haircut finished. Haircut took {a}")
        # global Earnings
        Shop.earnings += payment


class Barber(threading.Thread):  # Consumer Thread
    def __init__(self, queue: Queue) -> None:  # Constructor passes Global Queue (all_customers) to Class
        super().__init__()
        self.queue = queue
        self.sleep = True  # No Customers in Queue therefore Barber sleeps by default

    def is_empty(self):  # check if customer in Queue
        if self.queue.empty():
            self.sleep = True  # if nobody in Queue Barber sleeps.
        else:
            self.sleep = False  # else he wakes up
        print(f"------------------\nBarber sleep {self.sleep}\n------------------")

    def run(self):
        while Shop.open:
            while self.queue.empty():
                # Waits for the Event flag to be set, Can be seen as the Barber Actually sleeping.
                EVENT.wait()
                print("Barber is sleeping...")
            print("Barber is awake.")
            customer = self.queue
            self.is_empty()
            # FIFO Queue So first customer added is gotten.
            customer = customer.get()
            customer.trim()  # Customers Hair is being cut
            customer = self.queue
            customer.task_done()
            print(self.name)  # Which Barber served the Customer


def wait():
    time.sleep(1 * random.random())


if __name__ == '__main__':
    shop = Shop()
    Shop.earnings = 0
    Shop.open = True
    all_customers = Queue(Shop.seats)  # A queue of size Customer Seats

    for _ in range(Shop.num_barbers):
        barber = Barber(all_customers)
        # Makes the Thread a super low priority thread allowing it to be terminated easier
        barber.daemon = True
        barber.start()  # Invokes the run method in the Barber Class
        # Adding the Barber Thread to an array for easy referencing later on.
        shop.barbers.append(barber)
    for _ in range(10):  # Loop that creates infinite Customers
        print("----")
        # Simple Tracker to see the qsize (NOT RELIABLE!)
        print(all_customers.qsize())
        wait()
        customer = Customer(all_customers)  # Passing Queue object to Customer class
        all_customers.put(customer)  # Puts the Customer Thread in the Queue
        customer.run()

    all_customers.join()  # Terminates all Customer Threads
    print("€" + str(Shop.earnings))
    Shop.open = False
    for i in shop.barbers:
        i.join(timeout=1)  # Terminates all Barbers
        # Program hangs due to infinite loop in Barber Class, use ctrl-z to exit.
