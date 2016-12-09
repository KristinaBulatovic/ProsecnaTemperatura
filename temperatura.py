import txt

def main():
    txt.txtFile()

    while True:
        try:
            mesec = input("Izaberite mesec: ").lower()
            folder = open(mesec + ".txt", "r")
        except:
            print("Unesite mesec!")
        else:
            break

    temp = []
    for i in folder:
        temp.append(int(i.strip()))
    folder.close()
    s = 0
    for j in temp:
        s += j

    if mesec == "april" or mesec == "jun" or mesec == "septembar" or mesec == "novembar":
        print("Prosecna temperatura u %s mesecu je: "%mesec, s/30)
    elif mesec == "februar":
        print("Prosecna temperatura u %s mesecu je: "%mesec, s/28)
    else:
        print("Prosecna temperatura u %s mesecu je: "%mesec, s/31)

close = None
while close != "0":
    main()
    close = input("U slucaju da zelite da napustite program pritisnite 0, a u suprotnom pritisnite bilo koji karakter: ")
