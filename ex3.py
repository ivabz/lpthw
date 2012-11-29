#This is an exercise in Python with mathematical oeprators. Conveniently named Counting Chickens (before they hatch. Naturally.)

print "I will now count chickens:"
print "Hens", 25.0 + 30.0 / 6.0
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0 #BODMAS in operation... First 25*3 is calculated then the result is treated with modulus % 4 to yield 3, which of course, yields 3, which when subtracted from 100 leaves us with 97
print "Now I will count the eggs."
print 3 + 2 + 1 - 5.0 + 4.0 % 2.0 - 1 / 4.0 + 6.0

#the above code shows that the equation is first read left to right and then evaluated using BODMAS

print "is it true that 3 + 2 < 5 - 7?"
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False!"

print "How about some more?"

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less than or equal?", 5<= -2

#Writing a number with an explicit decimal space defines it as a floating point value and the immediate mathematical operation performed upon it results in a floating point output
