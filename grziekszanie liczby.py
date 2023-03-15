print("Podaj przykładowe zdanie: ")
x=input()
dlugosc=len(x)
if dlugosc<=3:
    print("Ale krótkie zdanie! Zamienimy je na duże litery!")
    duze=x.upper()
    print(duze)
    yyy=input()
elif dlugosc > 3 and dlugosc <= 6:
    print("To zdanie ma już trochę liter, napiszmy je małymi literami")
    male=x.lower()
    print(male)
    yyy=input()
elif dlugosc > 6 and dlugosc <=9:
    print("To już jest pradziwe zdanie! Odwróćmy wielkość liter!")
    zmiana=x.swapcase()
    print(zmiana)
    yyy=input()
elif dlugosc > 9:
    print("Ale olbrzym! Wszystko będzie małe! Który znaki chcesz zamienić na duże?")
    ciag=x.lower()
    print(ciag)
    numer=int(input())
    numer1=numer-1
    bang=ciag[numer1:numer]
    print("Na duży zostanie zmieniony",numer,"znak :)")
    print(ciag[0:numer1]+bang.upper()+ciag[numer:dlugosc])
    yyy=input()
else:
    print("BŁĄD")
    yyy=input()
    