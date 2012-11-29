#-----------------------------------------------------------------
# Reading Files
#-----------------------------------------------------------------

# Tell python it needs to import argument variables from system
# (i.e. from the command line)
from sys import argv 

# Tell the import method how many argument variables in needs to get
script, filename = argv

# Use method open(...) to return the object of type file that was
# specified in the argument variable "filename"
# Then bind a variable "txt" to value of the file object and print stuff
txt = open(filename)
print "Here's your file %r:" % filename
print "This is the value of the Object 'txt': %r" % txt
print txt.read()

# Ask user for input at the command line and binds a variable to it
print "Type that filename again:"
file_again = raw_input("> ")

# The method open(file_again) tries to match the string, bound to
# the variable file_again, with the file names of files contained
# in the current directory. If it finds a match, then it returns
# the value of the object file_name with additional default parameters
# of the method open()
txt_again = open(file_again)

print "This is the value of the object bound to txt_again: %r" % txt_again

# The method read() locates the object pointed to by txt_again and 
# attempts to read it
print txt_again.read()

# The file.close() method ensures that the files associated with 
# the variables "txt" and "txt_again" cannot be read 
# or written to anymore.
txt.close()
txt_again.close()
