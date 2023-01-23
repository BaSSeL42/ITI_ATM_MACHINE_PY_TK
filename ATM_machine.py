from time import sleep

def loading ():
	print("")
	print("LOADING")
	for i in range(1,30):
		print('.', end='',flush=True)
		sleep(.1) 
	print("")	


member = {
    "bassel"    : {"pin" : 1234},
    "mohamed"   : {"pin" : 5665},
    "sara"      : {"pin" : 1111}
}

dataBase = {
    member["bassel"]["pin"]  : {"salary" : 2500, "status" : "active", "name" : "bassel"},
    member["mohamed"]["pin"] : {"salary" : 4000, "status" : "active", "name" : "mohamed"},
    member["sara"]["pin"]    : {"salary" : 10000, "status" : "active", "name" : "sara"}
}

def changePin(value,Nam):
    global member
    member[Nam]["pin"] = value

myPin = 0
myName = "0"
count = 1 
while (count > 0):
    print ("(1) login   ")
    print ("(0) exit    ")
    count=sel=int(input("please enter your selection >> "))
    if (count == 0):
        loading ()
        print("________________THANK YOU :)__________________")
        break
    elif (sel == 1):
        yourName = input("username >> ")
        yourName = yourName.lower()
        yourName = yourName.strip()
        y = 3
        while (y>0):
            if yourName in member:
                myName = yourName
                yourPass = int(input("password >> "))
                if yourPass == member[yourName]["pin"]:
                    loading ()
                    print(f"____________welcome {yourName}________________")
                    myPin = member[yourName]["pin"]
                    count = 2
                    y = 0

                else:
                    print("Invalid password.....try again!")
                    y -= 1
            else:
                print("Invalid username......")
                y = 0

    while (count == 2):
        print("(0) Log out")
        print("(1) View Account balance" )
        print("(2) Withdraw Cash")
        print("(3) Deposit Cash")
        print("(4) Change Pin")
        sel = int(input("Your selection >> "))
        if sel == 0:
            count=5
        elif sel ==1:
            mypin = myPin
            
            print(member[myName]["pin"])
            print(" ")
            print("your balance is {} ".format( dataBase[mypin]["salary"]))
            print(" ")

        elif sel==2:
            mypin = myPin
            print("your balance is {} ".format( dataBase[myPin]["salary"]))
            moneyVal = int(input("Enter money amount >> "))
            if dataBase[mypin]["salary"] > moneyVal:
                print("to proceed please enter your pin number ")
                
                y = 3
                while (y>0):
                    
                    pinNum = int(input("pin number = "))
                    if pinNum == member[myName]["pin"]:
                        # loading ()
                        print("Account authorized!")
                        print(" ")
                        print(" process loading ")
                        # loading ()
                        dataBase[mypin]["salary"] -= moneyVal
                        print("your balance is {} ".format( dataBase[mypin]["salary"]))
                        print("_______________________________________________________________")
                        y = 0
                    else:
                        print("wrong pin number..... try again")
                        y -= 1
            else:
                print("sorry you don't have enough money")


        elif sel==3:
            mypin = member[myName]["pin"]
            print("your balance is {} ".format( dataBase[mypin]["salary"]))
            moneyVal = int(input("Enter money amount >> "))
            if dataBase[mypin]["salary"] > moneyVal:
                print("to proceed please enter your pin number ")
                
                y = 3
                while (y>0):
                    pinNum = int(input("pin number = "))
                    if pinNum == member[myName]["pin"]:
                        # loading ()
                        print("Account authorized!")
                        print(" ")
                        print(" process loading ")
                        # loading ()
                        dataBase[mypin]["salary"] += moneyVal
                        print("your balance is {} ".format( dataBase[mypin]["salary"]))
                        print("_______________________________________________________________")
                        y = 0
                    else:
                        print("wrong pin number..... try again")
                        y -= 1
            else:
                print("sorry you don't have enough money")     

        elif sel==4:
            mypin = member[myName]["pin"]
            n = myName
            
            print("please enter old pin") 
            y = 3
            while (y > 0 ):
                pinNum = int(input("old pin >> "))
                if pinNum == member[myName]["pin"]:
                    # loading()
                    print("enter your new pin number >> ")
                    newPin = int(input("new pin >> "))
                    changePin(newPin,myName)
                    # print(member[myName]["pin"])
                    # member[myName]["pin"] = newPin
                    # myPin = member[yourName]["pin"]
                    # print(member[n][myName])
                    y = 0
                else:
                    print("invalid pin .... try again")
                    y -= 1     



