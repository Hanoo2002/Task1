n = int(input("Enter Num"))
while (n < 1 or n >8):
    n = int(input("Enter Num"))
for i in range(1,n+1):
        print (" "*(n-i)+"#"*i+"  "+"#"*i )