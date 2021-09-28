"""Example of for in syntax."""

names: list[str] = ["Laura", "Kat", "Bestie", "Lizzo"]

i: int = 0
print("while output")
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("forin output")
for name in names:
    print(name)
