tea_variety = [ "green" , "black" , "masala" , "white","Oolang"]
print(tea_variety)
print(tea_variety[-2])
print(tea_variety[2])

tea_variety[3] = "herbal"
print(tea_variety)
tea_variety[1:2] = ["coffe"]
print(tea_variety)
tea_variety[1:3] = ["capachino" , "coffe"]
for tea in tea_variety:
    print(tea)

for tea in tea_variety:
    print(tea, end="--")
print()
 
tea_variety.insert(2,"water")
tea_variety.pop()
squared_num = [x**2 for x in range(10)]
print(squared_num)



