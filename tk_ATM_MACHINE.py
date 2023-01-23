from tkinter import *
import os

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
    # global newPinNum 
    # newPinNum = member[Nam]["pin"] 

def change_dict_key(d, old_key, new_key, default_value=None):
    d[new_key] = d.pop(old_key, default_value)


newPinNum= 0


def w_1():
    window_1 = Tk()
    window_1.title("ATM MACHINE")
    # window_1.geometry('600x600')


    string_var  = StringVar()
    pass_var    = StringVar()
    

    # newPinNum = 0

    def submit(): 

        myUserName = string_var.get()
        myPinNumber = pass_var.get()
        myUserName = myUserName.lower()
        myUserName = myUserName.strip()
        y = 3
        c = 3
        while (y>0):
            if myUserName in member:
                naMe = myUserName
                if int(myPinNumber) == member[myUserName]["pin"]:
                    newPinNum = member[myUserName]["pin"]
                    c = 2
                    y = 0
                else:
                    label22 = Label(window_1,text = "         Wrong password                ", bg = "red", fg = "black").grid(row=8,column=0)
                    # c -= 1
                    y -= 1
            else:
                label21 = Label(window_1,text = "         Wrong username                ", bg = "red", fg = "black").grid(row=8,column=0)
                y = 0
        #         c = 0

        # if c == 0:
        #     label28 = Label(window_1,text = "         system terminated                ", bg = "red", fg = "black").place(x = 300, y = 410)

        if (c == 2):
            window_1.destroy()
            window_2 = Tk()
            window_2.title("ATM")
            window_2.geometry('600x600')

            F_2 = Frame(master=window_2, relief=SUNKEN, bg='red4', width=175, height=200).place(x = 300, y = 200)
            L_30 = Label(F_2, text = "Balance", font = ("Times New Roman", 20), bg='red4').place(x = 330, y = 240)

            def viewBalance():
                # nn = newPinNum
                nn = int(member[naMe]["pin"])
                # upin = newPinNum
                # print(dataBase[nn]["salary"] ,"\n")
                # print(nn,"\n")
                mysal = dataBase[nn]["salary"] 
                label_30 = Label(F_2, text = (f"         {mysal}          "), font = ("Times New Roman", 15),  bg='red4').place(x = 310, y = 320)
            
            

            
            def withDraw():
                window_3 = Toplevel()
                window_3.title("withdraw")
                # window_2.geometry('600x600')
                moneyAmount  = StringVar()
                def ok():
                    amount = moneyAmount.get()
                    amount = int(amount)
                    mypin = member[naMe]["pin"]
                    if amount <= dataBase[mypin]["salary"]:
                        dataBase[mypin]["salary"] -= amount 
                        mysal = dataBase[mypin]["salary"] 
                        L_5 = Label(F_2, text = (f"         {mysal}          "), font = ("Times New Roman", 15),  bg='red4').place(x = 310, y = 320)
                    else:
                        L_5 = Label(F_2, text = (f"  balance is low"), font = ("Times New Roman", 15),  bg='red4').place(x = 310, y = 320)
                    moneyAmount.set("")

                
                L_1 = Label(window_3, text = "money amount",fg= "black" ,font = ("Times New Roman", 10, 'bold')).grid(row=1,column=0)
                E_1 = Entry(window_3,textvariable=  moneyAmount,bg = "black", fg= "white" ,font = ("Times New Roman", 10, 'bold')).grid(row=1,column=1)
                B_6 = Button(window_3, text= "  OK   ", bd = '5', command=lambda:[window_3.destroy(), ok()]).grid(row=2,column=2)
                window_3.mainloop()

            def deposit():
                window_3 = Toplevel()
                window_3.title("Deposit")
                # window_2.geometry('600x600')
                moneyAmount  = StringVar()
                def ok():
                    amount = moneyAmount.get()
                    # amount = int(amount)
                    mypin = member[naMe]["pin"]
                    dataBase[mypin]["salary"] += int(amount); 
                    mysal = dataBase[mypin]["salary"] 
                    L_5 = Label(F_2, text = (f"         {mysal}          "), font = ("Times New Roman", 15),  bg='red4').place(x = 310, y = 320)
                    moneyAmount.set("") 

                
                L_1 = Label(window_3, text = "money amount",fg= "black" ,font = ("Times New Roman", 10, 'bold')).grid(row=1,column=0)
                E_1 = Entry(window_3,textvariable=  moneyAmount,bg = "black", fg= "white" ,font = ("Times New Roman", 10, 'bold')).grid(row=1,column=1)
                B_6 = Button(window_3, text= "  OK   ", bd = '5', command=lambda:[window_3.destroy(), ok()]).grid(row=2,column=2)
                window_3.mainloop()

            def pinChange():
                window_4 = Toplevel()
                window_4.title("Deposit")
                # window_2.geometry('600x600')
                newPin  = StringVar()
                def okk():
                    Npin = newPin.get()
                    Npin = int(Npin)
                    old_key1= member[naMe]["pin"]
                    new_key1 = Npin
                    change_dict_key(dataBase, old_key1, new_key1)
                    changePin(Npin,naMe)
                    # newPinNum = member[naMe]["pin"]
                    # print(newPinNum,"\n")
                    # member[naMe]["pin"] = Npin
                    
                    newPin.set("") 
                    # window_4.destroy()

                
                L_3 = Label(window_4, text = "new pin",fg= "black" ,font = ("Times New Roman", 10, 'bold')).grid(row=1,column=0)
                E_3 = Entry(window_4,textvariable=  newPin,bg = "black", fg= "white" ,font = ("Times New Roman", 10, 'bold')).grid(row=1,column=1)
                B_10 = Button(window_4, text= "  OK   ", bd = '5', command=lambda:[okk(),window_4.destroy(),window_2.destroy(),w_1()]).grid(row=2,column=2)
                window_4.mainloop()          

            F_1 = Frame(master=window_2, relief=RIDGE, borderwidth='5', width=200, height=350, bg='red4').place(x = 40, y = 150)
            label_21 = Label(window_2, text = (f"Welcome {naMe.capitalize()}"), font = ("Times New Roman", 50), fg = "grey26" ).pack(side=TOP)
            B_1 = Button(window_2, text = "____View account balance____", bd = '5', command = viewBalance).place(x = 50, y = 250)
            B_2 = Button(window_2, text = "________Withdraw cash________", bd = '5', command=withDraw).place(x = 50, y = 300)
            B_3 = Button(window_2, text = "_________Deposit cash_________", bd = '5', command=deposit).place(x = 50, y = 350)
            B_4 = Button(window_2, text = "_____Change pin number_____", bd = '5', command=pinChange).place(x = 50, y = 400)
            B_5 = Button(window_2, text = "   logout  ", bd = '5', fg= "red", command=lambda:[window_2.destroy(),w_1() ]).pack(side= BOTTOM)
            # B_1 = Button(window_2, text = "   Back  ", bd = '5').place(x = 250, y = 250)
            window_2.mainloop()
        

        string_var.set("")
        pass_var.set("")



    label_user 	= Label(window_1, text = "Username",fg= "black" ,font = ("Times New Roman", 10, 'bold')).grid(row=4,column=0,padx=1, pady=1)
    entry_1 	= Entry(window_1, textvariable = string_var ,bg = "black", fg= "white" , font = ("Times New Roman", 10, 'bold')).grid(row=4,column=1)
    label_pass 	= Label(window_1, text = "Pin",fg= "black", font = ("Times New Roman", 10, 'bold') ).grid(row=5,column=0)
    entry_2 	= Entry(window_1, textvariable = pass_var ,bg = "black", fg= "white" , font = ("Times New Roman", 10, 'bold'), show = '*').grid(row=5,column=1)
    sub_but 	= Button(window_1, text = "log in", bd = '3', command = submit).grid(row=6,column=1,padx=5, pady=5)
    label_33    = Label(window_1, text = "      A    T    M       ",fg = "black", font = ("Times New Roman", 25) ).grid(row=2,column=1,padx=5, pady=5)
    button_1 = Button(window_1, text = "Close", bd = '5',bg = "burlywood4", command = window_1.destroy ).grid(row=0,column=0,padx=5, pady=5)


    window_1.mainloop()




w_1()