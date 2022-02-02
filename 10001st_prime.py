goal = 2
num1= 3
num2 = 2

while goal < 10002:
    for i in range(2, num1+1):
        if num1%num2 == 0 and num2 != num1:
            num1 +=2
            num2 = 2
        else:
            num2 +=1
        if num1%num2 == 0 and num1 == num2:
            goal +=1
            if goal == 10002:
                print(num1)
            num1 +=2
            num2 = 2
        


