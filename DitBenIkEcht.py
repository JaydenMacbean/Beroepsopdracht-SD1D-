def Question3():
    print("Hoe was mijn eerste week hier?")
    print("A. Goed")
    print("B. Slecht")
    print("C. Geweldig")
    inputAntwoordAVraag3 = "A"
    inputAntwoordBVraag3 = "B"
    inputAntwoordCVraag3 = "C"
    inputVraag3 = input("Typ in A B of C: ")
    if(inputVraag3 == inputAntwoordAVraag3):
        print("Helemaal goed!")
    if(inputVraag3 == inputAntwoordBVraag3):
        print("Haha fout you suck :P")
    if(inputVraag3 == inputAntwoordCVraag3):
        print("Haha fout you suck :P")
def Question2():
    print("Welke directie ga ik op?")
    print("A. Game Development")
    print("B. Media Development")
    print("C. Weet ik nog niet")
    inputAntwoordAVraag2 = "A"
    inputAntwoordBVraag2 = "B"
    inputAntwoordCVraag2 = "C"
    inputVraag2 = input("Typ in A B of C: ")
    if(inputVraag2 == inputAntwoordAVraag2):
        print("<INSERT FF VICTORY THEME HERE> Correct!")
        Question3()
    if(inputVraag2 == inputAntwoordBVraag2):
        print("Ew Media Development, natuurlijk niet xDxDxD")
        Question3()
    if(inputVraag2 == inputAntwoordCVraag2):
        print("Pfft, waarom zou ik NIET Game Development kiezen smh")
        Question3()
def Question1():
    naamJayden = "Jayden"
    print("Hello You!, ik ben " + naamJayden + ".")
    print("Wat is jouw naam?")
    naam = input("Naam is: ")
    print("Sup " + naam)
    print("Ben ik een nieuwkomer?")
    print("A. Ja")
    print("B. Helll no")
    print("C. Soort van?")
    inputAntwoordAVraag1 = "A"
    inputAntwoordBVraag1 = "B"
    inputAntwoordCVraag1 = "C"
    inputVraag1 = input("Typ in A B of C: ")
    if(inputVraag1 == inputAntwoordAVraag1):
        print("Well no, but actually yes.")
        Question2()
    if(inputVraag1 == inputAntwoordBVraag1):
        print("Well yes, but actually no.")
        Question2()
    if(inputVraag1 == inputAntwoordCVraag1):
        print("Correct!")
        Question2()

Question1()
        