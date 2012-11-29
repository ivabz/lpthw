# Dictionaries, oh lovely dictionaries

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

def print_cities():
    print cities, "--> The current city Dictionary. Hit enter to proceed."
    raw_input()

print_cities()

cities['NY'] = 'New York'
print "I added cities['NY'] --> ", cities['NY']
print_cities()

cities['OR'] = 'Portland'
print "I added cities['OR'] --> ", cities['OR']
print_cities()

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not Found."

#ok, pay attention!!!
cities['_find'] = find_city

while True:
    print "State? (ENTER to Quit)",
    state = raw_input("> ")

    if not state: break

    #this is the most important line ever... Study!!!
    city_found = cities['_find'](cities, state)
    print city_found
