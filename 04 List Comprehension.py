import collections
from pprint import pprint

Scientist = collections.namedtuple("Scientist", field_names=[
    'name',
    'field',
    'born',
    'nobel'
])

immutable_scientist = (
    Scientist(name="Van", field="math", born=1987, nobel=True),
    Scientist(name="Gery", field="math", born=1970, nobel=False),
    Scientist(name="Penn", field="physics", born=1934, nobel=False),
    Scientist(name="Ran", field="astronomy", born=1997, nobel=True),
    Scientist(name="Gen", field="chemistry", born=1967, nobel=True),
    Scientist(name="Ann", field="physics", born=1974, nobel=True),
    Scientist(name="Ron", field="physics", born=1977, nobel=False),
)

# Filtering with list comprehension
filtered = tuple(x for x in immutable_scientist if x.nobel == True)
pprint(filtered)
