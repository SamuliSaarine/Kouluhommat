def tulostaOhjeet():
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.")
    print("Anna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.")
    print("Merkkijonojen tulee olla vähintään 5 ja korkeintaan 15 merkkiä pitkiä.")
    print("Merkkijonoissa ei osaa olla merkkiä ';'.\n")

def kysyMerkkijono(KehoteModaus=""):
    return input(f"Anna {KehoteModaus}merkkijono 5-15 merkkiä (enter lopettaa): ")

def tarkistaMerkkijono(Mj):
    if(len(Mj) < 5):
        print(f"Liian lyhyt, {len(Mj)} merkkiä.")
        return False
    elif(len(Mj) > 15):
        print(f"Liian pitkä, {len(Mj)} merkkiä.")
        return False
    elif(";" in Mj):
        print("Merkkijonossa on kielletty merkki ';'.")
        return False
    else:
        return True

def tulostaMerkkijono(Merkkijono):
    if(len(Merkkijono) > 0):
        print("Annoit seuraavat hyväksytyt merkkijonot:")
        print(Merkkijono.replace(";","\n"))
    else:
        print("Et antanut yhtään hyväksyttävää merkkijonoa.")

def paaOhjelma():
    tulostaOhjeet()
    KehoteModaus = ""
    Merkkijono = ""
    Viimejono = kysyMerkkijono()

    if(tarkistaMerkkijono(Viimejono)):
        Merkkijono += Viimejono
        KehoteModaus = "seuraava "
    else:
        KehoteModaus = "uusi "

    while(len(Viimejono) > 0):
        Viimejono = kysyMerkkijono(KehoteModaus)
        
        if(len(Viimejono) == 0):
            print("")
            break
    
        if(tarkistaMerkkijono(Viimejono)):
            if(len(Merkkijono)>0):
                Merkkijono+=";"
            Merkkijono += Viimejono
            KehoteModaus = "seuraava "
        else:
            KehoteModaus = "uusi "
    
    tulostaMerkkijono(Merkkijono)
    print("Kiitos ohjelman käytöstä.")


paaOhjelma()