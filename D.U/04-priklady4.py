R = int(input("Aký je rok:"))
M = int(input("Aký je mesiac:"))
D = int(input("Aký je deň v mesiaci je:"))
a = ((R * 365) + (M * 30) + D) - 2009 * 365
b = a * 24
c = b **60
print(f"Od zavedenia eura uplynulo: {a} dní")
print(f"Od zavedenia eura uplynulo: {b} dní")
print(f"Od zavedenia eura uplynulo: {c} sekúnd")


