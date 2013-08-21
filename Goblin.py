import random
b="enderdragon"
bhp = 1500
schaden = 4
maxschaden = 100
runde = 0
kritt = 0.2
drachenaktion = ["feuer",
                 "klaue",
                 "biss"]
menu = ["Normaler Angriff",
        "Ultimativer Angriff",
        "Deckung gehen",
        "Ausweichen",
        "Verstecken",
        "Heiltrank",
        "Beenden"]

while bhp > 0:
    runde = runde + 1 
    print ("autsch!",b,"hatt noch",bhp,"leben übrig")
    while True:
        for x in menu:
            print (menu.index (x),x)
        x = input("drücke enter")
        print()
        if x <"0" or x > "6" or len (x)>1:
            print ("Falsche Eingabe!!")
            continue 
        else:
            print ("Brav")
            break
    if x == "0":
        print ("goblin greift an! runde:",runde)
        schaden = random.randint(0,maxschaden)
        print (b,"erleidet",schaden,"schaden")
        bhp = bhp-schaden
    elif x == "1" :
        print ("Du versuchst den Ultimativen Angriff")
        treffer = random.random()
        if treffer < kritt:
            print ("Ulti geglückt")
            schaden = maxschaden * 4
            print (b,"erleidet",schaden,"schaden")
            bhp = bhp-schaden
        else:
            print ("Ulti verschwendet")


    elif x == "6":
        break
    #drache schlägt zurück
    aktion = random.choice(drachenaktion)
    if aktion == "feuer":
         print ("der drache spuckt feuer")
    elif aktion == "klaue":
        print ("der drache schlägt nach dir")
    elif aktion == "biss":
        print ("der drache schnappt nach dir")
     
    
