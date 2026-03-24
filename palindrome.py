number=int(input("Enter a number :"))
print("The number is :",number)
reverse=0
num=number
while(num>0):
    remainder=num%10
    reverse=reverse*10+remainder
    num=num//10
print("the reverse of the number is:",reverse)
if(number==reverse):
    print("The number is a palindrome")  
else:
    print("The number is not a palindrome ")  