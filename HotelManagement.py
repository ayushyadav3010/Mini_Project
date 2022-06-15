print("\t\tWelcome to my Hotel Management System")
print("\t\t1) Login \n\t\t2) SignUp")
ch1 = int(input())
name = [] 
mob = [] 
pas = [] 
room=0
roomdetail=[]
if ch1==1:
    print("\t\tEnter your mobile number : ",end='')
    m = int(input())  
    print("\t\tEnter your Password : ",end='')
    p = input()
    print("\t\tYOU HAVE NOT ACCOUNT") 
elif ch1==2:
    r=""
    print("\t\tEnter your First name : ",end='')
    fname = input()
    r=r+fname+" "
    print("\t\tEnter your Last name : ",end='')
    lname = input()
    r=r+lname
    name.append(r)
    print("\t\tEnter your mobile number : ",end='')
    mob.append(int(input())) 
    print("\t\tSet your password : ",end='')
    pas.append(input()) 
    print("\t\tWelcome")
    print("\t\tPlease Login")
    print("\tEnter Your Mob no : ",end='')
    mb = int(input()) 
    print("\tEnter your password : ",end='') 
    ps = input() 
    if ps in pas and mb in mob:
        j=0
        order=[]
        while (j==0):
            print("\t\tWelcome",name[0],"to Home Page") 
            print("\tWhich type of help can I")
            print("\t1) Food \n\t2) Hotel Room")
            ch2 = int(input())
            if ch2==1:
                print("\t1) You want to order food \n\t2) You want to see order details")
                ch3 = int(input())
                if ch3==1:
                    i=0
                    order=[]
                    sum =0 
                    while(i==0):
                        print("\tWhich type of food you want to order \n\t1) Potato\n\t2) Sandwich \n\t3) Burger \n\t4) Noodles")
                        print("\t5) Chilli \n\t6) Rice \n\t7) Pasta \n\t8) Pizza")
                        chf = int(input())
                        if chf==1:
                            print("\tItem                     Rupees")
                            print("\t1) French Fries          70 rs\n\t2) Potato Wedger         80 rs \n\t3) Cheese Balls          100 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\ttFrench fries   ---> 70" 
                                order.append(r)
                                print("\t\tYour French Fries is ordered succesfully")
                                sum = sum + 70
                                print("\t\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\t\tInvalid choie")
                             
                            elif chf1==2:
                                r = "\t\tPotato Wedger   ---> 80" 
                                order.append(r)
                                print("\t\tYour Potato Wedger is ordered succesfully")
                                sum = sum + 80
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            
                         
                            elif chf1==3:
                                r = "\t\tCheese Balls   ---> 100" 
                                order.append(r)
                                print("\tYour Cheese Balls is ordered succesfully")
                                sum = sum + 100
                                print("\tYou want to order other item \n1) YES \n2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            
                            
                        elif chf==2:
                            print("\t\t   Item                   Rupees")
                            print("\t\t1) Veg Sandwich           40 rs\n\t\t2) Cheese Sandwich        40 rs \n\t\t3) PaneerCheese Sanwich   70 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\t\tVeg Sandwich   ---> 40" 
                                order.append(r)
                                print("\t\tYour Veg Ssandwich is ordered succesfully")
                                sum = sum + 40
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                             
                            elif chf1==2:
                                r = "\t\tCheese Sandwich   ---> 40" 
                                order.append(r)
                                print("\t\tYour Cheese Sandwich is ordered succesfully")
                                sum = sum + 40
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==3:
                                r = "\t\tPaneerCheese Sandwich   ---> 70" 
                                order.append(r)
                                print("\t\tYour Paneer Cheese Sandwich is ordered succesfully")
                                sum = sum + 70
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                     
                        elif chf==3:
                            print("\t\t   Item             Rupees")
                            print("\t\t1) Veg Burger        70 rs\n\t\t2) Paneer Burger     80 rs \n\t\t3) Chicken Burger    100 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\t\tVeg Burger   ---> 70" 
                                order.append(r)
                                print("\t\tYour Veg Burger is ordered succesfully")
                                sum = sum + 70
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==2:
                                r = "\t\tPaneer Burger   ---> 80" 
                                order.append(r)
                                print("\t\tYour Paneer Burger is ordered succesfully")
                                sum = sum + 80
                                print("\tYou want to order other item \n/t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            
                         
                            elif chf1==3:
                                r = "\t\tChicken Burger   ---> 100" 
                                order.append(r)
                                print("\t\tYour Chicken Burger is ordered succesfully")
                                sum = sum + 100
                                print("\tYou want to order other item \n/t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                         
                        elif chf==4:
                            print("\t\t   Item                 Rupees")
                            print("\t\t1) Veg Noodles           50 rs\n\t\t2) Paneer Noodles        80 rs \n\t\t3) Egg Noodles           100 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\t\tVeg Noodles   ---> 50" 
                                order.append(r)
                                print("\t\tYour Veg Noodles is ordered succesfully")
                                sum = sum + 50
                                print("\tYou want to order other item \n1) YES \n2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                             
                            elif chf1==2:
                                r = "\t\tPaneer Noodles   ---> 80" 
                                order.append(r)
                                print("\t\tYour Paneer Noodles is ordered succesfully")
                                sum = sum + 80
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==3:
                                r = "\t\tEgg Noodles   ---> 100" 
                                order.append(r)
                                print("\t\tYour Egg Noodles is ordered succesfully")
                                sum = sum + 100
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                        elif chf==5:
                            print("\t\t   Item                  Rupees")
                            print("\t\t1) Paneer Chilli          120 rs\n\t\t2) Chicken Chilli Bone    100 rs \n\t\t3) Soya Chilli            80 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\t\tChilli Paneer   ---> 120" 
                                order.append(r)
                                print("\t\tYour Paneer Chilli is ordered succesfully")
                                sum = sum + 120
                                print("\tYou want to order other item \n1) YES \n2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==2:
                                r = "\t\tChicken Chilli Bone   ---> 100" 
                                order.append(r)
                                print("\t\tYour Chicken Chilli Bone is ordered Succesfully")
                                sum = sum + 100
                                print("\tYou want to order other item \n1) YES \n2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==3:
                                r = "\t\tSoya Chilli   ---> 80" 
                                order.append(r)
                                print("\t\tYour Soya Chilli is ordered succesfully")
                                sum = sum + 80
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                         
                        elif chf==6:
                            print("\t\t    Item                 Rupees")
                            print("\t\t1) Jeera Rice            70 rs\n\t\t2) Veg Fried Rice        110 rs \n\t\t3) Egg Fried rice        120 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\t\tJeera rice   ---> 70" 
                                order.append(r)
                                print("\t\tYour Jeera rice is ordered succesfully")
                                sum = sum + 70
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==2:
                                r = "\t\tVeg Fried Rice   ---> 110" 
                                order.append(r)
                                print("\t\tYour Veg Fried Rice is ordered succesfully")
                                sum = sum + 110
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==3:
                                r = "\t\tEgg Fried Rice   ---> 120" 
                                order.append(r)
                                print("\t\tYour Egg Fried Rice is ordered succesfully")
                                sum = sum + 120
                                print("\tYou want to order other item \n1) YES \n2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                        elif chf==7:
                            print("\t\t   Item              Rupees")
                            print("\t\t1) Veg Pasta         90 rs\n\t\t2) Non Veg Pasta     100 rs \n\t\t3) Masala Pasta      110 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\t\tVeg Pasta   ---> 90" 
                                order.append(r)
                                print("\t\tYour Veg Pasta is ordered succesfully")
                                sum = sum + 90
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                             
                            elif chf1==2:
                                r = "\t\tNon Veg Pasta   ---> 100" 
                                order.append(r)
                                print("\t\tYour Non Veg Pasta is ordered succesfully")
                                sum = sum + 100
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==3:
                                r = "\t\tMasala Pasta   ---> 110" 
                                order.append(r)
                                print("\t\tYour Masala Pasta is ordered succesfully")
                                sum = sum + 110
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                         
                        elif chf==8:
                            print("\t\t   Item                Rupees")
                            print("\t\t1) Veg Pizza           80 rs\n\t\t2) Paneer Pizza        110 rs \n\t\t3) Chicken Pizza       130 rs")
                            print("\tWhich item you want to do order")
                            chf1 = int(input()) 
                            if chf1==1:
                                r = "\t\tVeg Pizza   ---> 80" 
                                order.append(r)
                                print("\t\tYour Veg Pizza is ordered succesfully")
                                sum = sum + 80
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                             
                            elif chf1==2:
                                r = "\t\tPaneer Pizza   ---> 110" 
                                order.append(r)
                                print("\t\tYour Paneer Pizza is ordered Succesfully")
                                sum = sum + 110
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                            elif chf1==3:
                                r = "\t\tChicken Pizza   ---> 130" 
                                order.append(r)
                                print("\t\tYour Chicken Pizza is ordered succesfully")
                                sum = sum + 130
                                print("\tYou want to order other item \n\t1) YES \n\t2) NO")
                                chf11 = int(input()) 
                                if chf11==1:
                                    i=0 
                                elif chf11==2:
                                    i=i+1
                                else:
                                    print("\tInvalid choie")
                    print("\t\tYou Want Return Home Page. \n\t\t1) yes \n\t\t2) No")
                    chm = int(input())
                    if chm==1:
                        j=0  
                    elif chm==2:
                        print("\t\t THANK YOU!")
                        j=j+1
                    else:
                        print("\t\tInvalid Choice")

                elif ch3==2:
                    print("\t\t ORDER LIST IS \n")
                    for i in order:
                        print("\t\t",i) 
                    print("\t\tTotal Price is : ",sum)
                    print("\t1) You want to go back Home Page \n\t2) YOu want to exit this service")
                    ch211=int(input())  
                    if ch211==1:
                        j=0  
                    elif ch211==2:
                        print("\t\tTHANK YOU!") 
                        j=j+1
                    else:
                        print("\t\tInvalid Choice")
                else:
                    print("\t\tInavlid choice")
                    pass 
            elif ch2==2:
                print("\t\t1) You want to book room \n\t\t2) Booked Room details")
                chb = int(input())   
                if chb==1:
                    print("\t\tWhich type of room you want to book \n\t1) AC Room          1000 rs/per day \n\t2) Non AC Room      700 rs/per day")
                    ch21 = int(input())
                    if ch21==1:
                        r="AC Room   ----->  1000 rs/per day booked"
                        room=room+1000
                        print("\t\t",r)
                        roomdetail.append(r)
                        print("\t\tYour Ac Room is booked")
                        print("1) You want to go back Home Page \n2) YOu want to exit this service")
                        ch211=int(input())  
                        if ch211==1:
                            j=0  
                        elif ch211==2:
                            print("THANK YOU!") 
                        else:
                            print("Invalid Choice")
                    elif ch21==2:
                        r=""
                        r="Non AC Room   ----->  700 rs/per day booked"
                        rom=room+700
                        print("\t\t",r)
                        roomdetail.append(r)
                        print("Your Non Ac Room is booked") 
                        print("1) You want to go back Home Page \n2) YOu want to exit this service")
                        ch211=int(input())  
                        if ch211==1:
                            j=0  
                        elif ch211==2:
                            j=j+1
                            print("THANK YOU!") 
                        else:
                            print("Invalid Choice")
                elif chb==2:
                    print("\t\t Room Booked \n")
                    for i in roomdetail:
                        print("\t\t",i) 
                    print("\t\tTotal Cost is : ",room,"rs")
                    print("1) You want to go back Home Page \n2) YOu want to exit this service")
                    ch211=int(input())  
                    if ch211==1:
                        j=0  
                    elif ch211==2:
                        print("THANK YOU!") 
                        j=j+1
                    else:
                        print("Invalid Choice") 
            else:
                print("Invalid Choice")

    else:  
        print("Invalid mob or password")
else:
    print("Invalid Input")
