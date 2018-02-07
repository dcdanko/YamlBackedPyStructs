from yaml_backed_structs import PersistentDict, PersistentSet
from sys import exit

pdict = PersistentDict('my-path.yml')
pdict['a'] = 1 # this will automatically be saved
pdict['b'] = []
pdict['b'].append(2) # this will not be saved automatically
pdict.save() # but we can save it like this

del pdict

pdict = PersistentDict('my-path.yml')

if pdict['a'] != 1:
    exit(2)

if pdict['b'][0] != 2:
    exit(3)
