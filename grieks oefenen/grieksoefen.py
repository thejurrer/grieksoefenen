import random
import dict as d
import sys
sys.dont_write_bytecode = True

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
            score = 0
        

        
            

if __name__ == "__main__":
    print("welkom, bij grieksoefenen!\nKies welke je wil typ 'a' om Grieks naar Nederlands te oefenen.")
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
        elif tekstchoice == "alles":
            alles = d.griekseWoordentekst2 | d.griekseWoordentekst3 | d.griekseWoordentekst4 | d.griekseWoordentekst6 | d.griekseWoordentekst7 | d.griekseWoordentekst8 | d.griekseWoordentekst9
            grieksNederlands(alles)
        elif tekstchoice == "q":
            print("tot ziens!") 
        else:
            print("sorry, die tekst bestaat niet.")
            
    else:
        print("Sorry, dat begrijp ik niet.")


