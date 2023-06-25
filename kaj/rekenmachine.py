import math

print("Welkom bij de ultieme rekenmachine!")
while True:

    bewerking = input("""
Wat is je bewerking, optellen, aftrekken, vermenigvuldigen, delen, kwadrateren of worteltrekken?
""")
    if (bewerking[0] == "o"):
        getal1 = float(input("Wat is het eerste getal? : "))
        getal2 = float(input("Wat is het tweede getal? : "))
        print(getal1 + getal2)

    elif (bewerking[0] == "a"):
        getal1 = float(input("Wat is het eerste getal? : "))
        getal2 = float(input("Wat is het tweede getal? : "))
        print(getal1 - getal2)

    elif (bewerking[0] == "v"):
        getal1 = float(input("Wat is het eerste getal? : "))
        getal2 = float(input("Wat is het tweede getal? : "))
        print(getal1 * getal2)

    elif (bewerking[0] == "d"):
        getal1 = float(input("Wat is het eerste getal? : "))
        getal2 = float(input("Wat is het tweede getal? : "))
        if (getal2 == 0):
            print("syntax error")
        else:
            print(getal1 / getal2)

    elif (bewerking[0] == "w"):
        getal1 = float(input("Wat is het getal? : "))
        print(math.sqrt(getal1))

    elif (bewerking[0] == "k"):
        getal1 = float(input("Wat is het getal? : "))
        print(getal1 * getal1)
