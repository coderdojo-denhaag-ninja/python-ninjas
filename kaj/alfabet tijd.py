import datetime
a = True
input("typ enter to start")
now = datetime.datetime.now()


while a == True:
    alfabet = input("""typ the alfabet as fast as you can
""")
    if alfabet == "abcdefghijklmnopqrstuvwxyz":
        print(datetime.datetime.now()-now)
        a = False
    else:
        print("that is not the alfabet!")
        


