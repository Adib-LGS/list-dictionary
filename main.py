# -----------------------Using Dictionary Basic----------------------------
people = {"name": "John", "familly name": "Rambo", "age": 35}

# rename value of key name
print(people['name'])
people['name'] = 'Elyagfuk'
print()

print(people['name'])
print()

# append key + value
people['Job'] = "WebDev"
print(people)
print()

# add a tupple
language = ("Python", "JSES6", "PHP")
people['language'] = language
print(people)
print()

# show all dictionary's key
for i in people:
    print(f"Key: {i} // Value: {people[i]}")
print()

# show all data in specific key
for i in people['language']:
    print(i)
print()

# -----------------------DATA TRAITEMENT----------------------------

# List traitement
police_profiles = [
    ("Elya", 45, 170),
    ("Monic", 27, 157),
    ("Simonac", 69, 192),
    ("Perz", 16, 183)
]


def get_info(name, listing):
    for x in listing:
        if x[0] == name:
            return x
    return None


infos = get_info('Elya', police_profiles)
print(infos)
print()

# Dictionary traitement we can found instantly the info via key name

police_officers = {
    "john": (45, 170),
    "maria": (27, 157),
    "Sally": (69, 192),
    "Peter": (16, 183)
}

# .get() == avoid error message in case of missing
infos_officers = police_officers.get('john')
if not infos_officers:
    print("Key doesn't exist")
else:
    print(infos_officers)
