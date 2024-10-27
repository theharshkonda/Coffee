from tkinter import *
from tkinter import ttk,messagebox
from PIL import *
from PIL import ImageTk,Image
import mysql.connector
import random
import time
import datetime
from pyscreenshot import grab
mycon=mysql.connector.connect(host='localhost',user="root",passwd='Harsh@2002',database="shop")
cur=mycon.cursor()
iname=[1]*100
iprice=[1]*100
iquan=[1]*100
count=0
total=0
m=0
w=0
def check():   
    ''' Check Button for Login Window '''
    global un, pwd, root
    q="select user from login"
    q1="select pass1 from login"
    cur.execute(q)
    row =cur.fetchone()
    cur.execute(q1)
    row1 =cur.fetchone()
    f=str(row[0])
    f1=str(row1[0])
    u=un.get()
    p=pwd.get()
    if f==u and f1==p:
        m=root.destroy()
        open_win()
    else:
        messagebox.showerror("Error!","Wrong Username or Password")
    cur.close()
    mycon.close()    
def again1():   
    ''' Main Login Window'''
    global un, pwd, WinStat, root, application
    root=Tk()
    root.iconbitmap('images\\icon1.ico')
    root.geometry("1300x700+0+0")
    root.title('Coffee Shop')
    root.configure(background="#fff3e6")
    img = ImageTk.PhotoImage(Image.open('IMAGES\\12.png'))
    panel = Label(root, image = img).place(x=600,y=20)
    Label(root,text='COFFEE CRUSH',background="#fff3e6",fg="red",font=("times", 45)).place(x=450,y=200)
    Label(root,text="Shop No 11,Kanna Chowk",background="#fff3e6",font=("times", 20)).place(x=510,y=300)
    Label(root,text=",Solapur-413005",background="#fff3e6",font=("times", 20)).place(x=570,y=340)
    Label(root,text='--------------------------------------------------------------------------------------------------------------------------------------------------------',background="#fff3e6",font=("times", 20)).place(x=0,y=400)
    Label(root, text='Username:',background="#fff3e6",font=("times",25)).place(x=350,y=430)
    un=Entry(root,width=20,font=("times",15))
    un.place(x=550,y=440)
    un.after(50,lambda: un.focus_force())
    Label(root, text='Password:',background="#fff3e6",font=("times",25)).place(x=350,y=500)
    pwd=Entry(root,width=20,show="*",font=("times",15))
    pwd.place(x=550,y=510)
    Button(root,width=8,text='Enter',command=check,font=("times",20),cursor='hand2').place(x=350,y=580)
    Button(root,width=8,text='Close',command=root.destroy,font=("times",20),cursor='X_cursor').place(x=720,y=580)
    #Python digital clock
    root.mainloop()
def truncate():
    q="delete from todaysorder where id!=100"
    cur.execute(q)
def open_win():
    main()
def login():
    again1()
