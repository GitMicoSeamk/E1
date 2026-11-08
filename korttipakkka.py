import random
korttipakka = []

for j in range(4):
        if j == 0 :
            maa = "Pata"
        elif j == 1:
            maa = "Hertta"
        elif j == 2:
            maa = "Risti"
        elif j == 3:
             maa = "Ruutu"
        if j == 0 or j == 2:
             vari = "Musta"
        else:
             vari = "Punainen"
        for i in range(1,13):
            kortti = (maa, i, "Musta")
            korttipakka.append(kortti)
#listataan kaikki mahdolliset korttiyhdistelmät
arvottu_kortti = random.choice(korttipakka)
print(f"Arvottu kortti: {arvottu_kortti}")
#arvotaan ja printataan pakasta kortille ja arvot