# The Gothons Are Getting Classy

from sys import exit
from random import randint

class Game(object):

    def __inti__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
        ]
        self.start = start

    def play(self):
        next = self.start
        
        while True:
            print "\n-----------"
            room = getattr(self, next)
            next = room()
    
