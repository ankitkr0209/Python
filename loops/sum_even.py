n = int(input("enter the number upto which you want the sum of even number :-" ))
sum = 0

for i in range(1,n):
    if i%2 == 0:
        sum+=i


print("sum of even number = ",sum)
