pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    new_world=original+original[1]+pyg
    new_world=new_world[1:len(new_world)]
    print new_world
else:
    print 'empty'