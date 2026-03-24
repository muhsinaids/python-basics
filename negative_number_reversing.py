number=int(input("Enter a negative number:"))
reverse=0
if(number<0):
    numbers=abs(number)
    while(numbers>0):
        reminder=numbers%10
        reverse=reverse*10+reminder
        numbers=numbers//10
    print(f"The reverse of negative number:-{reverse}")
else:
    print("Please enter a negative number")