import random
print ("uhodni číslo od 1 do 1000 máš na to 30 pokusů")
while True:
    print("Tak jdeme na to")
    hadane_cislo = random.randint(0,1000)
    inp = 0
    i=0
    while inp != hadane_cislo and i < 30:
        i = i + 1
        inputCheck = True
        while inputCheck:
            try:
                inp =int(input())
                inputCheck= False
            except ValueError:
                print("More napiš tam celý číslo bro")
                inputCheck = True
            except:
                print("něco se pokazilo zkus to znovu")

        if hadane_cislo < inp:
            print( random.choice(["Haha jsi L","rly?...","vy nevidíte že máte v kuchyni pneumatiku?"]))
        if hadane_cislo > inp:
            print (random.choice(["bruh","gay","da hell bro?"]))
        if hadane_cislo == inp:
            print ("Spravne bro")
        print ("bacha more už jen " + str(30-i) + " pokusů")
    print ("Konec kamo")