import random

griekseWoordentekst2 = {
    "ἐστί(ν)": "(hij/zij/het/er) is, bestaat",
    "ὁ, ἡ, τό": "de, het",
    "γῆ": "land, aarde",
    "ὁ ποταμός": "rivier",
    "ἡ πέτρα": "rots, rotsblok",
    "τό δένδρον": "boom",
    "ὁ ἄνθρωπος": "mens",
    "ὁ θεός": "god",
    "ἡ μάχη": "strijd, gevecht",
    "τό ἔργον": "werk, taak, daad",
    "πρῶτον": "eerst",
    "ἡ θεά": "godin",
    }

griekseWoordentekst3 = {
    "ὁ βίος": "(het) leven",
    "ἀεί": "altijd, steeds",
    "ὁ ἥλιος": "zon",
    "νοέω": "waarnemen, opmerken",
    "μέν...δέ": "1 (weliswaar) ... maar 2 ... en",
    "τὸ πεδίον": "vlakte",
    "τὸ θηρίον": "(wild) dier",
    "φέρω": "dragen, brengen",
    "κατά, καθ' + acc": "(verspreid) over",
    "ὁ ἵππος": "paard",
    "ἀλλά, ἀλλ'": "maar",
    "δάμαζω": "temmen",
    "ἀγω": "leiden, brengen",
    "λέγω": "zeggen, spreken",
    "ὁ ἐπίτροπος": "opzichter, beheerder",
    "νῦν": "nu, op dit moment",
    "αὐτίκα": "meteen",
    "ὀνομάζω": "noemen"
}

griekseWoordentekst4 = {
    "τὸ τέκνον" : "kind",
    "τίκτω" : "ter wereld brengen, voortbrengen",
    "ἡ κόρη" : "meisje",
    "ὁ θρόνος" : "troon",
    "οὖν" : "dus, dan, nu",
    "οὕτω(ς)" : "zo, op deze manier",
    "τέλος" : "tenslotte",
    "ὁ δόλος" : "list, bedrog",
    "ὁ υἱός" : "zoon",
    "πρός" : "naar (toe), tot, tegen",
    "ὁ ἀδελφός" : "broer",
    "ἡ ἀδελφή" : "zus",
    "ἔχω" : "hebben, houden",
    "εἰς + acc" : "naar (binnen)"
}

griekseWoordentekst6 = {
    "ὁ ἡγεμών, ἡγεμόνος": "leider, aanvoerder",
    "ἡ γυνή, γυναικός": "vrouw",
    "τὸ ὄνομα, ὀνόματος": "naam",
    "ἔγγυς": "dichtbij",
    "ἡ πυρ, πυρος": "vuur",
    "μόνον": "alleen (maar)",
    "ἡ τέχνη": "kunst, vaardigheid",
    "τὰ ὅπλα": "wapens",
    "ὁ δορυ, δόρατος": "lans",
    "ἡ ἀσπίς, ἀσπίδος": "schild",
    "διὰ, δι": "1 door ... heen 2 gedurende",
    "ὁ Ἕλλην, Ἕλληνος": "Griek",
    "βλέπω": "kijken",
    "τὸ πρᾶγμα, πράγματος": "zaak, gebeurtenis",
    "μάλα, μᾶλ'": "zeer, erg",
    "ἐκ, ἐξ + gen": "uit",
    "ἡ μήτηρ, μητρός": "moeder",
    "ὁ πατήρ, πατρός": "vader",
    "ἡ κεφαλή": "hoofd",
    "ἡ ἐσθής, ἐσθῆτος": "kleding(stuk)",
    "ἤδη": "al, reeds (vanaf) nu",
    "ἡ θυγάτηρ, θυγατρός": "dochter"
}

griekseWoordentekst7 = {
    "ὁ ἥρως, ἥρωος": "held",
    "ἀντὶ, ἀντ', ἀνθ' + gen": "in ruil voor, in plaats van",
    "κτείνω": "doden",
    "ὁ φόβος": "angst",
    "φεύγω": "vluchten, ontvluchten",
    "ὁ χῶρος": "gebied, plaats",
    "ἡ ἀρετή": "dapperheid, voortreffelijkheid",
    "φαίνω": "laten zien, tonen",
    "εθελω": "willen",
    "βοηθέω + dat": "helpen",
    "ὁ ἀνήρ, ἀνδρός": "man",
    "ὁ παῖς, παιδός": "kind",
    "παρέχω": "geven, verschaffen",
    "ὡς": "(zo)als",
    "εἰ": "als, indien",
    "ἐν + dat": "in, op, bij",
    "χαίρω": "blij zijn",
    "τὸ δῶρον": "geschenk",
    "ὡς ταχιστα":"1 zo snel mogelijk 2 zodra",
    "ἡ βοήθεια": "hulp"
}

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
            tekst = griekseWoordentekst2
            grieksNederlands(tekst)
        elif tekstchoice == "3":
            tekst = griekseWoordentekst3
            grieksNederlands(tekst)
        elif tekstchoice == "4":
            tekst = griekseWoordentekst4
            grieksNederlands(tekst)
        elif tekstchoice == "6":
            tekst = griekseWoordentekst6
            grieksNederlands(tekst)
        elif tekstchoice == "7":
            tekst = griekseWoordentekst7
            grieksNederlands(tekst)
        else:
            print("sorry, die tekst bestaat niet.")
            
    else:
        print("Sorry, dat begrijp ik niet.")


