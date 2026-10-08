#!/usr/bin/python3
dna = input("Введите ДНК: ").upper()
print(f"A: {dna.count('A')}")
print(f"T: {dna.count('T')}")
print(f"G: {dna.count('G')}")
print(f"C: {dna.count('C')}")
complement = dna.translate(str.maketrans("ATCG", "TACG"))
print(f"Комплиментарная ДНК: {complement}")
