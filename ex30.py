# Else and If

from sys import argv

script, people, cars, buses = argv

print "\npeople = %r \ncars = %r \nbuses = %r" % (people, cars, buses)

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many Buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decde."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
