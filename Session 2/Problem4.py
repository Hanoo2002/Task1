from collections import deque
 


def check_balance(brackets):
    stack = deque()
    for b in brackets:
        if b == '(':
            stack.append(b)
        else:
            if not bool(stack):
                return False
            stack.pop()
    if bool(stack):
        return False
    return True


bracks = input("Enter brackets: ")
if check_balance(bracks):
    print("Yes")
else:
    print("No")
