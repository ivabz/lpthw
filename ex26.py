# Congratulations, Take a Test! - Fix someone else's code.

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #added missing colon to define function
    """Prints the first word after popping it off."""
    word = words.pop(0) #pop() was mis-spelled as poop()
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # added closing paren ")" and corrected "pop("
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #Corrected dived by sign from "\" to "/"
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #Fixed assignment "==" to "=" and changed hypen to underscore in variable name start_point

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do it this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) #Fixed spelling of start_point and added closing brace


sentence = "All good things come to those who wait." #Removed \t and fixed spellings

words = break_words(sentence) #Removed ex25. <-- the method belongs in this fle itself
sorted_words = sort_words(words) #Removed ex25. <-- the method belongs in this file itself

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #removed "." from beginning of statement
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) #Removed ex25. <-- the method belongs in this file itself

print sorted_words #Fixed command "prin" to "print"

print_first_and_last(sentence) #Fixed spelling "irst" to "first"

print_first_and_last_sorted(sentence) #Removed indentation, fixed spelling "a" to "and" and "senence" to "sentence"


