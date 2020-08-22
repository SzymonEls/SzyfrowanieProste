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
    print(licz)
    nt = ""
    licznik = 0
    inp = txt[licz]
    if inp.count("\n") != 0:
        inp = inp[:inp.index("\n")]
        inp = inp + "   "
    while licznik != len(inp):
        liczba = ord(inp[licznik]) + klucz
        if liczba > do_ascii:
            liczba = (liczba - do_ascii) + od_ascii
            liczba = liczba - 1
        print("liczba{a}".format(a=liczba))
        nt = nt + chr(liczba)
        licznik = licznik + 1
    txt[licz] = nt
    licz += 1


#Plik
#tekst2 = open('C:/Users/SzymonPC/Documents/Do synch/projekth.txt', 'w+')
#licznik2 = 0
#while licznik2 != len(txt):
#    print(licznik2)
#    tekst2.write(txt[licznik2])
#    licznik2 = licznik2 + 1
#tekst2.close()

print(txt)
time.sleep(15)
