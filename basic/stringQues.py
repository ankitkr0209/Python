name = input("Enter name: ")

indices = []
for i in range(len(name)):
    if name[i] == " ":
        indices.append(i)

print("Indices of spaces:", indices)

print(len(indices))
if len(indices) == 0 or len(indices) == 1:
    print(name)
else:
    print(name[0],".",end='')
    for i in range(len(indices)-1):
        print(name[indices[i]],".",end='')
    
    print(name[len(indices)])




    
# if len(count) == 0 or len(count) == 1:
#     print(name)
# else:











