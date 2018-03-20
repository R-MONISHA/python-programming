n=int(input())
temp=n
rev=0
while(n>0):
    temp=n%10
    rev=rev*10+temp
    n=n/10
if(n==rev):
   print("The number is a palindrome!")
else:
    print("no")
