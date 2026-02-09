import random
import dict as d
import sys
sys.dont_write_bytecode = True
mark = False

def grieksNederlands(tekst):
    score = 0
    while True:
        vraag = random.choice(list(tekst.keys()))
        antwoord = tekst[vraag]
        print(vraag)
        x = input("-> ")
        if x == antwoord:
            print("goed gedaan! (typ q om te stoppen)")
            score = score + 1
            print(f"je streak is nu: {score}.")
        elif x == "q":
            break
        else:
            print(f"sorry, dat is fout. Het goede antwoord is {antwoord} . (typ q om te stoppen)")
            print(f"je had een streak van: {score}.")
            if score >= 150:
                mark = True
                naam = input("Wat is je naam?")
                print("Added to highscore list:", score)
                highscores(score, naam)
                
                while mark:
                    print("mark ga weg")

            elif score >= 100:
                print("\nga iets nuttigs met je leven doen")
                naam = input("Wat is je naam?")
                print("Added to highscore list:", score)
                highscores(score, naam)

            elif score >= 40:
                print("\nJij hebt het helemaal beheerst, goed!")
                naam = input("Wat is je naam?")
                print("Added to highscore list:", score)
                highscores(score, naam)

            elif score >= 30:
                print("\ngoed, goed, nog heel eventjes en je bent er!")
                naam = input("Wat is je naam?")
                print("Added to highscore list:", score)
                highscores(score, naam)

            elif score >= 20:
                print("\nAhh, oké dit gaat de goede kant op!")
                naam = input("Wat is je naam?")
                print("Added to highscore list:", score)
                highscores(score, naam)
            elif score >= 10:
                print("\nmehhhh, je kan het beter doen!")
            
            score = 0


def seehighscores():
    with open("highscores.txt", "r") as f:
        print(f.read())

def addhighscore(score):
    naam = input("Wat is je naam:")
    print("Added to highscore list:", score)
    highscores(score, naam)

def highscores(score, naam):
    with open("highscores.txt", "a") as f:
        f.write(f"{score, naam}, " )
    
        
            

if __name__ == "__main__":
    print("welkom, bij grieksoefenen!\nKies welke je wil typ 'a' om Grieks te oefenen en 'b' om latijn te oefenen. Als je beide wilt oefenen kies 'c'.\nOm highscores te zien, typ 'd'.")
    x = input("-> ")
    if x == "a":
        print("Oké, veel succes!")
        
        tekstchoice = input("Welke tekst wil je oefenen (antwoord met een cijfer, typ alles om alles te krijgen): ")
        if tekstchoice == "2":
            tekst = d.griekseWoordentekst2
            grieksNederlands(tekst)
        elif tekstchoice == "3":
            tekst = d.griekseWoordentekst3
            grieksNederlands(tekst)
        elif tekstchoice == "4":
            tekst = d.griekseWoordentekst4
            grieksNederlands(tekst)
        elif tekstchoice == "6":
            tekst = d.griekseWoordentekst6
            grieksNederlands(tekst)
        elif tekstchoice == "7":
            tekst = d.griekseWoordentekst7
            grieksNederlands(tekst)
        elif tekstchoice == "8":
            tekst = d.griekseWoordentekst8
            grieksNederlands(tekst)
        elif tekstchoice == "9":
            tekst = d.griekseWoordentekst9
            grieksNederlands(tekst)
        elif tekstchoice == "11":
            tekst = d.griekseWoordentekst11
            grieksNederlands(tekst)
        elif tekstchoice == "12":
            tekst = d.griekseWoordentekst12
            grieksNederlands(tekst)
        elif tekstchoice == "13":
            tekst = d.griekseWoordentekst13
            grieksNederlands(tekst)
        elif tekstchoice == "14":
            tekst = d.griekseWoordentekst14
            grieksNederlands(tekst)
        elif tekstchoice == "alles":
            alles = d.griekseWoordentekst2 | d.griekseWoordentekst3 | d.griekseWoordentekst4 | d.griekseWoordentekst6 | d.griekseWoordentekst7 | d.griekseWoordentekst8 | d.griekseWoordentekst9 | d.griekseWoordentekst11 | d.griekseWoordentekst12 | d.griekseWoordentekst13 | d.griekseWoordentekst14
            grieksNederlands(alles)
        elif tekstchoice == "lidwoorden":
            tekst =d.lidwoorden
            grieksNederlands(tekst)
        elif tekstchoice == "persoonsvormen":
            tekst =d.persoonsVormen
            grieksNederlands(tekst)
        elif tekstchoice == "q":
            print("tot ziens!") 
        else:
            print("sorry, die tekst bestaat niet.") 
    
    elif x == 'b':
        print("Oké, succes!")

        tekstchoice = input("Welke tekst wil je oefenen (antwoord met een cijfer, typ alles om alles te krijgen): ")

        if tekstchoice == "1":
            tekst = d.latijnseWoordentekst1
            grieksNederlands(tekst)
        elif tekstchoice == "2":
            tekst = d.latijnseWoordentekst2
            grieksNederlands(tekst)
        elif tekstchoice == "3":
            tekst = d.latijnseWoordentekst3
            grieksNederlands(tekst)
        elif tekstchoice == "4":
            tekst = d.latijnseWoordentekst4
            grieksNederlands(tekst)
        elif tekstchoice == "5":
            tekst = d.latijnseWoordentekst5
            grieksNederlands(tekst)
        elif tekstchoice == "6":
            tekst = d.latijnseWoordentekst6
            grieksNederlands(tekst)
        elif tekstchoice == "8":
            tekst = d.latijnseWoordentekst8
            grieksNederlands(tekst)
        elif tekstchoice == "9":
            tekst = d.latijnseWoordentekst9
            grieksNederlands(tekst)
        elif tekstchoice == "alles":
            alles = d.latijnseWoordentekst1 | d.latijnseWoordentekst2 |d.latijnseWoordentekst3 | d.latijnseWoordentekst4 | d.latijnseWoordentekst5 | d.latijnseWoordentekst6
            grieksNederlands(alles)
        elif tekstchoice == "q":
            print("tot ziens!") 
        else:
            print("sorry, die tekst bestaat niet.") 
    
    elif x=='c':
        alles = d.griekseWoordentekst2 | d.griekseWoordentekst3 | d.griekseWoordentekst4 | d.griekseWoordentekst6 | d.griekseWoordentekst7 | d.griekseWoordentekst8 | d.griekseWoordentekst9 | d.griekseWoordentekst11 | d.griekseWoordentekst12 | d.griekseWoordentekst13 | d.griekseWoordentekst14 | d.latijnseWoordentekst1 | d.latijnseWoordentekst2 |d.latijnseWoordentekst3 | d.latijnseWoordentekst4 | d.latijnseWoordentekst5 | d.latijnseWoordentekst6
        grieksNederlands(alles)

    elif x == 'd':
        print("Oké")
        seehighscores()

    

    else:
        print("Sorry, dat begrijp ik niet.")


