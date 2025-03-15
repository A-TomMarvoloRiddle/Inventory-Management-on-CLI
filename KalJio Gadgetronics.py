#                                                                  KalJio Gadgetronics
import sys
import time
import datetime
import prettytable as p
import mysql.connector as m
mcon=m.connect(host="localhost", user="root", passwd="scott", database="kaljio")
cr=mcon.cursor()


logintype=0
def made_by():
    msg = ''' 
            Company Name                    : Kaljio Gadegetronics Private.ltd
            Version                         : 2.1.1
            Programming Team                : Apaar Mathur
            Address                         : 12A DPS Jodhpur
            Session                         : 2022-23
            Contact info                    : 80035xxxxx
            \n\n
        '''
    for x in msg:
        print(x, end='')
        time.sleep(0.000001)
    

def logout():
    t=datetime.datetime.now()
    if t.hour<12:
        message3()
        print('Have a nice day :)')
    elif t.hour>=12 and t.hour<17:
        message3()
        print("Great Time Ahead")
    else:
        message3()
        print("Good night")
    time.sleep(3)
    sys.exit()
        
def utime():
    t=datetime.datetime.now()
    print(t.ctime(),end='')
    
def message1():
    print('\n'," Your requested changes(if there were any) are successfully saved  :) ")


def message2():
    print('\n'," Thanks for Showing Interset in KALJIO Gadgetronics......Hope to see you soon :) ")


def message3():
    print('\n'," Thanks for visiting KALJIO Gadgetronics......Hope to see you soon :) ")
   

# menu() is the main or initial Menu
def menu():
    print('\n')
    print('-'*33)
    print('|',' '*3,' KalJio Gadgetronics ',' '*3,'|' )
    print('|','-'*27,'  |')
    print('|',' '*9,'M E N U',' '*9,'  |')
    print('|','-'*27,'  |')
    print('|   ',end='')
    utime()
    print('    |')
    print('|','-'*27,'  |')
    print('|','1) U S E   A S   A D M I N   ','|')
    print('|','2) U S E   A S   G U E S T   ','|')
    print('|','3) A B O U T   U S           ','|')
    print('|','4) S H U T   D O W N         ','|')
    print('|','-'*27,'  |')
    print('-'*33)
    password()


def signin():
      print('-'*29)
      print(' '*11,'Signin',' '*7,)
      print('-'*29)
      uname=input('Enter user name: ')
      upass=input("Password : ")
      cr.execute("select * from login where username='{}' and password='{}'".format(uname,upass))
      x=cr.fetchone()
      
      if x==None:
            print("Check your Credentials")
      else:
            print('\nWelcome as Admin')
            menuadmin()
             
            
def signup():
      print("-"*40)
      uname=input("Enter User Name : ")
      
      q="select * from login where username='{}'".format(uname)
      cr.execute(q)
      x=cr.fetchone()
      
      if x==None:
            
            upass=input("Password : ")
            query="insert into login values('{}','{}')".format(uname, upass)
            x=cr.execute(query)
            mcon.commit()
      else:
            print("Username already exist")
      

# password() is the function to check user type and make the code work accordingly
def password():
        logintype =input('Enter user type :  ')
        if logintype=='1':
            signin()
        elif logintype=='2':
            print('\nWelcome as Guest')
            menuguest()
            return
        elif logintype=='3':
            print('\n',' '*26," (:   About Us  :) ",' '*7)
            made_by()
            input('Press <ENTER> to Continue\n')
            menu()
        elif logintype=='4' or logintype.lower()=='quit':
            logout()
        else:
            print('\nEnter a Valid Choice!!\n')
            menu()
           



# menuadimn() is the Menu specialised for Admin which will only be accesed when the coreect username & pass are enterned by the user
def menuadmin():
    while True:
        print('-'*33)
        print('|',' '*7,'Menu option',' '*7,'  |')
        print('|','-'*27,'  |')
        print('|   ',end='')
        utime()
        print('    |')
        print('|','-'*27,'  |')
        print('|','1) Display All               ','|')
        print('|','2) New Product Entry         ','|')
        print('|','3) Update information        ','|')
        print('|','4) Delete Entry              ','|')
        print('|','5) Filter by Product name    ','|')
        print('|','6) Filter by Company         ','|')
        print('|','7) Filter by feature         ','|')
        print('|','8) Filter by price           ','|')
        print('|','9) Display Total no. of items','|')
        print('|','10) Add New Login ID         ','|')
        print('|','11)L O G O U T               ','|')
        print('-'*33,'\n')
        option=input("Enter Choice : ")
        if option=='1' or option.lower()in'display all':
            dispall()
            input('Press <ENTER> to Continue\n')        
        elif option=='2' or option.lower()in'new entry':
            entry()
            input('Press <ENTER> to Continue\n')
        elif option=='3' or option.lower()=='update':
            updateinfo()
            input('Press <ENTER> to Continue\n')
        elif option=='4' or option.lower()=='delete':
            deleteinfo()
            input('Press <ENTER> to Continue\n')
        elif option=='5' or option.lower()in'search by name':
            searchbyname()
            input('Press <ENTER> to Continue\n')
        elif option=='6' or option.lower()in'search by company':
            searchbycomany()
            input('Press <ENTER> to Continue\n')
        elif option=='7' or option.lower()in'search by feature':
            searchbyfeature()
            input('Press <ENTER> to Continue\n')
        elif option=='8' or option.lower()in'search by price':
            searchbyprice()
            input('Press <ENTER> to Continue\n')
        elif option=='9' or option.lower()in'total no. of products':
            total()
            input('Press <ENTER> to Continue')
        elif option=='10' or option.lower()in'total no. of products':
            signup()
            input('Press <ENTER> to Continue')
        elif option=='11' or option.lower()=='logout':
            logout()
            break
        else:
            print('Enter a Valid Choice!!')
            continue


