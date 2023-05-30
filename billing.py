from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time

class Customer:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Customer Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="teal")

        ABC=Frame(self.root,bg="aquamarine",bd=15,relief=RIDGE)
        ABC.grid()
        ABC1=Frame(ABC,bd=5, height=100,width=1330,padx=10,bg="aquamarine",relief=RIDGE)
        ABC1.grid(row=0, column=0, columnspan=5,sticky=W)
        ABC2=Frame(ABC,bd=5, height=500,width=328.5,padx=10,bg="turquoise",relief=RIDGE)
        ABC2.grid(row=1, column=0, sticky=W)
        ABC3=Frame(ABC,bd=5, height=500,width=328.5,padx=10,bg="aquamarine",relief=RIDGE)
        ABC3.grid(row=1, column=1, sticky=W)
        ABC4=Frame(ABC,bd=5, height=500,width=328.5,padx=10,bg="turquoise",relief=RIDGE)
        ABC4.grid(row=1, column=2, sticky=W)
        
        ABC5=Frame(ABC,bd=5, height=500,width=315.5,padx=10,bg="turquoise",relief=RIDGE)
        ABC5.grid(row=1, column=3, sticky=W)
        
        ABC6=Frame(ABC5,bd=5, height=370,width=300,padx=10,bg="turquoise",relief=RIDGE)
        ABC6.grid(row=0, column=0, sticky=W)
        ABC7=Frame(ABC5,bd=5, height=100,width=300,padx=10,bg="aquamarine",relief=RIDGE)
        ABC7.grid(row=1, column=0, columnspan=4, sticky=W)
         
        #----------------------------------------------------------------------------------------------------------------------------------------------------------------

        Date1=StringVar()
        Time1=StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%H:%M:%S"))

        self.lblTitle=Label(ABC1, textvariable=Date1, font=('Arial',31),pady=31,bd=15,bg='turquoise'
                            , fg='black').grid(row=0,column=0)
        self.lblTitle=Label(ABC1, text='CUSTOMER BILLING SYSTEM', font=('cooper black',44),pady=20,bd=15
                            ,bg='turquoise'
                            , fg='black').grid(row=0,column=1)
        self.lblTitle=Label(ABC1, textvariable=Time1, font=('Arial',31),pady=31,bd=15,bg='turquoise'
                            , fg='black').grid(row=0,column=2)


        self.lblTitle=Label(ABC3, text='SNACKS', font=('Arial',15,'bold'),pady=2,bd=5
                            ,bg='aquamarine',fg='black', justify='center',height=2).grid(row=0)

        self.lblTitle=Label(ABC3, text='DESSERTS', font=('Arial',15,'bold'),pady=2,bd=5
                            ,bg='aquamarine',fg='black', justify='center',height=2).grid(row=11)

        self.lblTitle=Label(ABC4, text='DRINKS', font=('Arial',15,'bold'),pady=2,bd=5
                            ,bg='turquoise',fg='black', justify='center',height=2).grid(row=2)

        self.lblTitle=Label(ABC4, text='Tax & Total Sum', font=('Arial',15,'bold'),pady=2,bd=5
                            ,bg='turquoise',fg='black', justify='center').grid(row=10)
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------
        def Reset():
                self.txtReceipt.delete("1.0",END)
                E_chick.set("0")
                E_vsand.set("0")
                E_chickcb.set("0")
                E_chicksa.set("0")
                E_pizza.set("0")
                E_ice.set("0")
                E_chocol.set("0")
                E_chocob.set("0")
                E_t.set("0")
                E_cof.set("0")
                E_las.set("0")
                E_milks.set("0")
                E_manj.set("0")
                E_aamp.set("0")
                E_vmomo.set("0")
                E_fmomo.set("0")
                E_chimo.set("0")
                E_sam.set("0")
                E_coca.set("0")
                E_chaw.set("0")

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
                var17.set(0)
                var18.set(0)
                var19.set(0)
                var20.set(0)

                Customer_ref.set("")
                FirstName.set("")
                LastName.set("")
                Gender.set("")
                Address.set("")
                PinCode.set("")
                Mobile_No.set("")
                Email.set("")
                Nationality.set("")
                Date_Of_Birth.set("")
                Customer_ref.set("")
                Payment_Type.set("")
                Date.set("")
                
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------
        def chkchick():
                if (var1.get() ==1):
                    self.txtchick.configure(state=NORMAL)
                    self.txtchick.focus()
                    self.txtchick.delete('0',END)
                    E_chick.set("")
                elif var1.get() ==0:
                    self.txtchick.configure(state=DISABLED)
                    self.txtchick.set("0")

        def chkvsand():
              if (var2.get() ==1):
                 self.txtvsand.configure(state=NORMAL)
                 self.txtvsand.focus()
                 self.txtvsand.delete('0',END)
                 E_vsand.set("")
              elif var2.get() ==0:
                 self.txtvsand.configure(state=DISABLED)
                 self.txtvsand.set("0")

        def chkchicksa():
            if (var3.get() ==1):
                self.txtchicksa.configure(state=NORMAL)
                self.txtchicksa.focus()
                self.txtchicksa.delete('0',END)
                E_chicksa.set("")
            elif var3.get() ==0:
                self.txtchicksa.configure(state=DISABLED)
                self.txtchicksa.set("0")

        def chkchickcb():
            if (var4.get() ==1):
                self.txtchickcb.configure(state=NORMAL)
                self.txtchickcb.focus()
                self.txtchickcb.delete('0',END)
                E_chickcb.set("")
            elif var4.get() ==0:
                self.txtchickcb.configure(state=DISABLED)
                self.txtchickcb.set("0")

        def chkpizza():
            if (var5.get() ==1):
                self.txtpizza.configure(state=NORMAL)
                self.txtpizza.focus()
                self.txtpizza.delete('0',END)
                E_pizza.set("")
            elif var5.get() ==0:
                self.txtpizza.configure(state=DISABLED)
                self.txtpizza.set("0")

        def chkvmomo():
            if (var6.get() ==1):
                self.txtvmomo.configure(state=NORMAL)
                self.txtvmomo.focus()
                self.txtvmomo.delete('0',END)
                E_vmomo.set("")
            elif var6.get() ==0:
                self.txtvmomo.configure(state=DISABLED)
                self.txtvmomo.set("0")

        def chkchimo():
            if (var7.get() ==1):
                self.txtchimo.configure(state=NORMAL)
                self.txtchimo.focus()
                self.txtchimo.delete('0',END)
                E_chimo.set("")
            elif var7.get() ==0:
                self.txtchimo.configure(state=DISABLED)
                self.txtchimo.set("0")

        def chkfmomo():
            if (var8.get() ==1):
                self.txtfmomo.configure(state=NORMAL)
                self.txtfmomo.focus()
                self.txtfmomo.delete('0',END)
                E_fmomo.set("")
            elif var8.get() ==0:
                self.txtfmomo.configure(state=DISABLED)
                self.txtfmomo.set("0")

        def chksam():
            if (var9.get() ==1):
                self.txtsam.configure(state=NORMAL)
                self.txtsam.focus()
                self.txtsam.delete('0',END)
                E_sam.set("")
            elif var9.get() ==0:
                self.txtsam.configure(state=DISABLED)
                self.txtsam.set("0")

        def chkchaw():
            if (var10.get() ==1):
                self.txtchaw.configure(state=NORMAL)
                self.txtchaw.focus()
                self.txtchaw.delete('0',END)
                E_chaw.set("")
            elif var10.get() ==0:
                self.txtchaw.configure(state=DISABLED)
                self.txtchaw.set("0")

        def chkice():
            if (var11.get() ==1):
                self.txtice.configure(state=NORMAL)
                self.txtice.focus()
                self.txtice.delete('0',END)
                E_ice.set("")
            elif var11.get() ==0:
                self.txtice.configure(state=DISABLED)
                self.txtice.set("0")

        def chkchocol():
            if (var12.get() ==1):
                self.txtchocol.configure(state=NORMAL)
                self.txtchocol.focus()
                self.txtchocol.delete('0',END)
                E_chocol.set("")
            elif var12.get() ==0:
                self.txtchocol.configure(state=DISABLED)
                self.txtchocol.set("0")

        def chkchocob():
            if (var13.get() ==1):
                self.txtchocob.configure(state=NORMAL)
                self.txtchocob.focus()
                self.txtchocob.delete('0',END)
                E_chocob.set("")
            elif var13.get() ==0:
                self.txtchocob.configure(state=DISABLED)
                self.txtchocob.set("0")

        def chkt():
            if (var14.get() ==1):
                self.txtt.configure(state=NORMAL)
                self.txtt.focus()
                self.txtt.delete('0',END)
                E_t.set("")
            elif var14.get() ==0:
                self.txtt.configure(state=DISABLED)
                self.txtt.set("0")

        def chkcof():
            if (var15.get() ==1):
                self.txtcof.configure(state=NORMAL)
                self.txtcof.focus()
                self.txtcof.delete('0',END)
                E_cof.set("")
            elif var15.get() ==0:
                self.txtcof.configure(state=DISABLED)
                self.txtcof.set("0")

        def chklas():
            if (var16.get() ==1):
                self.txtlas.configure(state=NORMAL)
                self.txtlas.focus()
                self.txtlas.delete('0',END)
                E_las.set("")
            elif var16.get() ==0:
                self.txtlas.configure(state=DISABLED)
                self.txtlas.set("0")
               
        def chkmilks():
            if (var17.get() ==1):
                self.txtmilks.configure(state=NORMAL)
                self.txtmilks.focus()
                self.txtmilks.delete('0',END)
                E_milks.set("")
            elif var17.get() ==0:
                self.txtmilks.configure(state=DISABLED)
                self.txtmilks.set("0")
                
        def chkmanj():
            if (var18.get() ==1):
                self.txtmanj.configure(state=NORMAL)
                self.txtmanj.focus()
                self.txtmanj.delete('0',END)
                E_manj.set("")
            elif var18.get() ==0:
                self.txtmanj.configure(state=DISABLED)
                self.txtmanj.set("0")
            
        def chkaamp():
            if (var19.get() ==1):
                self.txtaamp.configure(state=NORMAL)
                self.txtaamp.focus()
                self.txtaamp.delete('0',END)
                E_aamp.set("")
            elif var19.get() ==0:
                self.txtaamp.configure(state=DISABLED)
                self.txtaamp.set("0")
     
        def chkcoca():
            if (var20.get() ==1):
                self.txtcoca.configure(state=NORMAL)
                self.txtcoca.focus()
                self.txtcoca.delete('0',END)
                E_coca.set("")
            elif var20.get() ==0:
                self.txtcoca.configure(state=DISABLED)
                self.txtcoca.set("0")
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------
        def costOfItem():
            Customer_ref.set(random.randint(19800,9875648))
            Item1=float(E_chick.get())
            Item2=float(E_vsand.get())
            Item3=float(E_chicksa.get())
            Item4=float(E_chickcb.get())
            Item5=float(E_pizza.get())
            Item6=float(E_vmomo.get())
            Item7=float(E_chimo.get())
            Item8=float(E_fmomo.get())
            Item9=float(E_sam.get())
            Item10=float(E_chaw.get())
            Item11=float(E_ice.get())
            Item12=float(E_chocol.get())
            Item13=float(E_chocob.get())
            Item14=float(E_t.get())
            Item15=float(E_cof.get())
            Item16=float(E_las.get())
            Item17=float(E_milks.get())
            Item18=float(E_manj.get())
            Item19=float(E_aamp.get())
            Item20=float(E_coca.get())


            price=(Item1*30)+(Item2*30)+(Item3*40)+(Item4*50)+(Item5*70)+(Item6*30)+(Item7*45)+(Item8*40)+(Item9*5)+(Item10*35)+(Item11*30)\
                    +(Item12*40)+(Item13*40)+(Item14*10)+(Item15*15)+(Item16*20)+(Item17*30)+(Item18*25)+(Item19*20)+(Item20*15)
            sub_total_of_items="Rs", str('%.2f'% price)
            SubTotal.set(sub_total_of_items)

            Tax="Rs", str('%.2f'%((price)*0.15))
             
            PaidTax.set(Tax)

            TTax=((price)*0.15)
            TCost="Rs", str('%.2f'% (price+TTax))
             
            TotalCost.set(TCost)

            self.txtReceipt.insert(END,'Customer ref.set: \t\t'+ Customer_ref.get()+ "\n")
            self.txtReceipt.insert(END,'Items\t\t\t'+ "Cost of Items \n")
            
            self.txtReceipt.insert(END,'Chicken Cutlet: \t\t\t'+ E_chick.get()+ "\n")
            self.txtReceipt.insert(END,'Veg. Sandwitch: \t\t\t'+ E_vsand.get()+ "\n")
            self.txtReceipt.insert(END,'Chicken Sandwich: \t\t\t'+ E_chicksa.get()+ "\n")
            self.txtReceipt.insert(END,'Chicken Cheese Balls: \t\t\t'+ E_chickcb.get()+ "\n")
            self.txtReceipt.insert(END,'Pizza: \t\t\t'+ E_pizza.get()+ "\n")
            self.txtReceipt.insert(END,'Veg. Momo: \t\t\t'+ E_vmomo.get()+ "\n")
            self.txtReceipt.insert(END,'Chicken Momo: \t\t\t'+ E_chimo.get()+ "\n")
            self.txtReceipt.insert(END,'Fried Momo: \t\t\t'+ E_fmomo.get()+ "\n")
            self.txtReceipt.insert(END,'Samosa: \t\t\t'+ E_sam.get()+ "\n")
            self.txtReceipt.insert(END,'Chowmin: \t\t\t'+ E_chaw.get()+ "\n")
            self.txtReceipt.insert(END,'Ice-Cream: \t\t\t'+ E_ice.get()+ "\n")
            self.txtReceipt.insert(END,'ChocoLava: \t\t\t'+ E_chocol.get()+ "\n")
            self.txtReceipt.insert(END,'Choco-Brownie: \t\t\t'+ E_chocob.get()+ "\n")
            self.txtReceipt.insert(END,'Tea: \t\t\t\t'+ E_t.get()+ "\n")
            self.txtReceipt.insert(END,'Coffee: \t\t\t'+ E_cof.get()+ "\n")
            self.txtReceipt.insert(END,'Lassi: \t\t\t'+ E_las.get()+ "\n")
            self.txtReceipt.insert(END,'Milkshake: \t\t\t'+ E_milks.get()+ "\n")
            self.txtReceipt.insert(END,'Mango-Juice: \t\t\t'+ E_manj.get()+ "\n")
            self.txtReceipt.insert(END,'Aampanna: \t\t\t'+ E_aamp.get()+ "\n")
            self.txtReceipt.insert(END,'Coca-cola: \t\t\t'+ E_coca.get()+ "\n")

            self.txtReceipt.insert(END,'\nTax Paid:\t\t'+ PaidTax.get()+ "\n")
            self.txtReceipt.insert(END,'\nSubTotal:\t\t'+ str(SubTotal.get())+ "\n")
            self.txtReceipt.insert(END,'\nTotalCost:\t\t'+ str(SubTotal.get()))

                        
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("Customer Billing System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.btnTotal= Button(ABC7, padx=2, pady=2, bd=7, fg='black', font=('arial',16,'bold'), width=7, height=2,
                              bg='teal', text='Total',command=costOfItem).grid(row=0,column=0)
        self.btnReset= Button(ABC7, padx=2, pady=2, bd=7, fg='black', font=('arial',16,'bold'), width=7, height=2,
                              bg='teal', text='Reset',command=Reset).grid(row=0,column=1)
        self.btnExit= Button(ABC7, padx=2, pady=2, bd=7, fg='black', font=('arial',16,'bold'), width=8, height=2,
                              bg='teal', text='Exit',command=iExit).grid(row=0,column=2)
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------

        self.txtReceipt= Text(ABC6, height=28, width=47,bd=10,font=('arial',9,'bold') )
        self.txtReceipt.grid(row=0, column=0)
        
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------
        Customer_ref=StringVar()
        FirstName=StringVar()
        LastName=StringVar()
        Gender=StringVar()
        Address=StringVar()
        PinCode=StringVar()
        Mobile_No=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        Date_Of_Birth=StringVar()
        Customer_ref=StringVar()
        Payment_Type=StringVar()
        Date=StringVar()
        PaidTax=StringVar()
        SubTotal=StringVar()
        TotalCost=StringVar()

        Customer_ref.set(random.randint(19800,9875648))

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16=IntVar()
        var17=IntVar()
        var18=IntVar()
        var19=IntVar()
        var20=IntVar()
        

        E_chick=StringVar()
        E_vsand=StringVar()
        E_chickcb=StringVar()
        E_chicksa=StringVar()
        E_pizza=StringVar()
        E_ice=StringVar()
        E_chocol=StringVar()
        E_chocob=StringVar()
        E_t=StringVar()
        E_cof=StringVar()
        E_las=StringVar()
        E_milks=StringVar()
        E_manj=StringVar()
        E_aamp=StringVar()
        E_vmomo=StringVar()
        E_fmomo=StringVar()
        E_chimo=StringVar()
        E_sam=StringVar()
        E_coca=StringVar()
        E_chaw=StringVar()


        E_chick.set("0")
        E_vsand.set("0")
        E_chickcb.set("0")
        E_chicksa.set("0")
        E_pizza.set("0")
        E_ice.set("0")
        E_chocol.set("0")
        E_chocob.set("0")
        E_t.set("0")
        E_cof.set("0")
        E_las.set("0")
        E_milks.set("0")
        E_manj.set("0")
        E_aamp.set("0")
        E_vmomo.set("0")
        E_fmomo.set("0")
        E_chimo.set("0")
        E_sam.set("0")
        E_coca.set("0")
        E_chaw.set("0")
        


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        

        
        self.lblCustomer_ref=Label(ABC2,font=('arial',12,'bold'),text='Customer ref:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblCustomer_ref.grid(row=0,column=0,sticky=W)
        self.txtCustomer_ref=Entry(ABC2,font=('arial',12,'bold'),textvariable=Customer_ref,width=12)
        self.txtCustomer_ref.grid(row=0,column=1,pady=3)

        self.lblFirstName=Label(ABC2,font=('arial',12,'bold'),text='FirstName:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblFirstName.grid(row=1,column=0,sticky=W)
        self.txtFirstName=Entry(ABC2,font=('arial',12,'bold'),textvariable=FirstName,width=12, )
        self.txtFirstName.grid(row=1,column=1,pady=3)

        self.lblLastName=Label(ABC2,font=('arial',12,'bold'),text='LastName:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblLastName.grid(row=2,column=0,sticky=W)
        self.txtLastName=Entry(ABC2,font=('arial',12,'bold'),textvariable=LastName,width=12)
        self.txtLastName.grid(row=2,column=1,pady=3)

        self.lblGender=Label(ABC2,font=('arial',12,'bold'),text='Gender:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblGender.grid(row=3,column=0,sticky=W)
        self.cboGender=ttk.Combobox(ABC2,state='readonly',textvariable=Gender,font=('arial',12,'bold'),width=12)
        self.cboGender['values']=('','Male','Female','Others')
        self.cboGender.current(0)
        self.cboGender.grid(row=3,column=1,pady=3,padx=15)


        self.lblAddress=Label(ABC2,font=('arial',12,'bold'),text='Address:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblAddress.grid(row=4,column=0,sticky=W)
        self.txtAddress=Entry(ABC2,font=('arial',12,'bold'),textvariable=Address,width=12)
        self.txtAddress.grid(row=4,column=1,pady=3)

        self.lblPinCode=Label(ABC2,font=('arial',12,'bold'),text='Pin Code:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblPinCode.grid(row=5,column=0,sticky=W)
        self.txtPinCode=Entry(ABC2,font=('arial',12,'bold'),textvariable=PinCode,width=12)
        self.txtPinCode.grid(row=5,column=1,pady=3)

        self.lblMobile_No=Label(ABC2,font=('arial',12,'bold'),text='Mobile No:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblMobile_No.grid(row=6,column=0,sticky=W)
        self.txtMobile_No=Entry(ABC2,font=('arial',12,'bold'),textvariable=Mobile_No,width=12)
        self.txtMobile_No.grid(row=6,column=1,pady=3)

        self.lblEmail=Label(ABC2,font=('arial',12,'bold'),text='Email:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblEmail.grid(row=7,column=0,sticky=W)
        self.txtEmail=Entry(ABC2,font=('arial',12,'bold'),textvariable=Email,width=12, )
        self.txtEmail.grid(row=7,column=1,pady=3)

        self.lblNationality=Label(ABC2,font=('arial',12,'bold'),text='Nationality:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblNationality.grid(row=8,column=0,sticky=W)
        self.txtNationality=Entry(ABC2,font=('arial',12,'bold'),textvariable=Nationality,width=12, )
        self.txtNationality.grid(row=8,column=1,pady=3)

        self.lblDate_Of_Birth=Label(ABC2,font=('arial',12,'bold'),text='Date Of Birth:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblDate_Of_Birth.grid(row=9,column=0,sticky=W)
        self.txtDate_Of_Birth=Entry(ABC2,font=('arial',12,'bold'),textvariable=Date_Of_Birth,width=12, )
        self.txtDate_Of_Birth.grid(row=9,column=1,pady=3)

        self.lblPayment_Type=Label(ABC2,font=('arial',12,'bold'),text='Payment Type:',padx=2,fg='black', bg='turquoise',height=2 )
        self.lblPayment_Type.grid(row=10,column=0,sticky=W)
        self.cboPayment_Type=ttk.Combobox(ABC2,textvariable=Payment_Type,state='readonly',font=('arial',12,'bold'),width=12)
        self.cboPayment_Type['value']=('','PhonePay','Paytm','Cash')
        self.cboPayment_Type.current(0)
        self.cboPayment_Type.grid(row=10,column=1,pady=3,padx=20)


        self.lblDate=Label(ABC2,font=('arial',12,'bold'),text='Date:',padx=2,fg='black', bg='turquoise' ,height=2)
        self.lblDate.grid(row=11,column=0,sticky=W)
        Date.set(time.strftime("%d/%m/%y"))
        self.lblDate=Label(ABC2, textvariable=Date1, font=('Arial',12,'bold'),padx=2,bd=2,bg='white',width=12
                            , fg='black').grid(row=11,column=1)

        self.lblPaidTax=Label(ABC4,font=('arial',12,'bold'),text='Paid Tax:',padx=2,fg='black', bg='white' )
        self.lblPaidTax.grid(row=11,column=0,sticky=W)
        self.txtPaidTax=Entry(ABC4,font=('arial',12,'bold'),textvariable=PaidTax,width=12, )
        self.txtPaidTax.grid(row=11,column=1,pady=3)

        self.lblSubTotal=Label(ABC4,font=('arial',12,'bold'),text='Sub Total:',padx=2,fg='black', bg='white' )
        self.lblSubTotal.grid(row=12,column=0,sticky=W)
        self.txtSubTotal=Entry(ABC4,font=('arial',12,'bold'),textvariable=SubTotal,width=12, )
        self.txtSubTotal.grid(row=12,column=1,pady=3)

        self.lblTotalCost=Label(ABC4,font=('arial',12,'bold'),text='Total Cost:',padx=2,fg='black', bg='white' )
        self.lblTotalCost.grid(row=13,column=0,sticky=W)
        self.txtTotalCost=Entry(ABC4,font=('arial',12,'bold'),textvariable=TotalCost,width=12, )
        self.txtTotalCost.grid(row=13,column=1,pady=3)

        

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.chick=Checkbutton(ABC3,text='Chicken Cutlet',variable=var1,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkchick).grid(row=1,sticky=W)
        self.txtchick=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_chick,bd=8,width=10,justify='left',state=DISABLED)
        self.txtchick.grid(row=1,column=1)
        
        self.vsand=Checkbutton(ABC3,text='Veg. Sandwitch',variable=var2,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkvsand).grid(row=2,sticky=W)
        self.txtvsand=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_vsand,bd=8,width=10
                            ,justify='left',state=DISABLED)
        self.txtvsand.grid(row=2,column=1)

        self.chicksa=Checkbutton(ABC3,text='Chicken Sandwich',variable=var3,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkchicksa).grid(row=3,sticky=W)
        self.txtchicksa=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_chicksa,bd=8,width=10,justify='left',state=DISABLED)
        self.txtchicksa.grid(row=3,column=1)

        self.chickcb=Checkbutton(ABC3,text='Chicken Cheese Balls',variable=var4,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkchickcb).grid(row=4,sticky=W)
        self.txtchickcb=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_chickcb,bd=8,width=10,justify='left',state=DISABLED)
        self.txtchickcb.grid(row=4,column=1)

        self.pizza=Checkbutton(ABC3,text='Pizza',variable=var5,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkpizza).grid(row=5,sticky=W)
        self.txtpizza=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_pizza,bd=8,width=10,justify='left',state=DISABLED)
        self.txtpizza.grid(row=5,column=1)

        self.vmomo=Checkbutton(ABC3,text='Veg. Momo',variable=var6,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkvmomo).grid(row=6,sticky=W)
        self.txtvmomo=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_vmomo,bd=8,width=10,justify='left',state=DISABLED)
        self.txtvmomo.grid(row=6,column=1)

        self.chimo=Checkbutton(ABC3,text='Chicken Momo',variable=var7,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkchimo).grid(row=7,sticky=W)
        self.txtchimo=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_chimo,bd=8,width=10,justify='left',state=DISABLED)
        self.txtchimo.grid(row=7,column=1)

        self.fmomo=Checkbutton(ABC3,text='Fried Momo',variable=var8,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkfmomo).grid(row=8,sticky=W)
        self.txtfmomo=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_fmomo,bd=8,width=10,justify='left',state=DISABLED)
        self.txtfmomo.grid(row=8,column=1)

        self.sam=Checkbutton(ABC3,text='Samosa',variable=var9,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chksam).grid(row=9,sticky=W)
        self.txtsam=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_sam,bd=8,width=10,justify='left',state=DISABLED)
        self.txtsam.grid(row=9,column=1)

        self.chaw=Checkbutton(ABC3,text='Chowmin',variable=var10,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkchaw).grid(row=10,sticky=W)
        self.txtchaw=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_chaw,bd=8,width=10,justify='left',state=DISABLED)
        self.txtchaw.grid(row=10,column=1)

        self.ice=Checkbutton(ABC3,text='Ice-Cream',variable=var11,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkice).grid(row=12,sticky=W)
        self.txtice=Entry(ABC3,font=('Arial',12,'bold'),textvariable=E_ice,bd=8,width=10,justify='left',state=DISABLED)
        self.txtice.grid(row=12,column=1)

        self.chocol=Checkbutton(ABC4,text='ChocoLava',variable=var12,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkchocol).grid(row=0,sticky=W)
        self.txtchocol=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_chocol,bd=8,width=10,justify='left',state=DISABLED)
        self.txtchocol.grid(row=0,column=1)

        self.chocob=Checkbutton(ABC4,text='Choco-Brownie',variable=var13,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkchocob).grid(row=1,sticky=W)
        self.txtchocob=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_chocob,bd=8,width=10,justify='left',state=DISABLED)
        self.txtchocob.grid(row=1,column=1)

        self.t=Checkbutton(ABC4,text='Tea',variable=var14,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkt).grid(row=3,sticky=W)
        self.txtt=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_t,bd=8,width=10,justify='left',state=DISABLED)
        self.txtt.grid(row=3,column=1)

        self.cof=Checkbutton(ABC4,text='Coffee',variable=var15,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkcof).grid(row=4,sticky=W)
        self.txtcof=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_cof,bd=8,width=10,justify='left',state=DISABLED)
        self.txtcof.grid(row=4,column=1)

        self.las=Checkbutton(ABC4,text='Lassi',variable=var16,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chklas).grid(row=5,sticky=W)
        self.txtlas=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_las,bd=8,width=10,justify='left',state=DISABLED)
        self.txtlas.grid(row=5,column=1)

        self.milks=Checkbutton(ABC4,text='Milkshake',variable=var17,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkmilks).grid(row=6,sticky=W)
        self.txtmilks=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_milks,bd=8,width=10,justify='left',state=DISABLED)
        self.txtmilks.grid(row=6,column=1)

        self.manj=Checkbutton(ABC4,text='Mango-Juice',variable=var18,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkmanj).grid(row=7,sticky=W)
        self.txtmanj=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_manj,bd=8,width=10,justify='left',state=DISABLED)
        self.txtmanj.grid(row=7,column=1)

        self.aamp=Checkbutton(ABC4,text='Aampanna',variable=var19,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkaamp).grid(row=8,sticky=W)
        self.txtaamp=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_aamp,bd=8,width=10,justify='left',state=DISABLED)
        self.txtaamp.grid(row=8,column=1)

        self.coca=Checkbutton(ABC4,text='Coca-cola',variable=var20,onvalue=1,offvalue=0,font=('Arial',8,'bold'),
                                bg='white',command=chkcoca).grid(row=9,sticky=W)
        self.txtcoca=Entry(ABC4,font=('Arial',12,'bold'),textvariable=E_coca,bd=8,width=10,justify='left',state=DISABLED)
        self.txtcoca.grid(row=9,column=1)
        
         

        #---------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------
       
        #---------------------------------------------------------------------------------------------------------------------------------------------------------------



        
if __name__=='__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()



        
