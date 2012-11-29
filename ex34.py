# Accessing Elements of Lists

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "The 1st animal is a bear and is found at index 0 --> ", animals[0]
print "The 2nd animal is a python and is found at index 1 --> ", animals[1]
print "The 3rd animal is a peacock and is found at index 2 --> ", animals[2]
print "The 4th animal is found at index 3. It is a kangaroo --> ", animals[3]
print "The 5th animal is found at index 4. It is a whale --> ", animals[4]
print "The 6h animal is found at index 5. It is a platypus --> ", animals[5]
print "In a list[..] of 'n' items, the index starts at 0 and finishes at n-1. If we try to access element linst[n], python will throw an error."
print "In a list of 6 animals, asking for animals[6] will throw an IndexError BECAUSE the index does not exist.", animals[6]
