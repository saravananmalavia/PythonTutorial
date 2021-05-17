print("Enter a number")
n = int(input())
m = n
result = 0
while(n>0):
    lastdigit = n % 10
    result = result + lastdigit
    n = int (n / 10)
print("The digit sum of ", m , " is ",result) 
