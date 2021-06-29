import random
from time import sleep
from threading import Thread

class Stock:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.climbing = True

    def update(self):
        while True:
            if self.climbing:
                increment = random.randint(1,5)
                self.value += increment
            else:
                decrease = random.randint(1,5)
                if self.value - decrease <= 0:
                    self.value += decrease
                    self.climbing = True
                else:
                    self.value -= decrease
            sleep(round(random.randint(1, 50)/10))
        
    def changeState(self):
        while True:
            sleep(random.randint(5, 30))
            if random.randint(1,2) == 1:
                self.climbing = True
            else:
                self.climbing = False
        

    def start(self):
        valueThread = Thread(target=self.update)
        changeThread = Thread(target=self.changeState)
        changeThread.start()
        valueThread.start()

stock = Stock("Tesla")
stock.start()
while True:
    print(stock.value)