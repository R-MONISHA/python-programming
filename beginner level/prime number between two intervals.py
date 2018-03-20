number=int(raw_input())
lower=raw_input()
upper=raw_input()
for num in range(lower,upper+1):
	if(num>1):
		for i in range(2, number):
			if number%i == 0:
				print("no")
			break
			else:
				print("yes")
			break
