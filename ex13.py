#Parameters, Unpacking, Variables

from sys import argv

script, first, second, third = argv

extra_variable = raw_input("Enter yet another value: --> ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "This is an extra variable:", extra_variable

# IMPORTANT NOTE:
# See output and then look at the first import: 
# "from sys import argv"
# It says import argument variable(s) ARGV from SYSTEM (sys).
# The next line tells Python that four variables should initialized to successive values of argv.
# Python will expect four values at the command line, seperated by a white space.
# Therefore, it includes **all** the arguments typed at the command line **including** the system path pointed to by the script name (ex13.py). BECAUSE the script is itself an argument to Python.
