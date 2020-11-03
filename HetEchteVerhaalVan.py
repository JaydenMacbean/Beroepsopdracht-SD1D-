import sys

def Antwoorden():
    AntwoordA = "A"
    AntwoordB = "B"
    AntwoordC = "C"
    inputVraag = input("TYP IN A, B OF C: ")
    if(inputVraag == AntwoordA):
        Stuk2A()
    if(inputVraag == AntwoordB):
        Stuk2A()
    if(inputVraag == AntwoordC):
        Stuk2A()

def Stuk2A():
    print("In je dromen hoor je gegil, geschreeuw en het geluid van afvurende wapens... Waarom weet je niet precies.")
    print("In de achtergrond verschijnt er een man, de details van het figuur's gezicht zijn moeilijk te verwerken.")
    Stuk3()

def Stuk3():
    print("Uit angst ren je weg.")
    print("In de achtergrond hoor je geluiden... ren weg... ga hier vandaan.")
    print("...En zo eindigt de droom.")
    print("Je schrikt wakker, de mensen om je heen kijken naar je en vragen of je oké bent.")
    print("Wat doe je?")
    print("A. Vertel ze over de droom.")
    print("B. Zeg dat het wel gaat.")
    print("C. Vraag wat er gebeurt.")
    AntwoordA3 = "A"
    AntwoordB3 = "B"
    AntwoordC3 = "C"
    inputVraag3 = input("TYP IN A, B OF C: ")
    if(inputVraag3 == AntwoordA3):
        Stuk4A()
    if(inputVraag3 == AntwoordB3):
        Stuk4B()
    if(inputVraag3 == AntwoordC3):
        Stuk4C()

def Stuk4A():
    print("Iedereen kijkt je raar aan en begint een beetje te giegelen.")
    print("Er komt een jongen naast je zitten. Hij introduceert zichzelf als Yousra.")
    print("Yousra: H-Hallo, is het goed als ik hier blijf zitten?")
    print("A. Ja")
    print("B. Nee")
    print("C. Waarom?")
    AntwoordA4 = "A"
    AntwoordB4 = "B"
    AntwoordC4 = "C"
    inputVraag4 = input("TYP IN A, B OF C: ")
    if(inputVraag4 == AntwoordA4):
        YousraStuk5A()

def Stuk4B():
    print("Er komt een jongen naast je zitten. Hij introduceert zichzelf als Yousra.")
    print("Yousra: H-Hallo, is het goed als ik hier blijf zitten?")
    print("A. Ja")
    print("B. Nee")
    print("C. Waarom?")
    AntwoordA4 = "A"
    AntwoordB4 = "B"
    AntwoordC4 = "C"
    inputVraag4 = input("TYP IN A, B OF C: ")
    if(inputVraag4 == AntwoordA4):
        YousraStuk5A()

def YousraStuk5A():
    print("Yousra: Echt?! OH DANK J-")
    print("Yousra realiseerde zich niet dat hij zo luid sprak. De oudere mensen rond jullie heen moestten zachtjes lachen.")
    print("Yousra: Uhhhh... sorry daarvoor. Het is gewoon dat jij de enige van mijn leeftijd bent die hier is.")
    print("Een deel van je wil meer weten over het verhaal van Yousra.")
    print("A. Hoe ben jij hier gekomen?")
    print("B. Zwijg.")
    print("C. Waar is de rest van jouw familie?")
    AntwoordA5 = "A"
    AntwoordB5 = "B"
    AntwoordC5 = "C"
    inputVraag5 = input("TYP IN A, B OF C: ")
    if(inputVraag5 == AntwoordA5):
        print("Ikke? ")
    if(inputVraag5 == AntwoordB5):
        print("Nothing happens the end lol")
        sys.exit()
    if(inputVraag5 == AntwoordC5):
        print("Yousra: ...Ik heb geen idee. De anderen hier hebben mij snel meegenomen in het busje zodat ik veilig bleef.")
        print("Ik weet niet hoe het gaat met mijn 2 broertjes, mijn moeder of mijn zus...")
        print("Maar genoeg over mij. Wat is er gebeurd met jou?")
        print("Jij vertelt tegen Yousra over het feit dat je weinig herinnerd over wat er is gebeurd.")
        print("Yousre: Oh... het spijt me heel erg voor je...")
        print("Hey! Aangezien wij de enige kinderen hier zijn.. z-zou je misschien vrienden willen worden?")
        print("Je hoofd knikt ja.")
        print("Yousra: Echt? Tof! Samen komen wij wel hier doorheen!")
        print("_____________________________________________________________________")
        print("THANK YOU FOR PLAYING!")
        sys.exit()
        

        

def Stuk4C(): 
    print("Er komt een grote man naast je zitten. Hij introduceert zichzelf als Amir.")
    print("Amir: We zitten nu in een busje en zijn op de vlucht. We zijn een ver eind van thuis... en we komen waarschijnlijk ook niet terug.")
    print("Amir: Is er nog iets wat je herrinert voordat je hier terecht kwam?")
    print("Je probeert te herinneren wat er is gebeurd voor deze situatie.")
    print(".....Maar er komt niks in je op.")

    print("Amir: Niks? Dat is jammer. Ieder van ons heeft veel veloren door weg te vluchten.")
    print("Een deel van je wil hier meer over weten hierover.")
    print("Wat doe je?")
    print("A. Niks zeggen.")
    print("B. Vragen over Amir's verhaal.")
    print("C. Vragen over de situatie.")
    AntwoordA4 = "A"
    AntwoordB4 = "B"
    AntwoordC4 = "C"
    inputVraag4 = input("TYP IN A, B OF C: ")
    if(inputVraag4 == AntwoordA4):
        AmirStuk5A()
    if(inputVraag4 == AntwoordB4):
        AmirStuk5B()
    if(inputVraag4 == AntwoordC4):
        AmirStuk5C()

