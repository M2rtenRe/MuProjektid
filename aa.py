#Kirjutab ridadega teksti
def writeFileLine(name, tekst, korrad):
    f = open(name+".txt", "w")
    for i in range(0,korrad):
        f.write(tekst + "\n")
    f.close()
#Kirjutab ridadeta teksti
def writeFile(name, tekst, korrad):
    f = open(name+".txt", "w")
    for i in range(0,korrad):
        f.write(tekst)
    f.close()
#Vaatab kas kasutaja tahab ridu või mitte
def lineChecker(a, name, tekst, korrad):
    if a == 0:
        writeFileLine(name, tekst, korrad)
    if a == 1:
        writeFile(name, tekst, korrad)
#Küsib kasutaja inputi
def askInput():
    try:
        fileName = input("Faili nimi: ")
        if len(fileName) <= 0:
            print("Sisesta faili nimi!")
            askInput()
        userIn = input("Tekst: ")
        if len(userIn) <= 0:
            print("Sisesta tekst!")
            askInput()
        times = int(input("Mitu korda? ")) #Mitu korda peaks kordama seda teksti
        if times <= 0:
            print("Sisesta number üle nulli!")
            askInput()
        lineCheck = input("Kas soovid ridu?[Y/N] ")
        if lineCheck == "Y" or lineCheck == "y":
            lineChecker(0, fileName, userIn, times)
        if lineCheck == "N" or lineCheck == "n":
            lineChecker(1, fileName, userIn, times)
    except:
        print("Sisesta number!")
        askInput()
        
        
askInput()
