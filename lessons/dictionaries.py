"""Demonstrates dictionary capabilities."""


schools: dict[str, int]

schools = dict()

schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

print(f"UNC has {schools['UNC']} students")

schools.pop("Duke")

if "Duke" in schools:
    print("Found key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dicitonary literal
schools = {}  # same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400, 
    "Duke": 6717, 
    "NCSU": 26150}

print(schools)

# EX of a key error
# print(schools["UNCC"])

# Q21

for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")