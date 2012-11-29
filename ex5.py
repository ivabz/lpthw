my_name = 'Aditya Athalye' # String has been assigned in single quotes
my_age = 29 #not a lie
my_height = 5.5 #feet
my_weight = 74 #kilos
my_eyes = 'Light Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %r feet tall." % my_height
print "He's %d kilos heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# the modulus % is used to specify some data type or variable is going to appear next... %s is a string and %d is a digit... specify with no space for better readability.

print "If I add %d, %r, and %d I get %r." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Let's talk about %s (my name) %s (my age) and %s (my height)" % (my_name, my_age, my_height)

