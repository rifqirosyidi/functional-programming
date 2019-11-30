import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', field_names=[
    'name',
    'field',
    'born',
    'nobel'
])

van = Scientist(name="Van", field="math", born=1987, nobel=True)
print(van.name)

# van.name = "Ren" # Cant Set Attribute Because it is Immutable

# Now We Can Create more Scientist

scientist = [
    Scientist(name="Van", field="math", born=1987, nobel=True),
    Scientist(name="Gery", field="math", born=1970, nobel=False),
    Scientist(name="Penn", field="physics", born=1934, nobel=False),
    Scientist(name="Ran", field="astronomy", born=1997, nobel=True),
    Scientist(name="Gen", field="chemistry", born=1967, nobel=True)

]

pprint(scientist)
print("\n")

# Now You Cant Modify the key args but you can still delete the record or add new one
del scientist[0]
pprint(scientist)

# It Because its using the list try using it with tuple
immutable_scientist = (
    Scientist(name="Van", field="math", born=1987, nobel=True),
    Scientist(name="Gery", field="math", born=1970, nobel=False),
    Scientist(name="Penn", field="physics", born=1934, nobel=False),
    Scientist(name="Ran", field="astronomy", born=1997, nobel=True),
    Scientist(name="Gen", field="chemistry", born=1967, nobel=True)
)

# del immutable_scientist[0]  # Now The Data is immutable
