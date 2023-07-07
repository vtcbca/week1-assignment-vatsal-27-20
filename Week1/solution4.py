#write a program to check given number is armstrong or not
n=int(input("Enter number:"))
sum=0
temp=n
while temp>0:
        dig=temp%10
        sum += dig **3
        temp //=10
if n==sum:
    print("The number is a armstrong!")
else:
    print("The number is not armstrong!")