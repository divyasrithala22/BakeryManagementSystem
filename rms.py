import random 
import tkinter.messagebox
from tkinter import*
import datetime
from datetime import time
from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("1350x750+0+0")
root.title("Lavender Bakery Management System")
root.configure (background = 'Gray')

Tops = Frame(root, bg='Gray', bd=20, pady =5, relief=RIDGE)
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=('arial', 60, 'bold'), text="Lavender Bakery Management System",bd=21,bg='Gray',fg='cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)

BillCal_F=Frame(root, bg='LightGray', bd=10, relief=RIDGE)
BillCal_F.pack(side=RIGHT)
Buttons_F=Frame(BillCal_F, bg='LightGray', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F=Frame(BillCal_F, bg='LightGray', bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Bill_F=Frame(BillCal_F, bg='LightGray', bd=4, relief=RIDGE)
Bill_F.pack(side=BOTTOM)

MenuFrame=Frame(root, bg='Gray', bd=10)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='LightGray',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='Gray',bd=10)
Drinks_F.pack(side=TOP)

Drinks_F=Frame(MenuFrame, bg='LightGray',bd=10,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F=Frame(MenuFrame, bg='LightGray',bd=10,relief=RIDGE)
Cake_F.pack(side=RIGHT)

# variables
var1=IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
var8= IntVar()
var9= IntVar()
var10= IntVar()
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()

DateofOrder = StringVar()
Bill_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_input = StringVar()
operator = ""

E_Maaza= StringVar()
E_Pepsi = StringVar()
E_Coke = StringVar()
E_Mirinda= StringVar()
E_Sprite= StringVar()
E_Milkshake = StringVar()
E_Chocolateshake= StringVar()
E_Orangejuice=StringVar()

E_Strawberrycake= StringVar()
E_chocolatecake= StringVar()
E_cupcake= StringVar()
E_MixedBerryCoffeeCake= StringVar()
E_Pineapplecake= StringVar()
E_BlackForestcake= StringVar()
E_plumcake= StringVar()
E_gemscake= StringVar()

E_Maaza.set("0")
E_Pepsi.set("0")
E_Coke.set("0")
E_Mirinda.set("0")
E_Sprite.set("0")
E_Milkshake.set("0")
E_Chocolateshake.set("0")
E_Orangejuice.set("0")

E_Strawberrycake.set("0")
E_chocolatecake.set("0")
E_cupcake.set("0")
E_MixedBerryCoffeeCake.set("0")
E_Pineapplecake.set("0")
E_BlackForestcake.set("0")
E_plumcake.set("0")
E_gemscake.set("0")

# DateofOrder.set(time.Strftime("%d/%m/%Y"))

# function declaration
def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Bakery System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():
    E_Maaza.set("0")
    E_Pepsi.set("0")
    E_Coke.set("0")
    E_Mirinda.set("0")
    E_Sprite.set("0")
    E_Milkshake.set("0")
    E_Chocolateshake.set("0")
    E_Orangejuice.set("0")

    E_Strawberrycake.set("0")
    E_chocolatecake.set("0")
    E_cupcake.set("0")
    E_MixedBerryCoffeeCake.set("0")
    E_Pineapplecake.set("0")
    E_BlackForestcake.set("0")
    E_plumcake.set("0")
    E_gemscake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtMaaza.configure(state=DISABLED)
    txtPepsi.configure(state=DISABLED)
    txtCoke.configure(state=DISABLED)
    txtMirinda.configure(state=DISABLED)
    txtSprite.configure(state=DISABLED)
    txtMilkshake.configure(state=DISABLED)
    txtChocolateshake.configure(state=DISABLED)
    txtOrangejuice.configure(state=DISABLED)
    txtStrawberrycake.configure(state=DISABLED)
    txtchocolatecake.configure(state=DISABLED)
    txtcupcake.configure(state=DISABLED)
    txtMixedBerryCoffeeCake.configure(state=DISABLED)
    txtPineapplecake.configure(state=DISABLED)
    txtBlackForestcake.configure(state=DISABLED)
    txtplumcake.configure(state=DISABLED)
    txtgemscake.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Maaza.get())
    Item2=float(E_Pepsi.get())
    Item3=float(E_Coke.get())
    Item4=float(E_Mirinda.get())
    Item5=float(E_Sprite.get())
    Item6=float(E_Milkshake.get())
    Item7=float( E_Chocolateshake.get())
    Item8=float( E_Orangejuice.get())

    Item9=float( E_Strawberrycake.get())
    Item10=float(E_chocolatecake.get())
    Item11=float(E_cupcake.get())
    Item12=float(E_MixedBerryCoffeeCake.get())
    Item13=float(E_Pineapplecake.get())
    Item14=float(E_BlackForestcake.get())
    Item15=float(E_plumcake.get())
    Item16=float(E_gemscake.get())

    priceofDrinks = (Item1 * 1.2) + (Item2 * 1.99) +(Item3 * 2.05) \
                  + (Item4 * 1.89) + (Item5 * 1.99) +(Item6 * 2.99) +(Item7 * 2.39) +(Item8 * 1.29)

    priceofCakes = (Item9 * 1.35) + (Item10 * 2.2) + (Item11 * 1.99) \
                    + (Item12 * 1.49) + (Item13 *1.8) + (Item14*1.67) + (Item5  * 1.6) + (Item16 * 1.99)

    DrinksPrice="$",str('%.2f'%(priceofDrinks))
    CakesPrice="$",str('%.2f'%(priceofCakes))
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC="$",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "$",str('%.2f'%(priceofDrinks+priceofCakes+1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "$",str('%.2f'%((priceofDrinks+priceofCakes+1.59)*0.15))
    PaidTax.set(Tax)
    TT = ((priceofDrinks+priceofCakes+1.59)*0.15)
    TC="$",str('%.2f'%(priceofDrinks+priceofCakes+1.59+TT))
    TotalCost.set(TC)

# Bill
# txtBill = Text(Bill_F, width =46, height=12, bg="white",bd=4,font=('arial',12,'bold'))
# txtBill.grid(row=0,column=0)

def chkMaaza():
    if (var1.get() == 1):
         txtMaaza.configure(state=NORMAL)
         txtMaaza.focus()
         txtMaaza.delete('0',END)
         E_Maaza.set("") 
    elif (var1.get() == 0):
         txtMaaza.configure(state=DISABLED)
         E_Maaza.set("0") 

def chkPepsi():
    if (var2.get() == 1):
         txtPepsi.configure(state=NORMAL)
         txtPepsi.focus()
         txtPepsi.delete('0',END)
         E_Pepsi.set("") 
    elif (var2.get() == 0):
         txtPepsi.configure(state=DISABLED)
         E_Pepsi.set("0") 


def chkCoke():
    if (var3.get() == 1):
         txtCoke.configure(state=NORMAL)
         txtCoke.focus()
         txtCoke.delete('0',END)
         E_Coke.set("") 
    elif (var3.get() == 0):
         txtCoke.configure(state=DISABLED)
         E_Coke.set("0") 


def chkMirinda():
    if (var4.get() == 1):
         txtMirinda.configure(state=NORMAL)
         txtMirinda.focus()
         txtMirinda.delete('0',END)
         E_Mirinda.set("") 
    elif (var4.get() == 0):
         txtMirinda.configure(state=DISABLED)
         E_Mirinda.set("0") 


def chkSprite():
    if (var5.get() == 1):
         txtSprite.configure(state=NORMAL)
         txtSprite.focus()
         txtSprite.delete('0',END)
         E_Sprite.set("") 
    elif (var5.get() == 0):
         txtSprite.configure(state=DISABLED)
         E_Sprite.set("0") 


def chkMilkshake():
    if (var6.get() == 1):
         txtMilkshake.configure(state=NORMAL)
         txtMilkshake.focus()
         txtMilkshake.delete('0',END)
         E_Maaza.set("") 
    elif (var6.get() == 0):
         txtMilkshake.configure(state=DISABLED)
         E_Milkshake.set("0") 


def chkChocolateshake():
    if (var7.get() == 1):
         txtChocolateshake.configure(state=NORMAL)
         txtChocolateshake.focus()
         txtChocolateshake.delete('0',END)
         E_Chocolateshake.set("") 
    elif (var7.get() == 0):
         txtChocolateshake.configure(state=DISABLED)
         E_Chocolateshake.set("0") 


def chkOrangejuice():
    if (var8.get() == 1):
         txtOrangejuice.configure(state=NORMAL)
         txtOrangejuice.focus()
         txtOrangejuice.delete('0',END)
         E_Orangejuice.set("") 
    elif (var8.get() == 0):
         txtOrangejuice.configure(state=DISABLED)
         E_Orangejuice.set("0") 


def chkStrawberrycake():
    if (var9.get() == 1):
         txtStrawberrycake.configure(state=NORMAL)
         txtStrawberrycake.focus()
         txtStrawberrycake.delete('0',END)
         E_Strawberrycake.set("") 
    elif (var9.get() == 0):
         txtStrawberrycake.configure(state=DISABLED)
         E_Strawberrycake.set("0") 


def chkchocolatecake():
    if (var10.get() == 1):
         txtchocolatecake.configure(state=NORMAL)
         txtchocolatecake.focus()
         txtchocolatecake.delete('0',END)
         E_chocolatecake.set("") 
    elif (var10.get() == 0):
         txtchocolatecake.configure(state=DISABLED)
         E_chocolatecake.set("0") 


def chkcupcake():
    if (var11.get() == 1):
         txtcupcake.configure(state=NORMAL)
         txtcupcake.focus()
         txtcupcake.delete('0',END)
         E_cupcake.set("") 
    elif (var11.get() == 0):
         txtcupcake.configure(state=DISABLED)
         E_cupcake.set("0") 


def chkMixedBerryCoffeeCake():
    if (var12.get() == 1):
         txtMixedBerryCoffeeCake.configure(state=NORMAL)
         txtMixedBerryCoffeeCake.focus()
         txtMixedBerryCoffeeCake.delete('0',END)
         E_MixedBerryCoffeeCake.set("") 
    elif (var12.get() == 0):
         txtMixedBerryCoffeeCake.configure(state=DISABLED)
         E_MixedBerryCoffeeCake.set("0") 


def chkPineapplecake():
    if (var13.get() == 1):
         txtPineapplecake.configure(state=NORMAL)
         txtPineapplecake.focus()
         txtPineapplecake.delete('0',END)
         E_Pineapplecake.set("") 
    elif (var13.get() == 0):
         txtPineapplecake.configure(state=DISABLED)
         E_Pineapplecake.set("0") 


def chkBlackForestcake():
    if (var14.get() == 1):
         txtBlackForestcake.configure(state=NORMAL)
         txtBlackForestcake.focus()
         txtBlackForestcake.delete('0',END)
         E_BlackForestcake.set("") 
    elif (var14.get() == 0):
         txtBlackForestcake.configure(state=DISABLED)
         E_BlackForestcake.set("0") 


def chkplumcake():
    if (var15.get() == 1):
         txtplumcake.configure(state=NORMAL)
         txtplumcake.focus()
         txtplumcake.delete('0',END)
         E_plumcake.set("") 
    elif (var15.get() == 0):
         txtplumcake.configure(state=DISABLED)
         E_plumcake.set("0") 

def chkgemscake():
    if (var16.get() == 1):
         txtgemscake.configure(state=NORMAL)
         txtgemscake.focus()
         txtgemscake.delete('0',END)
         E_gemscake.set("") 
    elif (var16.get() == 0):
         txtgemscake.configure(state=DISABLED)
         E_gemscake.set("0") 

def Bill():
    txtBill.delete("1.0",END)
    X = random.randint(10903, 609235)
    randomRef = str(X)
    Bill_Ref.set("Bill" + randomRef)

    # txtBill.insert(END, 'Bill Ref:\t\t\t'+Bill_F.get()+'\t'+DateofOrder.get()+"\n")
    txtBill.insert(END, 'Item:\t\t\t'+"Cost of Items\n")
    txtBill.insert(END, 'Maaza:\t\t\t'+ E_Maaza.get()+ "\n")
    txtBill.insert(END, 'Pepsi:\t\t\t'+ E_Pepsi.get()+ "\n")
    txtBill.insert(END, 'Coke:\t\t\t'+ E_Coke.get()+ "\n")
    txtBill.insert(END, 'Mirinda:\t\t\t'+ E_Mirinda.get()+ "\n")
    txtBill.insert(END, 'Sprite:\t\t\t'+ E_Sprite.get()+ "\n")
    txtBill.insert(END, 'Milkshake:\t\t\t'+ E_Milkshake.get()+ "\n")
    txtBill.insert(END, 'Chocolateshake:\t\t\t'+ E_Chocolateshake.get()+ "\n")
    txtBill.insert(END, 'Orangejuice:\t\t\t'+ E_Orangejuice.get()+ "\n")
    txtBill.insert(END, 'SchookCake:\t\t\t'+ E_Strawberrycake.get()+ "\n")
    txtBill.insert(END, 'chocolatecake:\t\t\t'+ E_chocolatecake.get()+ "\n")
    txtBill.insert(END, 'cupcake\t\t\t'+ E_cupcake.get()+ "\n")
    txtBill.insert(END, 'MixedBerryCoffeeCake:\t\t\t'+ E_MixedBerryCoffeeCake.get()+ "\n")
    txtBill.insert(END, 'Pineapplecake:\t\t\t'+ E_Pineapplecake.get()+ "\n")
    txtBill.insert(END, 'BlackForestcake:\t\t\t'+ E_BlackForestcake.get()+ "\n")
    txtBill.insert(END, 'plumcake:\t\t\t'+ E_plumcake.get()+ "\n")
    txtBill.insert(END, 'gemscake:\t\t\t'+ E_gemscake.get()+ "\n")
    txtBill.insert(END, 'cost of drinks:\t\t\t'+ CostofDrinks.get()+ '\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtBill.insert(END, 'cost of cakes:\t\t\t'+ CostofCakes.get()+ '\nSubTotal:\t\t\t\t'+(SubTotal.get())+"\n")
    txtBill.insert(END, 'service charge:\t\t\t'+ ServiceCharge.get()+ '\nTotal cost:\t\t\t\t'+str(TotalCost.get())+"\n")
    
    

# drinks
Maaza = Checkbutton(Drinks_F, text="Maaza", variable =var1, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkMaaza).grid(row=0, sticky=W)

Pepsi= Checkbutton(Drinks_F, text="Pepsi", variable =var2, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkPepsi).grid(row=1, sticky=W)

Coke= Checkbutton(Drinks_F, text="Coke", variable =var3, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkCoke).grid(row=2, sticky=W) 

Mirinda= Checkbutton(Drinks_F, text="Mirinda", variable =var4, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkMirinda).grid(row=3, sticky=W)

Sprite= Checkbutton(Drinks_F, text="Sprite", variable =var5, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkSprite).grid(row=4, sticky=W)

Milkshake= Checkbutton(Drinks_F, text="Milkshake", variable =var6, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkMilkshake).grid(row=5, sticky=W)

Chocolateshake= Checkbutton(Drinks_F, text="Chocolateshake", variable =var7, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkChocolateshake).grid(row=6, sticky=W)

Orangejuice= Checkbutton(Drinks_F, text="Orange juice", variable =var8, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkOrangejuice).grid(row=7, sticky=W)

# entry box for drinks
txtMaaza = Entry(Drinks_F, font=('arial',16,'bold'), textvariable=E_Maaza, bd=8,width=6, justify='left', state=DISABLED)
txtMaaza.grid(row=0,column=1)

txtPepsi = Entry(Drinks_F, font=('arial',16,'bold'), textvariable=E_Pepsi, bd=8,width=6, justify='left', state=DISABLED)
txtPepsi.grid(row=1,column=1)

txtCoke = Entry(Drinks_F, font=('arial',16,'bold'), textvariable=E_Coke, bd=8,width=6, justify='left', state=DISABLED)
txtCoke.grid(row=2,column=1)

txtMirinda = Entry(Drinks_F, font=('arial',16,'bold'), textvariable=E_Mirinda, bd=8,width=6, justify='left', state=DISABLED)
txtMirinda.grid(row=3,column=1)

txtSprite = Entry(Drinks_F, font=('arial',16,'bold'), textvariable=E_Sprite, bd=8,width=6, justify='left', state=DISABLED)
txtSprite.grid(row=4,column=1)

txtMilkshake = Entry(Drinks_F, font=('arial',16,'bold'), textvariable=E_Milkshake, bd=8, width=6,justify='left', state=DISABLED)
txtMilkshake.grid(row=5,column=1)

txtChocolateshake = Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Chocolateshake,bd=8,width=6,justify='left', state=DISABLED)
txtChocolateshake.grid(row=6,column=1)

txtOrangejuice = Entry(Drinks_F, font=('arial',16,'bold'),textvariable=E_Orangejuice,bd=8,width=6,justify='left', state=DISABLED)
txtOrangejuice.grid(row=7,column=1)


# cakes
Strawberrycake= Checkbutton(Cake_F, text="Strawberrycake", variable =var9, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkStrawberrycake ).grid(row=0, sticky=W)

chocolatecake= Checkbutton(Cake_F, text="chocolatecake", variable =var10, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command= chkchocolatecake).grid(row=1, sticky=W) 

cupcake= Checkbutton(Cake_F, text="cupcake", variable =var11, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkcupcake ).grid(row=2, sticky=W)

MixedBerryCoffeeCake= Checkbutton(Cake_F, text="MixedBerryCoffeeCake", variable =var12, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command= chkMixedBerryCoffeeCake).grid(row=3, sticky=W)

Pineapplecake= Checkbutton(Cake_F, text="Pineapplecake", variable =var13, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkPineapplecake).grid(row=4, sticky=W)

BlackForestcake= Checkbutton(Cake_F, text="BlackForestcake", variable =var14, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command= chkBlackForestcake).grid(row=5, sticky=W)

plumcake= Checkbutton(Cake_F, text="plumcake", variable =var15, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkplumcake).grid(row=6, sticky=W)

gemscake= Checkbutton(Cake_F, text="gemscake", variable =var16, onvalue=1, offvalue=0, font=('arial', 18, 'bold'), bg='LightGray',command=chkgemscake).grid(row=7, sticky=W)

# entry box for cakes
txtStrawberrycake = Entry(Cake_F, font=('arial',16,'bold'),textvariable=E_Strawberrycake, bd=8,width=6,justify='left',state=DISABLED)
txtStrawberrycake.grid(row=0,column=1)

txtchocolatecake = Entry(Cake_F, font=('arial',16,'bold'),textvariable=E_chocolatecake, bd=8,width=6,justify='left',state=DISABLED)
txtchocolatecake.grid(row=1,column=1)

txtcupcake = Entry(Cake_F, font=('arial',16,'bold'), textvariable=E_cupcake, bd=8,width=6,justify='left',state=DISABLED)
txtcupcake.grid(row=2,column=1)

txtMixedBerryCoffeeCake = Entry(Cake_F, font=('arial',16,'bold'),textvariable=E_MixedBerryCoffeeCake, bd=8,width=6,justify='left',state=DISABLED)
txtMixedBerryCoffeeCake.grid(row=3,column=1)

txtPineapplecake = Entry(Cake_F, font=('arial',16,'bold'), textvariable=E_Pineapplecake, bd=8,width=6,justify='left',state=DISABLED)
txtPineapplecake.grid(row=4,column=1)

txtBlackForestcake = Entry(Cake_F, font=('arial',16,'bold'),textvariable=E_BlackForestcake, bd=8,width=6,justify='left',state=DISABLED)
txtBlackForestcake.grid(row=5,column=1)

txtplumcake = Entry(Cake_F, font=('arial',16,'bold'), textvariable=E_plumcake, bd=8,width=6,justify='left',state=DISABLED)
txtplumcake.grid(row=6,column=1)

txtgemscake = Entry(Cake_F, font=('arial',16,'bold'),textvariable=E_gemscake, bd=8,width=6,justify='left',state=DISABLED)
txtgemscake.grid(row=7,column=1)

# totals cost
lblCostofDrinks = Label(Cost_F, font=('arial', 14, 'bold'), text="cost of drinks\t ",bg='LightGray',fg='black')
lblCostofDrinks.grid(row=0, column=0,sticky=W)
txtCostofDrinks = Entry(Cost_F, font=('arial',14,'bold'), textvariable=CostofDrinks, bd=7, bg="white",insertwidth=2,justify=RIGHT)
txtCostofDrinks.grid(row=0,column=1)

lblCostofCakes = Label(Cost_F, font=('arial', 14, 'bold'), text="cost of cakes\t ",bg='LightGray',fg='black')
lblCostofCakes.grid(row=1, column=0,sticky=W)
txtCostofCakes = Entry(Cost_F, font=('arial',14,'bold'), bd=7,textvariable=CostofCakes, bg="white",insertwidth=2,justify=RIGHT)
txtCostofCakes.grid(row=1,column=1)

lblServiceCharge = Label(Cost_F, font=('arial', 14, 'bold'), text="service charge\t ",bg='LightGray',fg='black')
lblServiceCharge.grid(row=2, column=0,sticky=W)
txtServiceCharge = Entry(Cost_F, font=('arial',14,'bold'), textvariable=ServiceCharge, bd=7, bg="white",insertwidth=2,justify=RIGHT)
txtServiceCharge.grid(row=2,column=1)

# payment information
lblPaidTax = Label(Cost_F, font=('arial', 14, 'bold'), text="\tTax paid\t ",bd=7,bg='LightGray',fg='black')
lblPaidTax.grid(row=0, column=2,sticky=W)
txtPaidTax = Entry(Cost_F, font=('arial',14,'bold'),textvariable=PaidTax, bd=7, bg="white",insertwidth=2,justify=RIGHT)
txtPaidTax.grid(row=0,column=3)

lblSubTotal = Label(Cost_F, font=('arial', 14, 'bold'), text="\tSub Total ",bd=7, bg='LightGray',fg='black')
lblSubTotal.grid(row=1, column=2,sticky=W)
txtSubTotal = Entry(Cost_F, font=('arial',14,'bold'),textvariable=SubTotal,bd=7, bg="white",insertwidth=2,justify=RIGHT)
txtSubTotal.grid(row=1,column=3)

lblTotalCost = Label(Cost_F, font=('arial', 14, 'bold'), text="\tTotal Cost",bd=7, bg='LightGray',fg='black')
lblTotalCost.grid(row=2, column=2,sticky=W)
txtTotalCost = Entry(Cost_F, font=('arial',14,'bold'),textvariable=TotalCost, bd=7, bg="white",insertwidth=2,justify=RIGHT)
txtTotalCost.grid(row=2,column=3)


# Bill
txtBill = Text(Bill_F, width =46, height=12, bg="white",bd=4,font=('arial',12,'bold'))
txtBill.grid(row=0,column=0)


# buttons
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Total",bg="LightGray",command=CostofItem).grid(row=0,column=0)
btnBill=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Bill",bg="LightGray",command=Bill).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Reset",bg="LightGray",command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg="black",font=('arial',16,'bold'),width=4,text="Exit",bg="LightGray",command=iExit).grid(row=0,column=3)


# calculator display
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

txtDisplay = Entry(Cal_F, width =45, bg="white",bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

# calculator buttons
btn7= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="7"
            , bg="LightGray",command=lambda:btnClick(7)).grid(row=2, column=0)
btn8= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="8"
            , bg="LightGray",command=lambda:btnClick(8)).grid(row=2, column=1)
btn9= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="9"
            , bg="LightGray",command=lambda:btnClick(9)).grid(row=2, column=2)
