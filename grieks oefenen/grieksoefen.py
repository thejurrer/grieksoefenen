import random
import dict as d



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
        
        tekstchoice = input("Welke tekst wil je oefenen (antwoord met een cijfer): ")
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
        else:
            print("sorry, die tekst bestaat niet.")
            
    else:
        print("Sorry, dat begrijp ik niet.")


