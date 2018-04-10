print("1.sum")
print("2.sub")
print("3.div")
print("4.mod")
print("5.exp")
print("6.floor_division")
print("7.mul")
print("enter the operation")
choice=int(input())
num1=int(input())
num2 =int(input())
if choice==1:
	sum= num1 + num2
	print("sum of num1 and num2 ",sum)
elif choice==2:
	sub=num1-num2
	print("sub of num1 and num2 ",sub)
elif choice==3:
            div=num1/num2
            print("div of num1 and num2 ",div)
elif choice==4:
            mod=num1%num2
            print("mod of  num1 and num2",mod)
elif choice==5:
            exp=num1**num2
            print("exp of  num1 and num2 ",exp)
elif choice==6:
            floor_division=num1//num2
            print("floor_division of num1 and num2",floor_division)
else:
	mul=num1*num2
	print("mul of num1 and num2",mul)
