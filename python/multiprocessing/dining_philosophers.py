# https://rosettacode.org/wiki/Dining_philosophers#Python

import threading
import random
import time

# Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
#
# Deadlock is avoided by never waiting for a fork while holding a fork (locked)
# Procedure is to do block while waiting to get first fork, and a nonblocking
# acquire of second fork.  If failed to get second fork, release first fork,
# swap which fork is first and which is second and retry until getting both.
#
# See discussion page note about 'live lock'.


class Philosopher(threading.Thread):

    running = True

    def __init__(self, name, left_fork, right_fork):
        super().__init__()
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.running:
            #  Philosopher is thinking (but really is sleeping).
            time.sleep(random.uniform(3, 13))
            print(f'{self.name} is hungry.')
            self.dine()

    def dine(self):
        fork1, fork2 = self.left_fork, self.right_fork

        while self.running:
            fork1.acquire(True)  # blocking = True
            locked = fork2.acquire(False)  # blocking = False i.e. non-blocking
            if locked:  # if second fork is acquired
                break
            fork1.release()
            print(f'{self.name} swaps forks')
            fork1, fork2 = fork2, fork1  # swap forks and try again
        else:
            return
        # here after breaking out of while loop
        self.dining()  # Philosopher is eating
        fork2.release()  # after eating release the resources
        fork1.release()

    def dining(self):
        print(f'{self.name} starts eating')
        time.sleep(random.uniform(1, 10))
        print(f'{self.name} finishes eating and leaves to think.')


def dining_philosophers():

    forks = [threading.Lock() for _ in range(5)]
    philosopher_names = ('Aristotle', 'Kant', 'Buddha', 'Marx', 'Russel')

    philosophers = [Philosopher(philosopher_names[i], forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(100)
    Philosopher.running = False
    print("Now we're finishing.")


if __name__ == '__main__':
    dining_philosophers()
