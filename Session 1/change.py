money = int(input("Enter amount: "))
while(money < 0):
    money = int(input("Enter positive amount: "))

bills = [200, 100, 50 , 20, 10 , 5 , 1]
for bill in bills:
    num = money // bill
    money = money % bill
    if num != 0:
        print(str(num) + " X " + str(bill) + "L.E. ", end="")
        if bill != 1:
            print(" + ",end="")
   
