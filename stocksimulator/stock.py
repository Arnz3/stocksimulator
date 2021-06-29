import random
from time import sleep
from threading import Thread

class Stock:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.climbing = True
        self.changeValue = (1,5)
        self.updateRangeX10 = (1,50)
        self.changeRange = (5,30)
        self.changeChance = (1,2)

    def update(self):
        while True:
            if self.climbing:
                increment = random.randint(self.changeValue[0],self.changeValue[1])
                self.value += increment
            else:
                decrease = random.randint(self.changeValue[0],self.changeValue [1])
                if self.value - decrease <= 0:
                    self.value += decrease
                    self.climbing = True
                else:
                    self.value -= decrease
            sleep(round(random.randint(self.updateRangeX10[0], self.updateRangeX10[1])/10))
        
    def changeState(self):
        while True:
            sleep(random.randint(self.changeRange[0], self.changeRange[1]))
            if random.randint(self.changeChance[0],self.changeChance[1]) == 1:
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