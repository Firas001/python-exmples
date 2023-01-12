
# print("while loop:\n")
# x=int(input("Enter Nom. "))
# i=1
# while i<=10:
#     z=x*i
#     print(f"{x} * {i} = {z}")
#     # print(f"{x} * {i} = {x*i}")
#     # print(f"{i} * {x} = {i*x}")
#     i+=1 #i=i+1 (No i++)
# else:
    # print(f" i= {i} condition ev. {(i<=10)}")
# 
# print("outside while loop")
# y= int(input("Enter Nom. "))
# for a in range(1,y):
#     # if a%2==0:
#     print(f"{a} * {x} = {a * x} ")
#     # else:
#     print(f"{a} ** {x} = {a ** x} ")


# password=input("Enter password ")
# while password != "abcd12":
#     print("ERROR Password")
#     password=input("Enter password ")
# else:
#     print("password is True")

# for y in range(15,1,-2):
#     print(y)
# else:
#     print(f"false codition y = {y}")


# def name_func(name="Ali",age=16):
#     print(f"\nwellcome {name} {age}")
#     return age

# # nam="ALi"
# # nam=input("Enter Name: ")
# # age=12
# x=name_func("ahmed")
# print(x)
i=1
while i<=10:
    
    print(f"i = {i}")
    i+=1 #i=i+1

def name_metod(name,age,*marks):
    print(f"welcome {name} {age}")
    for m in marks:
        print(f"Ur Marks: {m} ")

    

print("before Method\n")

name_metod("ali",45,60,70,40)
name_metod("ahmed",12,45,60,100,150)
# print(name_metod("ali"))
# name_metod("ali")
# print(b)