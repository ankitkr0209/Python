

# class compare:
#     def __greater(self,a,b):
#         self.a=a
#         self.b=b
#         if(self.a > self.b):
#             return self.a
#         else:
#             return self.b 
#     def display(self,a,b):
#         print("Greater number : " , self.__greater(a,b))
    

# cmp1 = compare()
# cmp1.display(5,6)

# # display(2,9)

class ClassWithGlobalFunction:
    global spam
    def spam(): return 'eggs'

    def method(self):
        global monty
        def monty(): return 'python'
print(spam())