# Making Decisions

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

prompt = ">"

door = raw_input(prompt)

if door == "1":
    print "Giant bear eating cheese cake. What to do?"
    print "1. Take cake?"
    print "2. Scream at bear?"

    bear = raw_input(prompt)

    if bear == "1":
        print "Ayyo. Bear ate your face."
    elif bear == "2":
        print "Ayyo! Bear ate your legs."
    else:
        print "Good you did %s. Rascala bear ran away." % bear

elif door == "2":
    print "You're looking at Rajni."
    print "1. Rascala."
    print "2. Dichkaaaon."
    print "3. Mind it."

    rajni = raw_input(prompt)

    if rajni == "1" or rajni == "2":
        print "Bye bye! You are vapourised."
    else:
        print "Consider yourself warned."

else:
    print "Safe!"
