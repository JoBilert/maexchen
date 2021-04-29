from random import *

class Player:
    def __init__(self,name):
        self.points = 0
        self.name = name
        self.ergebnis = 0

    def winner(self):
        self.points += 1
    
    def wurf(self, wuerfelA, wuerfelB):
        if wuerfelA > wuerfelB:
            self.ergebnis = int(str(wuerfelA) + str(wuerfelB))
        else:
            self.ergebnis = int(str(wuerfelB) + str(wuerfelA))

    def wuerfeln(self):
        self.wurf(randint(1,6), randint(1,6))

def checkWinner(s1, s2):
    pasch = [11,22,33,44,55,66]
    max = 21
    if s1 == s2:
        print("Gleichstand - es werden keine Punkte vergeben!")
    elif s1 == max and s2 != max:
        spielerA.winner()
        print(spielerA.name + " hat gewonnen! Er erhaelt einen Punkt.")
        spielstand()
    elif s1 != max and s2 == max:
        spielerB.winner()
        print(spielerB.name + " hat gewonnen! Er erhaelt einen Punkt.")
        spielstand()
    elif s1 in pasch and s2 in pasch:
        if s1 > s2:
            spielerA.winner()
            print(spielerA.name + " hat gewonnen! Er erhaelt einen Punkt.")
            spielstand()
        elif s1 < s2:
            spielerB.winner()
            print(spielerB.name + " hat gewonnen! Er erhaelt einen Punkt.")
            spielstand()
    elif s1 in pasch and s2 not in pasch:
        spielerA.winner()
        print(spielerA.name + " hat gewonnen! Er erhaelt einen Punkt.")
        spielstand()
    elif s1 not in pasch and s2 in pasch:
        spielerB.winner()
        print(spielerB.name + " hat gewonnen! Er erhaelt einen Punkt.")
        spielstand()
    else:
        if s1 > s2:
            spielerA.winner()
            print(spielerA.name + " hat gewonnen! Er erhaelt einen Punkt.")
            spielstand()
        else:
            spielerB.winner()
            print(spielerB.name + " hat gewonnen! Er erhaelt einen Punkt.")
            spielstand()
    
def spielstand():
            print("************")
            print("Punktestand:")
            print("------------")
            print(spielerA.name + " -- " + str(spielerA.points) + " : " + str(spielerB.points) + " -- " + spielerB.name)

spielerA = Player(input("SpielerIn 1 - Bitte gib deinen Namen ein: "))
spielerB = Player(input("SpielerIn 2 - Bitte gib deinen Namen ein: "))
ende = False

while ende == False:
    spielerA.wuerfeln()
    print(spielerA.name + " hat " + str(spielerA.ergebnis) + " geworfen!")
    spielerB.wuerfeln()
    print(spielerB.name + " hat " + str(spielerB.ergebnis) + " geworfen!")
    checkWinner(spielerA.ergebnis, spielerB.ergebnis)
    if input("Wollt ihr nochmal spielen? (J/n)")=="n" :
        ende = True

print("Das Spiel wurde beendet:")
print("------------------------")
spielstand()