# Zad1
# list = [0+x for x in range(1, 31)]
# listx2 = [str(x*2) for x in list]
# plik = open("x2.txt", "w")
# plik.writelines(listx2)
#
# # Zad2
# plik = open("x2.txt", "r")
# odczyt = plik.readlines()
# print(odczyt)
#
# # Zad3
# with open("tekst.txt", "w") as plik:
#     for newLine in range(10) :
#         plik.write("tekst\n")
# with open("tekst.txt", "r") as plik:
#     for line in plik:
#         print(line, end="")

# Zad4
# class NaZakupy:
#     nazwa_produktu = ""
#     ilosc = 0
#     jednostka_miary = ""
#     cena_jed = 0
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#     def wyswietl_Produkt(self):
#         print(self.ilosc, self.nazwa_produktu, self.jednostka_miary, self.cena_jed)
#     def ile_produktu(self):
#         print(str(self.ilosc) +""+self.jednostka_miary)
#     def ile_kosztuje(self):
#         kwota = self.cena_jed*self.ilosc
#         return kwota
#
# produkt = NaZakupy("Jabłka", 2, "Kg", 0.45)
# produkt.wyswietl_Produkt()
# produkt.ile_produktu()
# print(produkt.ile_kosztuje())