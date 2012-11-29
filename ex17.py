# More Files

from sys import argv
from os.path import exists

#Get script, from file and to file at the command line
script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

# we could do these on one line too, how?
    # input = open(from_file)
    # indata = input.read()
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CRTL+C to abort."
raw_input(">")

output = open(to_file,'a')
output.write(indata)
output = open(to_file, 'r')

print "This is the combined file %r" % output.read()

print "\nAlright, all done"

output.close()
#indata.close()
