# What If

people = int(raw_input("How may people? --> "))
cats = int(raw_input("How may cats? --> "))
dogs = int(raw_input("How may dogs? --> "))

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <=dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are equal to dogs."
