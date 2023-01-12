import math


# def std_lang(name,age,*languages):

#     for lang in languages:
#         print(lang)


# std_lang("ahmed",22,"C#","C++","CSS",12)
# print("*****************")
# std_lang("C#","C++","CSS","Java")











#initialize parameters with default values 
def summation(n1=11,n2=0,n3=0): 
    print(n1,n2,n3)
    print(n1+n2+n3)
    # print(n1,n2)
    # print(n3)
    return (n1+n2+n3)


# x=input("enter any Nomber ")
# summation(15,4,7)
# print(summation(15,4,7))
a=summation()
print(f"result {a}")












# x=2
# print(f"x from Global Scope is {x}")

# def myMethod():
#     global x
#     y=5 # Local
#     print(f"x inside function {x}")
#     print(f"y local Var. {y}")
#     x=x+y
#     print(f"x +y =  {x}")


# myMethod()
# # print(f"y from Global Scope is {y}")
# print(f"x from Global Scope is {x}")










# # x=5

# # def scop1():
# #     global x
# #     x=1
# #     print(f"x= {x} from function1")

# # print(f"global x = {x}")
# # scop1()
# # print(f"global x = {x}")