# Intro to "The Gothons are getting Classy"

class theThing(object):

    def __init__(self, number = 0):
        self.number = number
        
    def some_function(self):
        print "I got called."

    def add_me_up(self, more):
        self.number += more
        return self.number

# two different things
a = theThing()
b = theThing()

a.some_function()
b.some_function()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(30)
print b.add_me_up(30)

print a.number
print b.number
