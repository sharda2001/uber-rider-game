name=input("Enter your name: ")
print("------------hii",name,"Welcome to BABY Cabs","------------")
print("*********************")
print("Till your destination, we will make sure to be your best companion :)")
print("*********************")
import random
def book_my_ride():
    Destination=["patna","hajipur","mahua","goroul","muzaffarpur"]
    Drivers=[["Sonu","Monu"],["ram","shyam"],["ravi","Jay"],["Vijay","vinayak"],["paankaj","Samarat"]]
    limit=int(input("How many rides you want?"))
    index=1
    d={}
    transport=["UberGo","UberAuto","Mini","Prime Sedan"]
    for t in transport:
        print(t)
    Book_any=input("enter your ride: ")
    confirm=input("Enter Yes for confirmation: ")
    
    print("~~~~Thankyou for confirming~~~~")
      
    book=int(input("for Booking Click option :1 >>>"))
    print("CONFIRM__\n hii sharda you booked\n i'm on the way ")
    print(">>>>>>>>>>>>")
    print("your otp is___1978")
    print("which type of payment you want to pay: ")
    print("1. online")
    print("2. cash")
    enter=input("enter your pickup location: ")
    for i in Destination:
        print(i)
    print("These are the places you can make an easy ride!")
    while index<=limit:
        select=input("enter your destination: ")
        # print("~~~Your cab is coming in few minutes~~~")
        i=0
        while i<len(Destination):
            if select==Destination[i]:
                j=0
                # total=0
                while j<len(Drivers[i]):
                    a=random.choice(Drivers[j])
                    print("available drivers are:",a)
                    j+=1
                choose=input("enter any one rider: ")
             
                total=0
                if book==1:
                    km=int(input("enter your kilometers: "))
                    fare=km*5
                    total+=fare
                b=total
                d[choose]=b
                print(d)
                print("~~~Your cab is coming in few minutes~~~")
            i+=1
        index+=1
    Rate_us=int(input("How was your ride rate by giving us numbers upto 5: "))
    if Rate_us<=2:
        a=input("Give us Feedback")
        print(a)
    elif Rate_us<=3:
        print("You need to work more on safety")
    else:
        print("It was best ride Thankyou :)")
        print
book_my_ride()
def ride_again():
    while True:
        again=input("Do you want to cancle your cab press y for yes and n for no: ") 
        if again=="y":
            print("Thankyou For riding with us!")
            break
        else:
             book_my_ride()
ride_again()
