scientist = [
    {
        'name': 'Vin',
        'field': 'math',
        'born': '1998',
        'nobel': False
    }, {
        'name': 'Gery',
        'field': 'math',
        'born': '1986',
        'nobel': False
    }, {
        'name': 'Penn',
        'field': 'chemistry',
        'born': '1987',
        'nobel': True
    }, {
        'name': 'Then',
        'field': 'physics',
        'born': '1952',
        'nobel': True
    }, {
        'name': 'Carl',
        'field': 'astronomy',
        'born': '1930',
        'nobel': False
    }
]

print(scientist)

# We don't want to change the dictionary dat, for example
scientist[0]["name"] = "Ran"
print(scientist)

# While the main principle of functional programming is you might work with immutable data sets

# Using Collection

