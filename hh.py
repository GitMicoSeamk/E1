i = 0
while i > 10:
    print(f"While silmukassa i={i}")
    print("Morjens")
    i = i+1

for i in range(10): #0-9
    print(f"for silmukassa i={i}")


jatketaanko:str = "k"
while jatketaanko != "e": #suorittaaa niin kauan kuin käyttäjä kirjoittaa "e"
    jatketaanko = input("Jatketaanko (e lopettaa) > ")