btnAdd= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="+"
            , bg="LightGray",command=lambda:btnClick("+")).grid(row=2, column=3)
# calculator buttons
btn4= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="4"
            , bg="LightGray",command=lambda:btnClick(4)).grid(row=3, column=0)
btn5= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="5"
            , bg="LightGray",command=lambda:btnClick(5)).grid(row=3, column=1)
btn6= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="6"
            , bg="LightGray",command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="-"
            , bg="LightGray",command=lambda:btnClick("-")).grid(row=3, column=3)

# calculator buttons
btn1= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="1"
            , bg="LightGray",command=lambda:btnClick(1)).grid(row=4, column=0)
btn2= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="2"
            , bg="LightGray",command=lambda:btnClick(2)).grid(row=4, column=1)
btn3= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="3"
            , bg="LightGray",command=lambda:btnClick(3)).grid(row=4, column=2)
btnMulti= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="*"
            , bg="LightGray",command=lambda:btnClick("*")).grid(row=4, column=3)

# calculator buttons
btn0= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="0"
            , bg="LightGray",command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="C"
            , bg="LightGray",command=btnClear).grid(row=5, column=1)
btnEquals= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="="
            , bg="LightGray",command=btnEquals).grid(row=5, column=2)
btnDiv= Button(Buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial', 16, 'bold'), width=4, text="/"
            , bg="LightGray",command=lambda:btnClick("/")).grid(row=5, column=3)

root.mainloop()




