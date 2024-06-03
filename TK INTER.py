import mysql.connector as ms

mydb = ms.connect(host='localhost', user='root', passwd='1211', database='smart_society')
point = mydb.cursor(buffered=True)
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
def table_print(heading,data,main_frame,canvas,scrolframe,table_frame):     #show tables on frame

    main_frame.pack(fill=BOTH, expand=True)
    scrolframe = Frame(main_frame)
    scrolframe.pack(fill=X, side=BOTTOM)
    canvas = Canvas(main_frame, bg='spring green2')
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    x_scrollbar = ttk.Scrollbar(scrolframe, orient=HORIZONTAL, command=canvas.xview)
    x_scrollbar.pack(side=BOTTOM, fill=X)
    y_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    y_scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(xscrollcommand=x_scrollbar.set)
    canvas.configure(yscrollcommand=y_scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.config(scrollregion=canvas.bbox(ALL)))
    table_frame = Frame(canvas, bg='yellow')
    canvas.create_window((0, 0), window=table_frame, anchor="nw")
    col_no1=0
    for row in heading:
        for col in row:
            col_no1 += 1
            str1 = col
            label8 = Label(table_frame, text=str(str1), borderwidth=1, relief='solid', width=43, height=5,bg='spring green2')
            label8.grid(row=0, column=col_no1)
            table_frame.grid_rowconfigure(1,)
            table_frame.grid_columnconfigure(col_no1)
    col_no2 = 0
    row_no = 0
    for row in data:
        row_no += 1
        col_no2 = 0
        for col in row:
            col_no2 += 1
            str2 = col
            label9 = Label(table_frame, text=str(str2), borderwidth=1, relief='solid', width=43, height=3,
                       bg='sea green1')
            label9.grid(row=row_no, column=col_no2)

            table_frame.grid_rowconfigure(row_no, weight=100)
            table_frame.grid_columnconfigure(col_no2, weight=2)
def login_info(user1=1):                        #edit login info
    frame14 = Frame(root, bg='spring green2')
    frame31 = Frame(root, bg='spring green2')
    frame2.pack_forget()
    frame14.pack(fill='both')
    label12 = Label(frame14, text='USERNAME', font='calibri 16 bold', bg='spring green2', width=20)
    label12.pack()
    entry_box6 = Entry(frame14)
    entry_box6.pack()
    if user1 != 1:


        for i in frame14.winfo_children():
            i.forget()
        for i in frame31.winfo_children():
            i.forget()
        frame14.forget(),frame31.forget()
        frame15.pack(fill='both'),frame32.pack()
    def command8():

        user = str(entry_box6.get())
        user = user.upper()
        query1 = "select* from login_info where user='{}'".format(user)
        point.execute(query1)
        fetch_1 = point.fetchone()

        if type(fetch_1) != tuple:
            frame15.pack(fill='both')

            if user1 == 1:
                frame31.pack(fill='both')
                global label13
                label13 = Label(frame31, text='''1:    CUSTOMER
    2:   SHOP OWNER''', font='calibri 16 bold', bg='spring green2', width=20)
                label13.pack()
                global entry_box7

                entry_box7 = Entry(frame31)
                entry_box7.pack()
            frame32.pack(fill='both',expand=True)

    button15 = Button(frame14, text='CHECK', command=command8)
    button15.pack()


    label14 = Label(frame15, text='NAME', font='calibri 16 bold', bg='spring green2', width=20)
    label14.pack()
    entry_box8 = Entry(frame15)
    entry_box8.pack()
    label15 = Label(frame15, text='ADRESS', font='calibri 16 bold', bg='spring green2', width=20)
    label15.pack()
    entry_box9 = Entry(frame15)
    entry_box9.pack()
    label23 = Label(frame15, text='MOBILE NUMBER', font='calibri 16 bold', bg='spring green2', width=20)
    label23.pack()
    entry_box10 = Entry(frame15)
    entry_box10.pack()
    label24 = Label(frame15, text='PASSWORD', font='calibri 16 bold', bg='spring green2', width=20)
    label24.pack()
    entry_box11 = Entry(frame15)
    entry_box11.pack()

    def command9():
        user = str(entry_box6.get())
        user=user.upper()

        if user1==1:
            type_1 = int(entry_box7.get())
            if type_1 == 1:
                type_2 = 'CUSTOMER'
            elif type_1 == 2:
                type_2 = 'SHOP OWNER'

        name = str(entry_box8.get())
        name = name.upper()

        house = str(entry_box9.get())

        mobile_no = str(entry_box10.get())

        password = str(entry_box11.get())
        if user1==1:
            query2 = "insert into login_info values('{}','{}','{}','{}','{}','{}')" \
            .format(house, name, user, password, type_2, mobile_no)
            point.execute(query2)
            mydb.commit()
            frame2.pack()



        frame14.pack_forget(),frame31.pack_forget(),frame32.pack_forget()
        frame15.pack_forget()

        for i in frame14.winfo_children():
            i.pack_forget()
        for i in frame23.winfo_children():
            i.pack_forget()
        for i in frame15.winfo_children():
            i.pack_forget()
        for i in frame31.winfo_children():
            i.pack_forget()
        for i in frame32.winfo_children():
            i.pack_forget()

    button16 = Button(frame32, text='SUBMIT', command=command9)
    button16.pack()
