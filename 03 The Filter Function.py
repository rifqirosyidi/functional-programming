import collections
from pprint import pprint

Scientist = collections.namedtuple("Scientist", field_names=[
    "name",
    "field",
    "born",
    "nobel"
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

# filtered = filter(lambda x: x.nobel is True, immutable_scientist)
# print(next(filtered))
# print(next(filtered))
# print(next(filtered))
# print(next(filtered))

# Directly Creating New Tuple Filteded

filtered_tuple = tuple(filter(lambda x: True, immutable_scientist))  # Filter Not Applied
pprint(filtered_tuple)

print("\nFiltered Physics")
physics_only = tuple(filter(lambda x: x.field == "physics", immutable_scientist))
pprint(physics_only)


# Creating Your own function
def nobel_filter(x):
    return x.nobel is True


def after_1980(x):
    return x.born >= 1980


print("\nNobel Filter")
pprint(tuple(filter(nobel_filter, immutable_scientist)))

print("\nAfter 1980")
pprint(tuple(filter(after_1980, immutable_scientist)))