import math

print("Welkom bij de ultieme rekenmachine!")

getal2 = 0

print("""
Druk op "c" bi het invoeren van een bewerking om de rekenmachine te resetten.
""")
    
getal1 = float(input("Wat is je getal? : "))

while True:
        bewerking = input("""
Wat is je bewerking, optellen, aftrekken, vermenigvuldigen, delen, kwadrateren of worteltrekken? : """)
        if (bewerking[0] == "c"):
            print()
            print("clearing...")
            print()
            getal1 = float(input("Wat is je getal? : "))
        else:

            if (bewerking[0] not in ["w","k"]):
                print()
                getal2 = float(input("wat is je volgende getal? : "))
                print()

            if (bewerking[0] == "o"):
                    getal1 = getal1 + getal2
                    print(getal1)

            elif (bewerking[0] == "a"):
                    getal1 = getal1 - getal2
                    print(getal1)

            elif (bewerking[0] == "v"):
                    getal1 = getal1 * getal2
                    print(getal1)

            elif (bewerking[0] == "d"):
                

                if (getal2 == 0):
                        print("syntax error")
                        print()
                        print("clearing...")
                        print()
                        getal1 = float(input("Wat is je getal? : "))

                else:
                        getal1 = getal1 / getal2
                        print(getal1)

            elif (bewerking[0] == "w"):
                    getal1 = math.sqrt(getal1)
                    print(getal1)

            elif (bewerking[0] == "k"):
                    getal1 = getal1 * getal1
                    print(getal1)