# menuguest() is the Menu specialised for Guest/other than Admin, which will be accessed when the the login type is given as 2 
def menuguest():
    while True:
        print('-'*33)
        print('|',' '*7,'Menu option',' '*7,'  |')
        print('|','-'*27,'  |')
        print('|   ',end='')
        utime()
        print('    |')
        print('|','-'*27,'  |')
        print('|','1) Display All               ','|')
        print('|','2) Filter by Product name    ','|')
        print('|','3) Filter by Company         ','|')
        print('|','4) Filter by Feature         ','|')
        print('|','5) Filter by price           ','|')
        print('|','6) L O G O U T               ','|')
        print('-'*33,'\n')  
        option=input("Enter Choice : ")
        if option=='1' or option.lower()in'display all':
            dispall()
            input('Press <ENTER> to Continue\n')
        elif option=='2' or option.lower()in'search by name':
            searchbyname()
            input('Press <ENTER> to Continue\n')
        elif option=='3' or option.lower()in'search by company':
            searchbycomany()
            input('Press <ENTER> to Continue\n')
        elif option=='4' or option.lower()in'search by feature':
            searchbyfeature()
            input('Press <ENTER> to Continue\n')
        elif option=='5' or option.lower()in'search by price':
            searchbyprice()
            input('Press <ENTER> to Continue\n')
        elif option=='6' or option.lower()=='logout':
            logout()
            break
        else:
            print('\nEnter a Valid Choice!!\n')
            continue
            


# total() shows the no. of products in d{}
def total():
    cr.execute('select * from product')
    data=cr.fetchall()
    total=len(data)
    print('\nTotal Products available : ',total)
    print('\n')



# entry() is to insert a new product
def entry():
    try:
        print(' '*5,'Add Products','\n')
        pno=int(input('Enter Product number   : '))
        pname=input('Enter Product name   : ')
        compnam=input('Enter company name : ')
        featr=input('Enter a feature      : ')
        price=float(input('Enter price    : '))
        query="insert into product values({},'{}','{}','{}',{})".format(pno,pname,compnam,featr,price)
        cr.execute(query)
        mcon.commit()
    except:
        print("Problem in insertion")
    print('\n')

def updateprice():
      upid=int(input("Enter product id:"))
      q="select * from product where pno={}".format(upid)
      cr.execute(q)
      x=cr.fetchall()
      a=cr.rowcount
      if a==0:
            print("record does not exist")
      else:
            uprice=int(input("Enter new price: "))
            query="update product set price={} where pno={}".format(uprice,upid)
            x=cr.execute(query)
            mcon.commit()
            print('Record updated successfully')


def updatename():
      upid=int(input("Enter product id:"))
      q="select * from product where pno={}".format(upid)
      cr.execute(q)
      x=cr.fetchall()
      a=cr.rowcount
      if a==0:
            print("record does not exist")
      else:
            upname=input("Enter new Product name: ")
            query="update product set pname='{}' where pno={}".format(upname,upid)
            x=cr.execute(query)
            mcon.commit()
            print('Record updated successfully')

def updatecompname():
      upid=int(input("Enter product id:"))
      q="select * from product where pno={}".format(upid)
      cr.execute(q)
      x=cr.fetchall()
      a=cr.rowcount
      if a==0:
            print("record does not exist")
      else:
            ucompname=input("Enter new company name: ")
            query="update product set compnam='{}' where pno={}".format(ucompname,upid)
            x=cr.execute(query)
            mcon.commit()
            print('Record updated successfully')

def updatefeatr():
      upid=int(input("Enter product id:"))
      q="select * from product where pno={}".format(upid)
      cr.execute(q)
      x=cr.fetchall()
      a=cr.rowcount
      if a==0:
            print("record does not exist")
      else:
            ufeatr=input("Enter new Feature: ")
            query="update product set featr='{}' where pno={}".format(ufeatr,upid)
            x=cr.execute(query)
            mcon.commit()
            print('Record updated successfully')

