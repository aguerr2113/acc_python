import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    def get_sideup(self):
        return self.sideup
        

def main():
    mycoin = Coin()

    print('This sideis up :', mycoin.get_sideup())

    print('I am tossing the coin...')

    mycoin.toss()

    print('This side is up:' , mycoin.get_sideup())

main()