#-----------------------------------------------------------------
#Reading and writing files - a simple text editor!!
#-----------------------------------------------------------------

from sys import argv

script, filename = argv

# Open the file in read mode first - Adi's avoidance of nasty accidents
print "Opening the file %r" % filename
target = open(filename, 'r')

# Prompt user about next actions
print "We are going to erase %r." % filename
raw_input("Hit RETURN to review the contents of the file...")
print target.read()

# Prompt user to continue with erase (truncate) or abort
# Note: ^C is a keybord interrupt that force-exits the program
print "If you don't want to erase file %r, hit CTRL-C (^C)." %filename
print "If you do want to earase it, hit RETURN."
raw_input("?")

# Open the file in 'w+' mode... 
# The 'w+' mode first truncates the file and then allows writes into it
print "Truncating the file. Goodbye..."
target = open(filename, 'w+')
print ("Now your file %r looks like this \n %r \n") %(filename, target.read())

# Get user's input to write into the file
print "Now I am going to ask you for three lines..."
raw_input("Hit RETURN to proceed to add stuff to the file.")

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "I am going to write these to the file..."
all_lines = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(all_lines) 
#NOTE: write() can take only ONE argument at a time

#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# Close "target" file to ensure it is closed for more reads or writes
print ("And finally, we close it.")
target.close()
