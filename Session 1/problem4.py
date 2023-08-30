card_num = input("Enter Card Number: ")
every_other_digit = card_num[-2::-2]
sum = 0
for digit in every_other_digit:
    dble = int(digit) * 2
    while dble :
        sum = sum + dble%10
        dble = dble//10

other_digits = card_num[-1::-2]
for digit in other_digits:
    sum += int(digit)

am_exp = ["34", "37"]
mast_card = (str(num) for num in range(51,56))

if sum%10 == 0:
    if card_num[0:2] in am_exp:
        print("American Express")
    elif card_num[0:2] in mast_card:
        print("Master Card")
    elif card_num[0] == '4':
        print("Visa")
    else:
        print("Invalid")
else:
    print("Invalid")
 