def updateall():
      upid=int(input("Enter product id:"))
      q="select * from product where pno={}".format(upid)
      cr.execute(q)
      x=cr.fetchall()
      a=cr.rowcount
      if a==0:
            print("record does not exist")
      else:
            upname=input("Enter new Product name: ")
            ucompname=input("Enter new company name: ")
            ufeatr=input("Enter new Feature: ")
            uprice=int(input("Enter new price: "))
            query="update product set pname='{}',compnam='{}',featr='{}',price={} where pno={}".format(upname,ucompname,ufeatr,uprice,upid)
            x=cr.execute(query)
            mcon.commit()
            print('Record updated successfully')


# updateinfo() is for updating the information of a product present in d{}
def updateinfo():
        print("\nWhat would you like to change?\n1)Product Name\n2)Company name\n3)Feature\n4)Price\n5) All\n")
        option=int(input("Enter your option 1/2/3/4/5 : "))
        print('\n')
        if option==1:
            updatename()
        elif option==2:
            updatecompname()
        elif option==3:
            updatefeatr()
        elif option==4:
            updateprice()
        elif option==5:
            updateall()
        print('\n')


# searchbyname() is to filter products on the basis of their name
def searchbyname():
    print(' '*5,'Search by Product Name')
    try:
        pname=input('Enter Product to be searched : ')
        query="select * from product where pname='{}'".format(pname)
        cr.execute(query)
        data= cr.fetchall()
        t=p.PrettyTable(['Product ID','Product Name','Company Name','Feature','Price'])
        for a,b,c,d,e in data:
            t.add_row([a,b,c,d,e])
        print(t)
        
    except:
        print("connectivity error in show")
    print('\n')


# searchbyprice() is to filter products on the basis of their price
def searchbyprice():
    print(' '*5,'Search by Price')
    print('To Enter Min. Price press 1 ')
    print('To Enter Max. Price press 2 ')
    print('To Enter Price segment press 3') 
    segment=int(input('Enter Range Segment :'))
    if segment==1:
        try:
            price=int(input("Enter Min. Price:")) 
            query="select * from product where price>={}".format(price)
            cr.execute(query)
            data= cr.fetchall()
            t=p.PrettyTable(['Product ID','Product Name','Company Name','Feature','Price'])
            for a,b,c,d,e in data:
                t.add_row([a,b,c,d,e])
            print(t)
            
        except:
            print("connectivity error in show")
        print('\n')
    elif segment==2:
        try:
            price=int(input("Enter Max. Price:"))
            query="select * from product where price<={}".format(price)
            cr.execute(query)
            data= cr.fetchall()
            t=p.PrettyTable(['Product ID','Product Name','Company Name','Feature','Price'])
            for a,b,c,d,e in data:
                t.add_row([a,b,c,d,e])
            print(t)
            
        except:
            print("connectivity error in show")
        print('\n')
    elif segment==3:
        try:
            pricedown=int(input("Enter Min. Price:"))
            priceup=int(input("Enter Max. Price:"))
            query="select * from product where price between {} and {} order by price".format(pricedown,priceup)
            cr.execute(query)
            data= cr.fetchall()
            t=p.PrettyTable(['Product ID','Product Name','Company Name','Feature','Price'])
            for a,b,c,d,e in data:
                t.add_row([a,b,c,d,e])
            print(t)
            
        except:
            print("connectivity error in show")
        print('\n')
        

# searchbyfeature() is to filter products on the basis of their features
def searchbyfeature():
    print(' '*5,'Search by Feature')
    try:
        ufeatr=input('Enter feature to be searched : ')
        query="select * from product where featr='{}' order by pno".format(ufeatr)
        cr.execute(query)
        data= cr.fetchall()
        t=p.PrettyTable(['Product ID','Product Name','Company Name','Feature','Price'])
        for a,b,c,d,e in data:
            t.add_row([a,b,c,d,e])
        print(t)
        
    except:
        print("connectivity error in show")
    print('\n')



# searchbycompany() is to filter products on the basis of the manufacturing company
def searchbycomany():
    print(' '*5,'Search by company Name')
    try:
        ucompname=input('Enter company to be searched : ')
        query="select * from product where compnam='{}' order by pname".format(ucompname)
        cr.execute(query)
        data= cr.fetchall()
        t=p.PrettyTable(['Product ID','Product Name','Company Name','Feature','Price'])
        for a,b,c,d,e in data:
            t.add_row([a,b,c,d,e])
        print(t)
        
    except:
        print("connectivity error in show")
    print('\n')



# dispall() is to show all the products 
def dispall():
   
    cr.execute("Select * from product order by pname")
    data= cr.fetchall()
    t=p.PrettyTable(['Product ID','Product Name','Company Name','Feature','Price'])
    for a,b,c,d,e in data:
        t.add_row([a,b,c,d,e])
    print(t)
    
    

    

# deleteinfo() is to remove a product from d{}
def deleteinfo() : 
      upid=int(input("Enter product id:"))
      q="select * from product where pno={}".format(upid)
      cr.execute(q)
      x=cr.fetchall()
      a=cr.rowcount
      if a==0:
            print("record does not exist")
      else:
            query="delete from product where pno={}".format(upid)
            x=cr.execute(query)
            mcon.commit()
            print('Record deleted successfully')
    

menu()


