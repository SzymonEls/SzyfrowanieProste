import time
#zmienne
txt = []
od_ascii = 32
do_ascii = 126


txt.append(input ("Wpisz tekst:"))#Jeśli plik usuń
klucz = int(input("Wpisz klucz:"))

#Plik
#tekst = open('ścieżka')
#txt = tekst.readlines()
#tekst.close()

licz = 0
while licz != len(txt):
    print(txt)
    #print(licz) - nie
    nt = ""
    licznik = 0
    inp = txt[licz]
    while licznik != len(inp):
        liczba = ord(inp[licznik]) - klucz
        if liczba < od_ascii:
            liczba = do_ascii - (od_ascii - liczba)
            liczba = liczba + 1
        nt = nt + chr(liczba)
        licznik = licznik + 1
    txt[licz] = nt
    licz += 1


#Plik
#tekst2 = open('ścieżka', 'w+')
#licznik2 = 0
#while licznik2 != len(txt):
#    tekst2.write(txt[licznik2])
#    licznik2 = licznik2 + 1
#tekst2.close()

print(txt)
time.sleep(15)