def delete(user,shop_owner=1):              #delete account

    point.execute("select name from login_info where user='{}'".format(user))
    fetch_10 = point.fetchone()
    name2 = fetch_10[0]
    point.execute("delete from login_info where user='{}'".format(user))
    point.execute("delete from orders where customer='{}'".format(name2))
    if shop_owner!=1:
        point.execute("delete from stock_list where shop_name='{}'".format(name2))
        point.execute("delete from orders where shop_name='{}'".format(name2))
    mydb.commit()


def user_frame_forget():            #function to forget frames and its children widget
    for i in main_frame4.winfo_children():
        i.pack_forget()
    for i in main_frame2.winfo_children():
        i.pack_forget()
    frame4.pack_forget(), main_frame2.pack_forget()
    for i in frame4.winfo_children():
        i.pack_forget()
    frame8.pack_forget()
    for i in frame8.winfo_children():
        i.pack_forget()
    for i in main_frame3.winfo_children():
        i.pack_forget()
    frame5.pack_forget()
    main_frame12.pack_forget(), frame33.pack_forget()
    for i in frame33.winfo_children():
        i.pack_forget()
    for i in main_frame12.winfo_children():
        i.pack_forget()
    frame13.pack_forget(), main_frame5.pack_forget()
    for i in frame13.winfo_children():
        i.pack_forget()
    frame30.pack_forget()
    for i in frame30.winfo_children():
        i.pack_forget()
    main_frame5.pack_forget()
    for i in main_frame5.winfo_children():
        i.pack_forget()
    main_frame7.pack_forget()
    for i in main_frame7.winfo_children():
        i.pack_forget()
    main_frame3.pack_forget()
    for i in main_frame14.winfo_children():
        i.pack_forget()
    main_frame14.pack_forget()

root = Tk()
root.configure(background='spring green2')
root.geometry("700x450")

root.minsize(width=800, height=700)

root.title(" SOCIETY STORE ")

photo = ImageTk.PhotoImage(Image.open(r"F:\SMART SOCIETY\logo.png"))


main_frame1 = Frame(root)
main_frame2 = Frame(root)
main_frame3 = Frame(root)
main_frame4 = Frame(root)
main_frame5 = Frame(root)
main_frame6 = Frame(root)
main_frame7 = Frame(root)
main_frame8 = Frame(root)
main_frame9 = Frame(root)
main_frame10 = Frame(root)
main_frame11 = Frame(root)
main_frame12 = Frame(root)
main_frame14 = Frame(root)

frame1 = Frame(root, bg='spring green2')
frame2 = Frame(root, bg='spring green2')
frame3 = Frame(root, bg='spring green2')
frame4 = Frame(root, bg='spring green2')
frame5 = Frame(root, bg='spring green2')
frame6 = Frame(root, bg='spring green2')
frame7 = Frame(root, bg='spring green2')
frame8 = Frame(root, bg='spring green2')
frame10 = Frame(root, bg='spring green2')
frame11 = Frame(root, bg='spring green2')
frame12 = Frame(root, bg='spring green2')
frame13 = Frame(root, bg='spring green2')
frame15 = Frame(root, bg='spring green2')
frame16 = Frame(root, bg='spring green2')                   #ALL THE FRAMES USED ARE CREATED HERE
frame17 = Frame(root, bg='spring green2')
frame18 = Frame(root, bg='spring green2')
frame19 = Frame(root, bg='spring green2')
frame20 = Frame(root, bg='spring green2')
frame21 = Frame(root, bg='spring green2')
frame22 = Frame(root, bg='spring green2')
frame23 = Frame(root, bg='spring green2')
frame24 = Frame(root, bg='spring green2')
frame25 = Frame(root, bg='spring green2')
frame26 = Frame(root, bg='spring green2')
frame27 = Frame(root, bg='spring green2')
frame28 = Frame(root, bg='spring green2')
frame29 = Frame(root, bg='spring green2')
frame30 = Frame(root, bg='spring green2')
frame32 = Frame(root, bg='spring green2')
frame33 = Frame(root, bg='spring green2')
frame34 = Frame(root, bg='spring green2')
frame35 = Frame(root, bg='spring green2')
frame36 = Frame(root, bg='spring green2')
frame37 = Frame(root, bg='spring green2')
frame38 = Frame(root, bg='spring green2')
frame39 = Frame(root, bg='spring green2')
frame40 = Frame(root, bg='spring green2')
frame1.pack(side=TOP, fill='both', expand=True)

