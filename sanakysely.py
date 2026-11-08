import random
sanasto = {"auto":"bil","leipä":"bröd", "juusto":"ost", "kakku":"kaka", "kala":"fisk", "lintu":"fågel",
           "porkkana":"morot", "punajuuri":"rödbeta", "silta":"bro", "kirja":"bok"}
#sanojen lista
avaimet_listana = list(sanasto.keys())
oikeat = 0
vaarat = 0
#määritetään arvot oikeille ja väärille
for i in range(10):
    kysyttava_sana = random.choice(avaimet_listana)
    vastattu_sana = input(f"Kirjoita vastaus: '{kysyttava_sana}' ruotsiksi >")
#kysytään sanaa


    if vastattu_sana == sanasto[kysyttava_sana]:
        oikeat += 1
        print("Oikein meni!")
        avaimet_listana.remove(kysyttava_sana)
    else:
        vaarat += 1
        print("Yritä uudelleen")
#määritetään onko vastaus oikein vai väärin
        