def main():
    def remolist():
        global count,iname,iprice,iquan,total
        selected=mylist.curselection()
        if selected:
            mylist.delete(selected[0])
            b=int(selected[0])
            total=total- iprice[b]
            for i in  range(0,count):
                    iname[b]=iname[b+1]
                    iprice[b]=iprice[b+1]
                    iquan[b]=iquan[b+1]
            count=count-1
        else:
            pass
    def clearlist():
        global count,iname,iprice,iquan,total
        mylist.delete(0,END)
        iname=[1]*100
        iprice=[1]*100
        iquan=[1]*100
        total=0
    def screenshot():
        global w,id
        img = grab(bbox=(0,0,750,800)) #X,Y,X,Y
        w=id
        saveloc='IMAGES\\BILL DATA\\'+str(w)+'.png'
        img.save(saveloc)
    def cook():
            global id,count,iname,iprice,iquan,total
            l=mylist.size()
            if(l==0):
                pass
            else:
                now = datetime.datetime.now()
                qid="select id from todaysorder order by id desc limit 1"
                cur.execute(qid)
                idrow=cur.fetchone()
                #print(idrow[0])
                id=int(idrow[0]) + 1
                list_data=mylist.get(0,END)
                q=""
                tim=str(now.strftime("%H:%M:%S"))
                day = now.strftime("%d")
                for i in range(0,l):
                    q=q + '   ' + str(list_data[i]) + ','
                q1="insert into todaysorder values(%d,'%s','%s','%s')"%(id,q,tim,day)
                cur.execute(q1)
                mycon.commit()
                winbill=Tk()
                winbill.iconbitmap('images\\icon1.ico')
                winbill.geometry("600x650+0+0")
                winbill.configure(bg="#f6ff99")
                winbill.title("COFFEE CRUSH")
                l4=Label(winbill,text="DATE:",font='times 14 bold ',fg="red",bg="#f6ff99").place(x=10,y=10)
                l4=Label(winbill,text=datetime.date.today(),font='times 14 bold',bg="#f6ff99").place(x=70,y=10)
                L1=Label(winbill,text=' BILL',font='times 30 ',bg="#f6ff99",fg="red").place(x=250,y=10)
                L3=Label(winbill,text='BILL NO:',font='times 15 bold',bg="#f6ff99",fg="red").place(x=430,y=10)
                L2=Label(winbill,text=id,font='times 15 ',bg="#f6ff99").place(x=520,y=10)
                la=Label(winbill,text='-------------------------------------------------------------------------------------',background="#f6ff99",font=("times", 20)).place(x=0,y=60)
                #psize=Label(winbill,text="Item ID:",font=("Courier New",15,'bold'),fg="black",bg='#f6ff99').place(x=10,y=90)
                r1=Label(winbill,text="Item Name:",font=("Courier New",15,'bold'),fg="black",bg='#f6ff99').place(x=10,y=90)
                r12=Label(winbill,text="Quantity:",font=("Courier New",15,'bold'),fg="black",bg='#f6ff99').place(x=250,y=90)
                r12=Label(winbill,text="Item Price:",font=("Courier New",15,'bold'),fg="black",bg='#f6ff99').place(x=450,y=90)
                r3=Label(winbill,text="Total   :",font=("Courier New",20,'bold'),fg="black",bg='#f6ff99').place(x=20,y=550)
                r4=Label(winbill,text=total,font=("Courier New",20,'bold'),fg="black",bg='#f6ff99').place(x=510,y=550)
                mylist1 = Listbox(winbill,width=18,height=18,font=("Courier New",15,'bold')) 
                mylist1.place(x=10,y=120)
                mylist2 = Listbox(winbill,width=15,height=18,font=("Courier New",15,'bold'),justify='center') 
                mylist2.place(x=230,y=120)
                mylist3 = Listbox(winbill,width=15,height=18,font=("Courier New",15,'bold'),justify='center') 
                mylist3.place(x=400,y=120)
                for i in range(0,count):
                    mylist1.insert(END,str(iname[i]))
                for i in range(0,count):
                    mylist3.insert(END,str(str(iquan[i])+' X '+str(iprice[i])+' = '+str(int(iprice[i])*int(iquan[i]))))
                for i in range(0,count):
                    mylist2.insert(END,str(iquan[i]))    
                button=Button(winbill,text='PRINT',font=("Courier New",17,'bold'),fg="red",command=screenshot).place(x=240,y=600)
                iname=[1]*100
                iprice=[1]*100
                iquan=[1]*100
                count=0
                total=0
                mylist.delete(0,END)
    def todayorder():
        global count,iname,iprice,iquan,total
        def billclose():
            order.destroy()
            win.deiconify()
        win.withdraw()
        order=Tk()
        order.iconbitmap('images\\icon1.ico')
        order.title("COFFEE CRUSH")
        order.geometry("1280x700")
        f2 = Frame(order, bg="#000000", borderwidth=30, relief=GROOVE)
        f2.pack()
        L2=Label(order,text='     TODAYS ORDERS     ',font='Verdana 13')
        L2.pack(side=TOP,fill='x')
        mylist1 = Listbox(order) 
        mylist1.pack(fill = BOTH ,anchor='center',ipadx=500,ipady=300) 
        scrollbar = Scrollbar(mylist1) 
        scrollbar.pack( side = RIGHT,anchor='ne', fill = Y) 
        scrollbar.config( command = mylist1.yview)
        mylist1.config(yscrollcommand = scrollbar.set)
        q2="select * from todaysorder where id<>100"
        cur.execute(q2)
        row=cur.fetchall()
        for row in row:
            mylist1.insert(END,str(row[0]) + '   ' + str(row[1]) + '    ' + str(row[2]))
        mycon.commit()
        Button(order,text="Back To Home",command=billclose,font='Verdana 10 bold',cursor='left_side').place(x=1100,y=1)
        iname=[1]*100
        iprice=[1]*100
        iquan=[1]*100
        count=0
        total=0
        mylist.delete(0,END)
    win=Tk()
    win.geometry("1280x700")
    win.title("COFFEE CRUSH")
    win.iconbitmap('images\\icon1.ico')
    s=ttk.Style()
    s.theme_use('alt')
    # width, height
    win.maxsize(1300,800)
    #Top frame for name
    f1 = Frame(win, bg="#c78cff", borderwidth=30,relief=RIDGE)
    f1.pack(side=TOP, fill="x")
    L1=Label(f1,text='COFFEE CRUSH',font='Times 30',fg='white',bg='#c78cff')
    L1.pack(side=TOP)
    #Left frame for cart
    f2 = Frame(win, bg="#d3fffc", borderwidth=10,relief=RAISED)
    f2.pack(side='left', fill="both")
    L2=Label(f2,text='     CART     ',font='Verdana 15',bg='#709b9e')
    L2.pack(side=TOP,fill='x')
    mylist = Listbox(f2,width=40,height=20,font='Verdana 10') 
    mylist.pack(fill = BOTH ,anchor='center',ipadx=100,ipady=120) 
    scrollbar = Scrollbar(mylist) 
    scrollbar.pack( side = RIGHT,anchor='ne', fill = Y) 
    scrollbar.config( command = mylist.yview)
    mylist.config(yscrollcommand = scrollbar.set)
    cook_button=Button(f2,text='COOK',command=cook,font='Verdana 15',bg='#709b9e',cursor='top_side').pack(pady=5)
    remove_button=Button(f2,text='Remove item',font='Verdana 11',command=remolist,cursor='X_cursor').pack(side='left',anchor='nw')
    clear_button=Button(f2,text='Clear Order',font='Verdana 11',command=clearlist,cursor='exchange').pack(side='right',anchor='ne')
    today_button=Button(f2,text='Todays Order',font='Verdana 11',command=todayorder,cursor='arrow').place(x=40,y=420)
    #Tabpages
    tab_parent=ttk.Notebook(win)

    tab1=ttk.Frame(tab_parent)
    tab2=ttk.Frame(tab_parent)
    tab3=ttk.Frame(tab_parent)
    tab4=ttk.Frame(tab_parent)
    tab5=ttk.Frame(tab_parent)
    tab6=ttk.Frame(tab_parent)

    tab_parent.add(tab1,text="    Coffee     ")
    tab_parent.add(tab2,text="   Tea   ")
    tab_parent.add(tab3,text="  Milk Shake  ")
    tab_parent.add(tab4,text="  Drinks  ")
    tab_parent.add(tab5,text="  Pizza  ")
    tab_parent.add(tab6,text="  Snaks  ")
    tab_parent.pack(expand=2,ipady=40,fill='both')	 
    #For Coffee
    global text1
    i=[]
    global total,c
    price=[]
    qty=IntVar()
    #For Coffee
    def order(n,p,q):
            if q=="":
                q=1
            global iname,iprice,iquan,count,total
            pq=int(p)*int(q)
            mylist.insert(END,n+"   "+str(q)+"   "+str(pq))
            total=total+pq
            if(count<100):
                iname[count]=n
                iprice[count]=p
                iquan[count]=q
                count=count+1;
    #For cappaccino
    var = StringVar()
    f3 = Frame(tab1, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f3.grid(padx=5,pady=5,column=0,row=0)
    img=  ImageTk.PhotoImage(Image.open('images\\c1.jpg'))
    panel=Label(f3, image = img).pack(pady=0,padx=0)
    L3=Label(f3, text="1.Cappaccino  (50)", padx=14,font='Verdana 11',bg='#d8bf6e').pack()
    L4=Label(f3, text="Qty", padx=5,font='Verdana 11' ).pack(pady=20)
    qty1 = StringVar()
    q = Entry(f3, textvariable=qty1,width=5)
    q.pack(pady=5,padx=20,anchor="n")
    Button(f3,text="Buy", command=lambda:order("Cappaccino",50,qty1.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    #for Black coffee
    var = StringVar()
    f4 = Frame(tab1, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f4.grid(padx=5,pady=5,column=1,row=0)
    img1=  ImageTk.PhotoImage(Image.open('images\\c4.png'))
    panel=Label(f4, image = img1).pack(pady=0,padx=0)
    L4=Label(f4, text="2.Black Coffee ", padx=14, font='Verdana 11',bg='#d8bf6e').pack()
    L5=Label(f4, text="Qty", padx=5, font='Verdana 11' ).pack(pady=20)
    qty2=StringVar()
    q1 = Entry(f4, textvariable=qty2,width=5)
    q1.pack(pady=5,padx=20,anchor="n")
    Button(f4,text="Buy", command=lambda:order("Black Coffee",40,qty2.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Americano coffee
    var = StringVar()
    f5 = Frame(tab1, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f5.grid(padx=5,pady=5,column=3,row=0)
    img2=  ImageTk.PhotoImage(Image.open('images\\c3.jpg'))
    panel=Label(f5, image = img2).pack(pady=0,padx=0) 
    L6=Label(f5, text="3.Americano ", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L7=Label(f5, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty3=StringVar()
    q2 = Entry(f5, textvariable=qty3,width=5)
    q2.pack(pady=5,padx=20,anchor="n")
    Button(f5,text="Buy", command=lambda:order("Americano",70,qty3.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Special coffee
    var = StringVar()
    f6 = Frame(tab1, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f6.grid(padx=5,pady=5,column=4,row=0)
    img3=  ImageTk.PhotoImage(Image.open('images\\c2.png'))
    panel=Label(f6, image = img3).pack(pady=0,padx=0)
    L8=Label(f6, text="4.Special Coffee ", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L9=Label(f6, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty4=StringVar()
    q3 = Entry(f6, textvariable=qty4,width=5)
    q3.pack(pady=5,padx=20,anchor="n")
    Button(f6,text="Buy", command=lambda:order("Special coffee",100,qty4.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)


    #for Tea

   


    #For Normal Tea
    var = StringVar()
    f = Frame(tab2, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f.grid(padx=5,pady=5,column=0,row=0)
    img4=  ImageTk.PhotoImage(Image.open('images\\t1.png'))
    panel=Label(f, image = img4).pack(pady=0,padx=0)
    L=Label(f, text="1.Normal Tea", padx=14,font='Verdana 11',bg='#d8bf6e' ).pack()
    L=Label(f, text="Qty", padx=5,font='Verdana 11' ).pack(pady=20)
    qty5 = StringVar()
    q = Entry(f, textvariable=qty5,width=5)
    q.pack(pady=5,padx=20,anchor="n")
    Button(f,text="Buy", command=lambda:order("Normal Tea",20,qty5.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    #for Lemon Tea
    var = StringVar()
    f8 = Frame(tab2, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f8.grid(padx=5,pady=5,column=1,row=0)
    img5=  ImageTk.PhotoImage(Image.open('images\\t2.png'))
    panel=Label(f8, image = img5).pack(pady=0,padx=0)
    L11=Label(f8, text="2.Lemon Tea ", padx=14, font='Verdana 11',bg='#d8bf6e' ).pack()
    L12=Label(f8, text="Qty", padx=5,font='Verdana 11' ).pack(pady=20)
    qty6=StringVar()
    q1 = Entry(f8, textvariable=qty6,width=5)
    q1.pack(pady=5,padx=20,anchor="n")
    Button(f8,text="Buy", command=lambda:order("Lemon Tea",50,qty6.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Green Tea
    var = StringVar()
    f9 = Frame(tab2, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f9.grid(padx=5,pady=5,column=3,row=0)
    img6=  ImageTk.PhotoImage(Image.open('images\\t3.png'))
    panel=Label(f9, image = img6).pack(pady=0,padx=0)
    L13=Label(f9, text="3.Green Tea ", padx=14, font='Verdana 11',bg='#d8bf6e' ).pack()
    L14=Label(f9, text="Qty", padx=5, font='Verdana 11' ).pack(pady=20)
    qty7=StringVar()
    q2 = Entry(f9, textvariable=qty7,width=5)
    q2.pack(pady=5,padx=20,anchor="n")
    Button(f9,text="Buy", command=lambda:order("Green Tea",50,qty7.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Black Tea
    var = StringVar()
    f10 = Frame(tab2, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f10.grid(padx=5,pady=5,column=4,row=0)
    img7=  ImageTk.PhotoImage(Image.open('images\\t4.png'))
    panel=Label(f10, image = img7).pack(pady=0,padx=0)
    L15=Label(f10, text="4.Black Tea ", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L16=Label(f10, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty8=StringVar()
    q3 = Entry(f10, textvariable=qty8,width=5)
    q3.pack(pady=5,padx=20,anchor="n")
    Button(f10,text="Buy", command=lambda:order("Black Tea",30,qty8.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    #for MilkShake
    #For Chocolate Milkshake
    var = StringVar()
    f = Frame(tab3, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f.grid(padx=5,pady=5,column=0,row=0)
    img8=  ImageTk.PhotoImage(Image.open('images\\m1.png'))
    panel=Label(f, image = img8).pack(pady=0,padx=0)
    L=Label(f, text="1.Chocolate", padx=14,font='Verdana 11',bg='#d8bf6e' ).pack()
    L=Label(f, text="Milkshake", padx=14,font='Verdana 11' ,bg='#d8bf6e').pack()
    L=Label(f, text="Qty", padx=5,font='Verdana 11' ).pack(pady=20)
    qty9 = StringVar()
    q = Entry(f, textvariable=qty9,width=5)
    q.pack(pady=5,padx=5,anchor="n")
    Button(f,text="Buy", command=lambda:order("Chocolate Milkshake",90,qty9.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    #for Badam Milkshake
    var = StringVar()
    f8 = Frame(tab3, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f8.grid(padx=5,pady=5,column=1,row=0)
    img9=  ImageTk.PhotoImage(Image.open('images\\m2.png'))
    panel=Label(f8, image = img9).pack(pady=0,padx=0)
    L11=Label(f8, text="2.Badam  ", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L11=Label(f8, text="MilkShake", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L12=Label(f8, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty10=StringVar()
    q1 = Entry(f8, textvariable=qty10,width=5)
    q1.pack(pady=5,padx=20,anchor="n")
    Button(f8,text="Buy", command=lambda:order("Badam MilkShake",150,qty10.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for ButterScotch
    var = StringVar()
    f9 = Frame(tab3, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f9.grid(padx=5,pady=5,column=3,row=0)
    img10=  ImageTk.PhotoImage(Image.open('images\\m3.png'))
    panel=Label(f9, image = img10).pack(pady=0,padx=0)
    L13=Label(f9, text="3.ButterScotch ", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L13=Label(f9, text="MilkShake ", padx=14, font='Verdana 11',bg='#d8bf6e' ).pack()
    L14=Label(f9, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty11=StringVar()
    q2 = Entry(f9, textvariable=qty11,width=5)
    q2.pack(pady=5,padx=20,anchor="n")
    Button(f9,text="Buy", command=lambda:order("ButterScotch MilkShake",100,qty11.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Mango
    var = StringVar()
    f10 = Frame(tab3, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f10.grid(padx=5,pady=5,column=4,row=0)
    img11=  ImageTk.PhotoImage(Image.open('images\\m4.png'))
    panel=Label(f10, image = img11).pack(pady=0,padx=0)
    L15=Label(f10, text="4.Mango MilkShake", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L16=Label(f10, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty12=StringVar()
    q3 = Entry(f10, textvariable=qty12,width=5)
    q3.pack(pady=5,padx=20,anchor="n")
    Button(f10,text="Buy", command=lambda:order("Mango MilkShake",80,qty12.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
        

    #for Drinks
    
 

    #For Pepsi
    var = StringVar()
    f = Frame(tab4, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f.grid(padx=5,pady=5,column=0,row=0)
    img12=  ImageTk.PhotoImage(Image.open('images\\d1.jpg'))
    panel=Label(f, image = img12).pack(pady=0,padx=0)
    L=Label(f, text="1.Pepsi", padx=14,font='Verdana 11' ,bg='#d8bf6e').pack()
    L=Label(f, text="Qty", padx=5,font='Verdana 11' ).pack(pady=20)
    qty13 = StringVar()
    q = Entry(f, textvariable=qty13,width=5)
    q.pack(pady=5,padx=20,anchor="n")
    Button(f,text="Buy", command=lambda:order("Pepsi",70,qty13.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    #for Cocacola
    var = StringVar()
    f8 = Frame(tab4, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f8.grid(padx=5,pady=5,column=1,row=0)
    img13=  ImageTk.PhotoImage(Image.open('images\\d2.png'))
    panel=Label(f8, image = img13).pack(pady=0,padx=0)
    L11=Label(f8, text="2.Cocacola ", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L12=Label(f8, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty14=StringVar()
    q1 = Entry(f8, textvariable=qty14,width=5)
    q1.pack(pady=5,padx=20,anchor="n")
    Button(f8,text="Buy", command=lambda:order("Cocacola",65,qty14.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Fanta
    var = StringVar()
    f9 = Frame(tab4, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f9.grid(padx=5,pady=5,column=3,row=0)
    img14=  ImageTk.PhotoImage(Image.open('images\\d3.png'))
    panel=Label(f9, image = img14).pack(pady=0,padx=0)
    L13=Label(f9, text="3.Fanta", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L14=Label(f9, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty15=StringVar()
    q2 = Entry(f9, textvariable=qty15,width=5)
    q2.pack(pady=5,padx=20,anchor="n")
    Button(f9,text="Buy", command=lambda:order("Fanta",60,qty15.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Sprite
    var = StringVar()
    f10 = Frame(tab4, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f10.grid(padx=5,pady=5,column=4,row=0)
    img15=  ImageTk.PhotoImage(Image.open('images\\d4.png'))
    panel=Label(f10, image = img15).pack(pady=0,padx=0)
    L15=Label(f10, text="4.Sprite", padx=14, font='Verdana 11',bg='#d8bf6e').pack()
    L16=Label(f10, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty16=StringVar()
    q3 = Entry(f10, textvariable=qty16,width=5)
    q1.pack(pady=5,padx=20,anchor="n")
    Button(f10,text="Buy", command=lambda:order("Sprite",50,qty16.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Pizza

    


    #For Non-Mix Pizza
    var = StringVar()
    f = Frame(tab5, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f.grid(padx=5,pady=5,column=0,row=0)
    img16=  ImageTk.PhotoImage(Image.open('images\\p1.jpg'))
    panel=Label(f, image = img16).pack(pady=0,padx=0)
    L=Label(f, text="1.Non-Mix Pizza", padx=14, font='Verdana 11',bg='#d8bf6e').pack()
    L=Label(f, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty17 = StringVar()
    q = Entry(f, textvariable=qty17,width=5)
    q.pack(pady=5,padx=20,anchor="n")
    Button(f,text="Buy", command=lambda:order("Non-Mix Pizza",100,qty17.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    #for Cheese Pizza
    var = StringVar()
    f8 = Frame(tab5, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f8.grid(padx=5,pady=5,column=1,row=0)
    img17=  ImageTk.PhotoImage(Image.open('images\\p2.gif'))
    panel=Label(f8, image = img17).pack(pady=0,padx=0)
    L11=Label(f8, text="2.Cheese Pizza", padx=14, font='Verdana 11',bg='#d8bf6e' ).pack()
    L12=Label(f8, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty18=StringVar()
    q1 = Entry(f8, textvariable=qty18,width=5)
    q1.pack(pady=5,padx=20,anchor="n")
    Button(f8,text="Buy", command=lambda:order("Cheese Pizza",130,qty18.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for  Pepper Barbique Pizza
    var = StringVar()
    f9 = Frame(tab5, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f9.grid(padx=5,pady=5,column=3,row=0)
    img18=  ImageTk.PhotoImage(Image.open('images\\p3.jpg'))
    panel=Label(f9, image = img18).pack(pady=0,padx=0)
    L13=Label(f9, text="3.Barbique  ", padx=14, font='Verdana 11',bg='#d8bf6e').pack()
    L13=Label(f9, text="Pizza ", padx=20, font='Verdana 11' ,bg='#d8bf6e').pack()
    L14=Label(f9, text="Qty", padx=5, font='Verdana 11' ).pack(pady=20)
    qty19=StringVar()
    q2 = Entry(f9, textvariable=qty19,width=5)
    q2.pack(pady=5,padx=20,anchor="n")
    Button(f9,text="Buy", command=lambda:order("Barbique Pizza",200,qty19.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Hawaian Pizza
    var = StringVar()
    f10 = Frame(tab5, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f10.grid(padx=5,pady=5,column=4,row=0)
    img19=  ImageTk.PhotoImage(Image.open('images\\p4.jpg'))
    panel=Label(f10, image = img19).pack(pady=0,padx=0)
    L15=Label(f10, text="4.Hawaian Pizza", padx=14, font='Verdana 11',bg='#d8bf6e' ).pack()
    L16=Label(f10, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty20=StringVar()
    q3 = Entry(f10, textvariable=qty20,width=5)
    q3.pack(pady=5,padx=20,anchor="n")
    Button(f10,text="Buy", command=lambda:order("Hawaian Pizza",150,qty20.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)


    #for Snacks



    #For Idli Snacks
    var = StringVar()
    f = Frame(tab6, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f.grid(padx=5,pady=5,column=0,row=0)
    img20=  ImageTk.PhotoImage(Image.open('images\\s1.jpg'))
    panel=Label(f, image = img20).pack(pady=0,padx=0)
    L=Label(f, text="1.Idli Wada", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L=Label(f, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty21 = StringVar()
    q = Entry(f, textvariable=qty21,width=5)
    q.pack(pady=5,padx=20,anchor="n")
    Button(f,text="Buy", command=lambda:order("Idli Wada",50,qty21.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    #for Dosa 
    var = StringVar()
    f8 = Frame(tab6, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f8.grid(padx=5,pady=5,column=1,row=0)
    img21=  ImageTk.PhotoImage(Image.open('images\\s2.png'))
    panel=Label(f8, image = img21).pack(pady=0,padx=0)
    L11=Label(f8, text="2.Dosa ", padx=14, font='Verdana 11',bg='#d8bf6e').pack()
    L12=Label(f8, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty22=StringVar()
    q1 = Entry(f8, textvariable=qty22,width=5)
    q1.pack(pady=5,padx=20,anchor="n")
    Button(f8,text="Buy", command=lambda:order("Dosa",70,qty22.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for  Samosa
    var = StringVar()
    f9 = Frame(tab6, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f9.grid(padx=5,pady=5,column=3,row=0)
    img22=  ImageTk.PhotoImage(Image.open('images\\s3.jpg'))
    panel=Label(f9, image = img22).pack(pady=0,padx=0)
    L13=Label(f9, text="3.Samosa  ", padx=14, font='Verdana 11',bg='#d8bf6e' ).pack()
    L14=Label(f9, text="Qty", padx=5 , font='Verdana 11').pack(pady=20)
    qty23=StringVar()
    q2 = Entry(f9, textvariable=qty23,width=5)
    q2.pack(pady=5,padx=20,anchor="n")
    Button(f9,text="Buy", command=lambda:order("Samosa",100,qty23.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)

    #for Puri Bhaji
    var = StringVar()
    f10 = Frame(tab6, bg="#d8bf6e", borderwidth=30 , relief=GROOVE)
    f10.grid(padx=5,pady=5,column=4,row=0)
    img23=  ImageTk.PhotoImage(Image.open('images\\s4.jpg'))
    panel=Label(f10, image = img23).pack(pady=0,padx=0)
    L15=Label(f10, text="4.Puri Bhaji", padx=14, font='Verdana 11' ,bg='#d8bf6e').pack()
    L16=Label(f10, text="Qty", padx=5, font='Verdana 11' ).pack(pady=20)
    qty24=StringVar()
    q3 = Entry(f10, textvariable=qty24,width=5)
    q3.pack(pady=5,padx=20,anchor="n")
    b1=Button(f10,text="Buy", command=lambda:order("Puri Bhaji",50,qty24.get()),width=10,cursor='plus', relief=GROOVE).pack(pady=20)
    win.mainloop()

    
qday=""
now1 = datetime.datetime.now()
curday=str(now1.strftime("%d"))
qdef="update todaysorder set day=%s where id=100"%(curday)
cur.execute(qdef)
mycon.commit();
qday="select day from todaysorder order by id desc limit 1"
cur.execute(qday)
dayrow=cur.fetchone()
if(int(dayrow[0])<int(now1.strftime("%d"))):
    truncate()
login()
#main()
cur.close()
mycon.close()