def AmirStuk5A():
    print("Je zwijgt.")
    print("...")
    print("En toen gebeurde er niks meer haha gottem thx for playing ma game lol.")
    sys.exit()

def AmirStuk5B():
    print("Amir: Mijn verhaal? Vooruit dan.")
    print("Ik ben een vader van 3. Één tweeling van 4 en een meisje van 7.")
    print("Ik was aan het werk totdat ik het geluid van wapens hoorde.")
    print("Ik heb moeten vluchten uit het dorp waarin ik werkte en ben meteen naar mijn familie toegereden.")
    print("Maar toen ik nog maar een paar straten weg was, zag ik mijn buurman aan komen sprinten.")
    print("Hij gaf aan mij het bericht dat mijn familie veilig is weggekomen en zijn samen met zijn familie gevlucht.")
    print("Hun ideale eindbestemming is Nederland, maar of dat lukt of niet moeten we zelf achter zien te komen.Communiceren met hun wordt zeer moeilijk...")
    print("...Nou, we hebben niet echt meer de kans om terug te gaan nu tenzij je opgepakt wil worden. Wat zeg je ervan, ga je met ons mee?")
    print("A. Ga met Amir en co mee.")
    print("B. Reis zelf.")
    print("C. Ga terug op zoek naar je familie.")
    AntwoordA5 = "A"
    AntwoordB5 = "B"
    AntwoordC5 = "C"
    inputVraag5 = input("TYP IN A, B OF C: ")
    if(inputVraag5 == AntwoordA5):
        print("Amir: We hebben een lange lange tocht voor ons liggen.")
        print("Wat is je naam?")
        PlayerName = input("TYP JE NAAM HIER: ")
        print("Amir: Oké " + PlayerName + ", welkom bij de groep!")
        print("_____________________________________________________________________")
        print("THANK YOU FOR PLAYING!")
        sys.exit()
    if(inputVraag5 == AntwoordB5):
        print("Amir: Toch maar zelf ervandoor? Jammer om te horen... Toch succes met je reis.")
        print("Amir zwaait je af met vele waarschuwingen om veilig te blijven.")
        print("En zo vertrek je de wijde wereld in...")
        print("_____________________________________________________________________")
        print("THANK YOU FOR PLAYING!")
        sys.exit()
    if(inputVraag5 == AntwoordC5):
        print("Amir: ...Ik weet dat je graag terug wilt naar je familie. Maar het is nu te gevaarlijk om teru-.")
        print("Amir kijkt en ziet het verdriet in jouw ogen.")
        print("Amir: ...Goed dan, maar alsjeblieft als er iets gebeurt, ren.")
        print("Amir zwaait je af met vele waarschuwingen om veilig te blijven.")
        print("En zo vertrek je de wijde wereld in...")
        print("12 dagen later kwam was er slecht nieuws in de krant, Tiener genaamd Sava dood neer gevonden...")
        print("_____________________________________________________________________")
        print("THANK YOU FOR PLAYING!")
        sys.exit()

def AmirStuk5C():
    print("Amir: Er worden meerdere aanslagen gepleegt door een onbekende groep. Meerdere mensen hebben moeten vluchten van hun thuis, zonder idee waar ze terecht komen.")
    print("Wij zijn nu op zoek naar een veilige plek om ons leven weer te herbouwen. De ideale plek voor ons is Nederland.")
    print("Wat zeg je ervan? Ga je met ons mee?")
    print("A. Ga met Amir en co mee.")
    print("B. Reis zelf.")
    print("C. Ga terug op zoek naar je familie.")
    AntwoordA5 = "A"
    AntwoordB5 = "B"
    AntwoordC5 = "C"
    inputVraag5 = input("TYP IN A, B OF C: ")
    if(inputVraag5 == AntwoordA5):
        print("Amir: We hebben een lange lange tocht voor ons liggen.")
        print("Wat is je naam?")
        PlayerName = input("TYP JE NAAM HIER: ")
        print("Amir: Oké " + PlayerName + ", welkom bij de groep!")
        print("_____________________________________________________________________")
        print("THANK YOU FOR PLAYING!")
        sys.exit()
    if(inputVraag5 == AntwoordB5):
        print("Amir: Toch maar zelf ervandoor? Jammer om te horen... Toch succes met je reis.")
        print("Amir zwaait je af met vele waarschuwingen om veilig te blijven.")
        print("En zo vertrek je de wijde wereld in...")
        print("_____________________________________________________________________")
        print("THANK YOU FOR PLAYING!")
        sys.exit()
    if(inputVraag5 == AntwoordC5):
        print("Amir: ...Ik weet dat je graag terug wilt naar je familie. Maar het is nu te gevaarlijk om teru-.")
        print("Amir kijkt en ziet het verdriet in jouw ogen.")
        print("Amir: ...Goed dan, maar alsjeblieft als er iets gebeurt, ren.")
        print("Amir zwaait je af met vele waarschuwingen om veilig te blijven.")
        print("En zo vertrek je de wijde wereld in...")
        print("12 dagen later kwam was er slecht nieuws in de krant, Tiener genaamd Sava dood neer gevonden...")
        print("_____________________________________________________________________")
        print("THANK YOU FOR PLAYING!")
        sys.exit()

print("Je wordt wakker in een truck. Het is krap, je zit opgescheept met drie andere mensen... zonder enig idee waar je bent.")
print("Jouw opties zijn: ")
print("A. Door blijven slapen")
print("B. Vragen aan je mede mensen wat er gebeurt")
print("C. Kijk naar buiten")
Antwoorden()
    