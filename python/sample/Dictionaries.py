SUITCASE =[] 
SUITCASE.append("sunglasses")

# Your code here!
SUITCASE.append("shoes")
SUITCASE.append("gloves")
SUITCASE.append("pens")

LIST_LENGTH = len(SUITCASE)  # Set this to the length of suitcase

print "There are %d items in the suitcase." % (LIST_LENGTH)
print SUITCASE


animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!

animals.insert(duck_index,"cobra")

print animals # Observe what prints after the insert operation


# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin']='Penguin'



print zoo_animals