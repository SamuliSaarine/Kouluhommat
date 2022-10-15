#Ohjelma kirjoittaa luettavan tiedoston kaikki palindromit uuteen tiedostoon.
#Ohjelma hylkää tarkastuksessa kaikki rivit, joissa on # tai numeroita tai niiden pituus ei ole yli 3 merkkiä.
#Ohjelma ei huomioi tarkastuksessa välilyöntejä, välimerkkejä tai isoja kirjaimia.

def EiOK(Rivi):
    print(f"Ei OK: '{Rivi}'")

def OnkoPalindromi(Rivi=""):
    #Poistetaan rivinvaihto tarkastuksesta.
    Rivi = Rivi[:-1]
    #Tarkastetaan pituus.
    if(len(Rivi)<3):
        EiOK(Rivi)
        return None
    r = ""
    #Käydään läpi merkkijonon kaikki merkit.
    for i in range (0, len(Rivi)):
        m = Rivi[i]
        if(m.isdigit() or m=="#"):
            #Hylätään merkkijono jos siinä on kielletty merkki.
            EiOK(Rivi)
            return None
        elif(m.isalpha()):
            #Lisätään aakkoset uuteen merkkijonoon.
            r+=m

    #Ei oteta huomioon isoja kirjaimia.
    r=r.lower()
    #Katsotaan onko merkkijono palindromi.
    if(r == r[::-1]):
        print(f"OK: '{Rivi}'")
        return Rivi, r
    else:
        EiOK(Rivi)
        return None 

def Lue(LuettavaTiedosto):
    Td = open(LuettavaTiedosto, "r", encoding="UTF-8") 
    Palindromit = []
    #Käydään tiedoston kaikki merkkijonot läpi tyhjään riviin asti.
    while(True):
        Rivi = Td.readline()
        if(len(Rivi)==0):
            break
        #Jos merkkijono on palindromi, se lisätään palindromilistaan.
        Pld = OnkoPalindromi(Rivi)
        if(Pld is not None):
            Palindromit.append(Pld)
    Td.close()
    return Palindromit

def Kirjoita(Ktiedosto, Palindromit=[]):
    Td = open(Ktiedosto, "w")
    #Kirjoitetaan listan kaikki palindromit, sekä merkkijonot, joista ne muodostuvat, tiedostoon.
    for i in range(0, len(Palindromit)):
        p = Palindromit[i]
        Td.write(f"{p[0]}\n----> {p[1]}\n")
    Td.close()
    return None

def paaOhjelma():
    LTiedosto = input("Anna luettavan tiedoston nimi: ")
    KTiedosto = input("Anna kirjoitettavan tiedoston nimi: ")
    Palindromit = Lue(LTiedosto)
    Kirjoita(KTiedosto, Palindromit)
    print("Kiitos ohjelman käytöstä.")
    
paaOhjelma()