p3 = ImageTk.PhotoImage(Image.open(r"F:\SMART SOCIETY\button (2).png"))
p4 = ImageTk.PhotoImage(Image.open(r"F:\SMART SOCIETY\button (3).png"))
p5 = ImageTk.PhotoImage(Image.open(r"F:\SMART SOCIETY\button (5).png"))


def command1():                        #front to options

    frame1.pack_forget()
    frame2.pack(side=TOP, fill='both', expand=True)

    def command2():                   #option to login

        frame2.pack_forget()
        frame3.pack(side=TOP, fill='both', expand=True)
        label4 = Label(frame3, text='Enter your username: ', width=20, height=3, font='calibri 15 bold', bg='spring green2')
        label5 = Label(frame3, text='Enter your password', width=20, height=3, font='calibri 15 bold', bg='spring green2')
        label4.pack(side=TOP)
        entry_box1 = Entry(frame3, width=20,font=16)
        entry_box1.pack(side=TOP)
        label5.pack(side=TOP)
        entry_box2 = Entry(frame3, width=20,font=16)
        entry_box2.pack(side=TOP)

        def command3():         #login to orders

            frame3.pack_forget()
            for i in frame3.winfo_children():
                i.pack_forget()
            user = entry_box1.get()
            user = user.upper()
            query3 = "select* from login_info where user='{}'".format(user)
            point.execute(query3)
            fetch_2 = point.fetchone()
            password = entry_box2.get()
            if fetch_2==None:
                messagebox.showinfo(" NOTIFICATION ", "WRONG ID OR PASSWORD ")
                root.destroy()


            elif fetch_2[2]==user and password==fetch_2[3]:
                type_2 = fetch_2[4]
                if type_2=='CUSTOMER':
                    label3.pack_forget()
                    label6 = Label(frame4, text='WELCOME BACK DEAR CUSTOMER',font='calibri 16 bold', bg='spring green2')
                    label6.pack(side=TOP)
                    query4 = "select * from orders where customer='{}' ".format(user)
                    point.execute(query4)
                    fetch_3 = point.fetchall()
                    if len(fetch_3) == 0:
                        label7 = Label(frame4,text='OOPS!  NO orders FOUND',font='calibri 26 bold', bg='spring green2')
                        label7.pack(pady=5)
                    else:
                        query4 = "select * from orders where customer='{}' ".format(user)
                        point.execute(query4)
                        fetch_4 = point.fetchall()
                        scrolframe2 ='scrolframe2'
                        my_canvas2 ='my_canvas2'
                        table = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                    'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO','STATUS')]
                        table_print(table,fetch_4,main_frame2,scrolframe2,my_canvas2,frame4,)
                    frame4.pack(side=TOP, fill='both', expand=True)
                    frame5.pack(side=TOP, fill='both', expand=True,pady=5)


                    def command4():               #want to order

                        user_frame_forget()
                        scrolframe1 = 'scrolframe1'
                        my_canvas1 = 'my_canvas1'
                        table2 = [('SLNO   ', 'PRODUCTS     ', ' PRICE   ', ' QUANTITY ', ' SHOP_NAME')]
                        point.execute('select * from stock_list')
                        fetch_32 = point.fetchall()
                        label10 = Label(frame7, text='SLNO.')
                        label10.pack()
                        entry_box4 = Entry(frame7)
                        entry_box4.pack()
                        label11 = Label(frame7, text='QUANTITY')
                        label11.pack()
                        entry_box5 = Entry(frame7)
                        entry_box5.pack()
                        table_print(table2,fetch_32,main_frame1,my_canvas1,scrolframe1,frame6)
                        frame7.pack(side=BOTTOM)

                        def command5():           #back to orders

                            main_frame2.pack_forget()

                            quantity = int(entry_box5.get())
                            ord_no = int(entry_box4.get())
                            point.execute("select shop_name from stock_list where slno={}".format(ord_no))
                            fetch_5 = point.fetchone()
                            str1 = fetch_5[0]
                            point.execute("select products from stock_list where slno={}".format(ord_no))
                            fetch_6 = point.fetchone()
                            str2 = fetch_6[0]
                            point.execute("select price from stock_list where slno={}".format(ord_no))
                            fetch_7 = str(point.fetchone())
                            str3 = ""
                            for i in fetch_7:
                                if i in "(Decimal'),":
                                    pass
                                else:
                                    str3 += i
                            str3 = float(str3)
                            total_price = str3 * int(quantity)
                            point.execute("select mobile_no from login_info where user='{}'".format(user))
                            fetch_8 = point.fetchone()
                            contact_no = fetch_8[0]
                            point.execute("select mobile_no from login_info where name='{}'".format(str1))
                            fetch_9 = point.fetchone()

                            shop_cont = fetch_9[0]
                            point.execute("select max(order_id) from orders ")
                            fetch_15 = point.fetchone()
                            fetch_16 = fetch_15[0]
                            print(fetch_15,fetch_16,type(fetch_16))
                            if fetch_16 == None:
                                order_id = 1
                            else:
                                order_id = int(fetch_16) + 1
                            md5 = "insert into orders (order_id,customer,shop_name,product,quantity,price,total," \
                                  "customer_no,shop_contact_no,status)" \
                                  " values({},'{}','{}','{}','{}',{},{},'{}','{}','PENDING')".format \
                                (order_id, user, str1, str2, quantity, str3, total_price, contact_no, shop_cont)
                            point.execute(md5)
                            mydb.commit()
                            md6 = "update stock_list set quantity=quantity-{} where products='{}'". \
                                format(quantity, str2)
                            point.execute(md6)
                            mydb.commit()
                            messagebox.showinfo(" ORDER CONFIRMATION ", " YOUR ORDER HAS BEEN PLACED ")
                            main_frame1.pack_forget()
                            for i in main_frame1.winfo_children():
                                i.pack_forget()
                            frame8.pack(),frame7.pack_forget()
                            for i in frame7.winfo_children():
                                i.pack_forget()
                            query4 = "select * from orders where customer='{}' ".format(user)
                            point.execute(query4)
                            fetch_22 = point.fetchall()
                            scrolframe3 = 'scrolframe3'
                            my_canvas3 = 'my_canvas3'
                            table3 = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                       'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                            table_print(table3,fetch_22,main_frame3,my_canvas3,scrolframe3, frame8, )
                            main_frame3,frame7.pack_forget()
                            frame5.pack( fill='both', expand=True,pady=5)
                            main_frame2.pack_forget()
                        button6=Button(frame7,command=command5,text='SUBMIT',font='calibri 16 bold')
                        button6.pack(side=BOTTOM,pady=30)


                    def command6():               #cancel orders

                        user_frame_forget()
                        frame11.pack(fill='both')
                        query4 = "select * from orders where customer='{}' ".format(user)
                        point.execute(query4)
                        fetch_23 = point.fetchall()
                        scrolframe4 = 'scrolframe4'
                        my_canvas4 = 'my_canvas4'
                        table = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                  'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                        table_print(table, fetch_23,main_frame4,my_canvas4,scrolframe4, frame11,)
                        frame12.pack(fill='both', expand=True,pady=5)
                        label22=Label(frame12,text='ORDER ID OF ORDER TO BE CANCELED')
                        label22.pack()
                        entry_box3 = Entry(frame12)
                        entry_box3.pack(side=TOP)

                        def command7():         #cancel orders to orders

                            main_frame4.pack_forget()
                            sln3 = int(entry_box3.get())
                            point.execute('select quantity from orders where order_id={}'.format(sln3))
                            fetch_17 = point.fetchone()
                            fetch_18 = fetch_17[0]
                            point.execute('select product from orders where order_id={}'.format(sln3))
                            fetch_19 = point.fetchone()
                            fetch_20 = fetch_19[0]
                            point.execute(
                                "update stock_list set quantity=quantity+{} where products='{}'".format(fetch_18,
                                                                                                        fetch_20))
                            mydb.commit()
                            point.execute("update orders set status='CANCELLED'where order_id={}".format(sln3))
                            mydb.commit()
                            messagebox.showinfo(" ORDER CANCELATION ", " YOUR ORDER HAS BEEN CANCELLED ")
                            query4 = "select * from orders where customer='{}' ".format(user)
                            point.execute(query4)
                            fetch_24 = point.fetchall()

                            table5 = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                      'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                            frame13.pack(fill='both')
                            scrolframe5 = 'scrolframe5'
                            my_canvas5 = 'my_canvas5'
                            table_print(table5, fetch_24,main_frame5,my_canvas5,scrolframe5, frame13,)
                            frame5.pack( fill='both', expand=True,pady=5)
                            frame11.pack_forget(),frame12.pack_forget()
                            for i in frame11.winfo_children():
                                i.pack_forget()
                            for i in frame12.winfo_children():
                                i.pack_forget()
                                main_frame4.pack_forget()
                            for i in main_frame4.winfo_children():
                                i.pack_forget()

                        button14=Button(frame12,text='SUBMIT',command=command7,font='calibri 16 bold', bg='spring green2')
                        button14.pack(side=TOP)

                    def command10():            #edit login info

                        user_frame_forget()
                        frame34.pack(fill='both')
                        frame35.pack(fill='both')
                        label12 = Label(frame34, text='USERNAME', font='calibri 16 bold', bg='spring green2', width=20)
                        label12.pack()
                        entry_box6 = Entry(frame34)
                        entry_box6.pack()
                        for i in frame34.winfo_children():
                             i.forget()
                        for i in frame35.winfo_children():
                            i.forget()
                        frame34.forget(), frame35.forget()
                        frame36.pack(fill='both'), frame40.pack()

                        def command8():

                            frame36.pack(fill='both')
                            frame40.pack(fill='both', expand=True)
                        button15 = Button(frame34, text='CHECK', command=command8)
                        button15.pack()
                        label14 = Label(frame36, text='NAME', font='calibri 16 bold', bg='spring green2', width=20)
                        label14.pack()
                        entry_box8 = Entry(frame36)
                        entry_box8.pack()
                        label15 = Label(frame36, text='ADRESS', font='calibri 16 bold', bg='spring green2', width=20)
                        label15.pack()
                        entry_box9 = Entry(frame36)
                        entry_box9.pack()
                        label23 = Label(frame36, text='MOBILE NUMBER', font='calibri 16 bold', bg='spring green2',
                                        width=20)
                        label23.pack()
                        entry_box10 = Entry(frame36)
                        entry_box10.pack()
                        label24 = Label(frame36, text='PASSWORD', font='calibri 16 bold', bg='spring green2', width=20)
                        label24.pack()
                        entry_box11 = Entry(frame36)
                        entry_box11.pack()

                        def command9():

                            name = str(entry_box8.get())
                            name = name.upper()
                            house = str(entry_box9.get())
                            mobile_no = str(entry_box10.get())
                            password = str(entry_box11.get())

                            point.execute("update orders set customer_no='{}' where customer='{}'".format(
                                 mobile_no, user))
                            point.execute(
                                "update login_info set name='{}',password='{}',adress='{}',mobile_no='{}' where user='{}'"
                                    .format(name, password, house,  mobile_no, user))
                            mydb.commit()
                            frame38.pack(fill=BOTH)
                            frame34.pack_forget(), frame35.pack_forget(), frame40.pack_forget()
                            frame36.pack_forget()
                            for i in frame34.winfo_children():
                                i.pack_forget()
                            for i in frame23.winfo_children():
                                i.pack_forget()
                            for i in frame36.winfo_children():
                                i.pack_forget()
                            for i in frame35.winfo_children():
                                i.pack_forget()
                            for i in frame40.winfo_children():
                                i.pack_forget()
                            query4 = "select * from orders where customer='{}' ".format(user)
                            point.execute(query4)
                            fetch_100 = point.fetchall()
                            table11 = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                      'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                            frame13.pack(fill='both')
                            scrolframe14 = 'scrolframe14'
                            my_canvas14 = 'my_canvas14'
                            table_print(table11, fetch_100,main_frame14,my_canvas14,scrolframe14, frame38)

                            frame5.pack( fill='both', expand=True,pady=5)

                        button16 = Button(frame40, text='SUBMIT', command=command9)
                        button16.pack()

                    def command11():        #delete account

                        user_frame_forget()
                        frame26.pack()
                        def command25():        #delete

                            delete(user)
                            root.destroy()
                        button18 = Button(frame26, text='delete',command=command25)
                        button18.pack()

                    def command13():    #see all orders
                        user_frame_forget()
                        frame16.pack(fill='both')
                        point.execute("select* from orders where customer='{}'".format(user))
                        fetch_27=point.fetchall()
                        scrolframe6 = 'scrolframe6'
                        my_canvas6 = 'my_canvas6'
                        table6 = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                   'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                        table_print(table6,fetch_27,main_frame6,my_canvas6,scrolframe6,frame16)
                        frame29.pack(fill='both', expand=True)

                        def command14():        #back

                            frame16.pack_forget()
                            for i in frame16.winfo_children():
                                i.pack_forget()
                            frame29.pack_forget()
                            frame30.pack(fill='both')
                            main_frame6.pack_forget()
                            for i in main_frame6.winfo_children():
                                i.pack_forget()
                            for i in frame29.winfo_children():
                                i.pack_forget()
                            table6 = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                       'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                            scrolframe7 = 'scrolframe7'
                            my_canvas7 = 'my_canvas7'
                            table_print(table6,fetch_27,main_frame7,my_canvas7,scrolframe7, frame30)
                            frame5.pack( fill='both', expand=True,pady=5)
                        button17=Button(frame29,text='BACK',command=command14)
                        button17.pack(fill='both')

                    button7 = Button(frame5, text='WANT TO ORDER',command=command4,font='calibri 16 bold', bg='spring green3',width=20)
                    button7.pack()
                    button8 = Button(frame5, text='EDIT LOGIN_INFO',font='calibri 16 bold', bg='spring green3',width=20,command=command10)
                    button10 = Button(frame5, text='CANCEL ORDER',command=command6,font='calibri 16 bold', bg='spring green3',width=20)
                    button11 = Button(frame5, text='DELETE ACCOUNT',font='calibri 16 bold', bg='spring green3',width=20,command=command11)
                    button12 = Button(frame5, text='LOGOUT',font='calibri 16 bold', bg='spring green3',width=20,command=root.destroy)
                    button13 = Button(frame5, text='SEE ALL ORDER',font='calibri 16 bold', bg='spring green3',width=20,command=command13)
                    button8.pack(), button10.pack(), button11.pack(),  button13.pack(),button12.pack()
                else:
                    frame17.pack(fill='both',expand=True,pady=20)

                    def command15():            #reveiw old orders

                        frame17.pack_forget()
                        frame18.pack(fill='both')
                        frame19.pack(fill='both', expand=True)
                        point.execute("select name from login_info where user='{}'".format(user))
                        fetch_30=point.fetchone()
                        shop=fetch_30[0]
                        point.execute("select * from orders where SHOP_NAME='{}' order by order_id desc".format(shop))
                        fetch_31=point.fetchall()
                        table7 = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                   'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                        scrolframe8 = 'scrolframe8'
                        my_canvas8 = 'my_canvas8'
                        table_print(table7,fetch_31,main_frame8,my_canvas8,scrolframe8,frame18)

                        def command16():        #back

                            frame18.pack_forget(),frame19.pack_forget()
                            frame17.pack(pady=20)
                            main_frame8.pack_forget()
                            for i in main_frame8.winfo_children():
                                i.forget()
                            button29.pack_forget()
                        button29=Button(frame19, text='BACK', font='calibri 16 bold', bg='spring green2',width=20,command=command16)
                        button29.pack()

                    def command17():        # main to add product

                        frame17.pack_forget()
                        frame20.pack(fill='both', expand=True)
                        label16=Label(frame20,text='PRODUCT NAME')
                        label17 = Label(frame20, text='PRICE')
                        label18 = Label(frame20, text='QUANTITY')
                        label16.pack()
                        entry_box12=Entry(frame20)
                        entry_box12.pack()
                        label17.pack()
                        entry_box13 = Entry(frame20)
                        entry_box13.pack()
                        label18.pack()
                        entry_box14 = Entry(frame20)
                        entry_box14.pack()

                        def command18():        #back

                            quantity=entry_box14.get()
                            price=entry_box13.get()
                            product=(entry_box12.get()).upper()
                            point.execute("select max(slno) from stock_list")
                            fetch_12 = point.fetchone()
                            if fetch_12[0] == None:
                                print(fetch_12,type(fetch_12))
                                print('hello')
                                slno = 1
                            else:
                                sl_no =fetch_12[0]
                                slno = int(sl_no) + 1
                            point.execute("select name from login_info where user='{}'".format(user))
                            fetch_13 = point.fetchone()
                            str7 = fetch_13[0]
                            point.execute(
                                " insert into STOCK_LIST values({},'{}',{},{},'{}')".format(slno, product, price,
                                                                                            quantity, str7))
                            mydb.commit()
                            label16.pack_forget(),label17.pack_forget(),label18.pack_forget()
                            entry_box14.pack_forget(),entry_box13.pack_forget(),entry_box12.pack_forget()
                            frame20.pack_forget()
                            frame17.pack(pady=20)
                            button30.pack_forget()
                        button30=Button(frame20, text='SUBMIT',bg='spring green2',command=command18)
                        button30.pack()

                    def command19():          #main to stock_list

                        frame17.pack_forget()
                        frame21.pack(fill='both')
                        frame22.pack(fill='both', expand=True)
                        point.execute("select name from login_info where user='{}'".format(user))
                        fetch_25=point.fetchone()
                        shop1=fetch_25[0]
                        point.execute("select* from stock_list where shop_name='{}'".format(shop1))
                        fetch_28=point.fetchall()
                        scrolframe9 = 'scrolframe9'
                        my_canvas9 = 'my_canvas9'
                        table10 = [('SLNO   ', 'PRODUCTS     ', ' PRICE   ', ' QUANTITY ', ' SHOP_NAME')]
                        table_print(table10,fetch_28,main_frame9,my_canvas9,scrolframe9,frame21)

                        def command20():        #back

                            frame22.pack_forget()
                            frame21.pack_forget()
                            main_frame9.pack_forget()
                            for i in main_frame9.winfo_children():
                                i.forget()
                            frame17.pack(pady=20)
                            button33.pack_forget()
                        button33=Button(frame22,text='BACK',width=10,command=command20)
                        button33.pack()

                    def command21():          #to update stock_list

                        frame17.pack_forget()
                        frame24.pack(fill='both')
                        frame23.pack(fill='both',expand=True)
                        point.execute("select name from login_info where user='{}'".format(user))
                        fetch_26 = point.fetchone()
                        shop1 = fetch_26[0]
                        point.execute("select* from stock_list where shop_name='{}'".format(shop1))
                        fetch_29 = point.fetchall()
                        scrolframe10 = 'scrolframe10'
                        my_canvas10 = 'my_canvas10'
                        table10 = [('SLNO   ', 'PRODUCTS     ', ' PRICE   ', ' QUANTITY ', ' SHOP_NAME')]
                        table_print(table10, fetch_29,main_frame10,my_canvas10,scrolframe10, frame24,)
                        point.execute("select name from login_info where user='{}'".format(user))
                        fetch_14 = point.fetchone()
                        shop_name=fetch_14[0]
                        label19=Label(frame23,text='SLNO OF PRODUCT TO BE EDITED')
                        label19.pack()
                        entry_box15=Entry(frame23)
                        entry_box15.pack()
                        label20 = Label(frame23, text='QUANTITY AVAILABLE')
                        label20.pack()
                        entry_box16 = Entry(frame23)
                        entry_box16.pack()

                        def command22():            #back

                            quantity1=entry_box16.get()
                            slno=entry_box15.get()
                            md7 = "update stock_list set quantity={} where slno='{}'". \
                                format(quantity1, slno)
                            point.execute(md7)
                            mydb.commit()
                            frame23.pack_forget()
                            for i in frame23.winfo_children():
                                i.forget()
                            for i in main_frame10.winfo_children():
                                i.forget()
                            main_frame10.pack_forget()
                            frame17.pack(pady=20)

                        button34=Button(frame23,text='SUBMIT',command=command22)
                        button34.pack()

                    def command23():              #delete account

                        frame17.pack_forget()
                        frame25.pack(fill='both')

                        def command41():

                            delete(user,'shop')
                            root.destroy()
                        button18 = Button(frame25, text='delete',command=command41)
                        button18.pack()

                        def command24():            #back

                            point.execute("delete from login_info where user='{}'".format(user))
                            mydb.commit()
                            point.execute("select name from login_info where user='{}'".format(user))
                            fetch_33=point.fetchone()
                            shop=fetch_33[0]
                            point.execute("delete from orders where shop_name='{}'".format(shop))
                            point.execute("delete from stock_list")
                            mydb.commit()
                            frame2.pack()
                        button35=Button(frame23,text='SUBMIT',command=command24)
                        button35.pack()

                    def command26():            #edit login info (shop owner)

                        frame17.pack_forget()
                        frame27.pack(fill='both')
                        frame37.pack(fill='both')
                        label14 = Label(frame37, text='NAME', font='calibri 16 bold', bg='spring green2', width=20)
                        label14.pack()
                        entry_box8 = Entry(frame37)
                        entry_box8.pack()
                        label15 = Label(frame37, text='ADRESS', font='calibri 16 bold', bg='spring green2', width=20)
                        label15.pack()
                        entry_box9 = Entry(frame37)
                        entry_box9.pack()
                        label23 = Label(frame37, text='MOBILE NUMBER', font='calibri 16 bold', bg='spring green2',
                                        width=20)
                        label23.pack()
                        entry_box10 = Entry(frame37)
                        entry_box10.pack()
                        label24 = Label(frame37, text='PASSWORD', font='calibri 16 bold', bg='spring green2', width=20)
                        label24.pack()
                        entry_box11 = Entry(frame37)
                        entry_box11.pack()

                        def command30():        #submit

                            name = str(entry_box8.get())
                            name = name.upper()
                            house = str(entry_box9.get())
                            mobile_no = str(entry_box10.get())
                            password = str(entry_box11.get())
                            point.execute("select name from login_info where user='{}'".format(user))
                            fetch_35=point.fetchone()
                            shopname=fetch_35[0]
                            query = "update orders set shop_contact_no='{}',shop_name='{}' where shop_name='{}'"
                            point.execute(query.format(mobile_no, name, shopname))

                            query1 = "update login_info set name='{}',password='{}',adress='{}',mobile_no='{}' where user='{}'"
                            point.execute(query1.format(name, password, house, mobile_no, user))

                            query2 = "update stock_list set shop_name='{}' where shop_name='{}'"
                            point.execute(query2.format( name, shopname))
                            mydb.commit()
                            for i in frame37.winfo_children():
                                i.forget()
                            frame37.pack_forget()
                            frame17.pack(pady=20)
                        button38 = Button(frame37, text='SUBMIT', font='calibri 16 bold', command=command30)
                        button38.pack(pady=20)


                    def command27():        #EDIT STATUS OF ORDER

                        frame17.pack_forget()
                        frame27.pack(fill='both')
                        frame28.pack(fill='both',expand=True,side=BOTTOM)
                        point.execute("select name from login_info where user='{}'".format(user))
                        fetch_34 = point.fetchone()
                        shop = fetch_34[0]
                        query4 = "select * from orders where shop_name='{}' ".format(shop)
                        point.execute(query4)
                        fetch_21 = point.fetchall()
                        scrolframe11 = 'scrolframe11'
                        my_canvas11 = 'my_canvas11'
                        table7 = [('ORDER_ID', 'CUSTOMER', 'SHOP_NAME', 'ORDER', 'QUANTITY', 'PRICE', 'TOTAL',
                                   'CUSTOMEER CONTACT NO', 'SHOP CONTACT NO', 'STATUS')]
                        table_print(table7,fetch_21,main_frame11,my_canvas11,scrolframe11,frame27)
                        label21=Label(frame28,text='ENTER SLNO TO UPDATE STATUS')
                        label21.pack()
                        entry_box17=Entry(frame28)
                        entry_box17.pack()

                        def command28():

                            sl_no2=int(entry_box17.get())
                            point.execute("update orders set status='PENDING'where order_id={}".format(sl_no2))
                            mydb.commit()
                            frame28.pack_forget(),frame27.pack_forget(),
                            frame17.pack(pady=20)
                            main_frame11.pack_forget()
                            for i in main_frame11.winfo_children():
                                i.forget()
                            for i in frame28.winfo_children():
                                i.forget()

                        def command29():
                            sl_no2 = int(entry_box17.get())
                            point.execute(" update orders set status='DELIVERED' where order_id={}".format(sl_no2))
                            mydb.commit()
                            frame28.pack_forget(), frame27.pack_forget()
                            frame17.pack(pady=20)
                            main_frame11.pack_forget()
                            for i in main_frame11.winfo_children():
                                i.forget()
                            for i in frame28.winfo_children():
                                i.forget()
                        button36 = Button(frame28, text='PENDING', command=command28)
                        button36.pack()
                        button37 = Button(frame28, text='DELIVERED', command=command29)
                        button37.pack()

                    button22 = Button(frame17, text='REVIEW OLD ORDERS', font='calibri 16 bold', bg='spring green2',width=30,command=command15)
                    button23 = Button(frame17, text='VIEW STOCK LIST', font='calibri 16 bold', bg='spring green2', width=30,command=command19)
                    button24 = Button(frame17, text='ADD NEW STOCK', font='calibri 16 bold', bg='spring green2', width=30,command=command17)
                    button25 = Button(frame17, text='UPDATE STOCK LIST', font='calibri 16 bold', bg='spring green2',width=30,command=command21)
                    button26 = Button(frame17, text='DELETE ACCOUNT', font='calibri 16 bold', bg='spring green2', width=30,command=command23)
                    button27 = Button(frame17, text='LOGOUT', font='calibri 16 bold', bg='spring green2', width=30,command=root.destroy )
                    button28 = Button(frame17, text='EDIT LOGIN_INFO (PROFILE)', font='calibri 16 bold', bg='spring green2', width=30,command=command26)
                    button32 = Button(frame17, text='EDIT STATUS OF ORDER', font='calibri 16 bold', bg='spring green2', width=30,command=command27)
                    button22.pack(pady=10),button23.pack(pady=10), button24.pack(pady=10), button25.pack(pady=10), button26.pack(pady=10), button27.pack(pady=10),button28.pack(pady=10),button32.pack(pady=10)
        button5 = Button(frame3,text='SUBMIT',font='calibri 16 bold', command=command3)
        button5.pack(pady=20)


    label3 = Label(frame2, text='PLEASE CHOOSE ANY OPTION', font='calibri 26 bold', bg='spring green2')
    label3.pack()
    button2 = Button(frame2, image=p3, bd=0, command=command2, bg='spring green2')
    button3 = Button(frame2, image=p4, bd=0, bg='spring green2', command=login_info)
    button4 = Button(frame2, image=p5, bd=0, bg='spring green2',command=root.destroy)
    button2.pack(pady=25)
    button3.pack(pady=25)
    button4.pack(pady=25)


label1 = Label(frame1, image=photo)
label1.pack(pady=10)
label2 = Label(frame1,text='SOCIETY STORE',font='calibri 26 bold', bg='spring green2', bd=0)
label2.pack(pady=15)
p2 = ImageTk.PhotoImage(Image.open(r"F:\SMART SOCIETY\button (1).png"))
button1 = Button(frame1,image=p2, command=command1, bg='spring green2', bd=0)
button1.pack(pady=10)

root.mainloop()
