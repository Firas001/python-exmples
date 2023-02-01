#برنامج يستقبل سلسلة ويطبع طولها وعدد الأحرف وعدد الأرقام وعدد الأحرف الخاصة فيها
s = input("Input a string")
#input: my name is ali, my Age is 25:m\
print("Length of String:", len(s))
print("The String is:", s)
d=l=other=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else: 
        other=other+1
        #pass
print("Letters", l) #Letters 19
print("Digits", d) #Digits 2
print("Other chracters", other) #Other chracters 10

#برنامج يستقبل سلسلة ويطبع عدد الأحرف وعدد الأرقام
# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)
