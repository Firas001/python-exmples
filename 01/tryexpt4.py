# try:
#     print(9/3)
#     print(int('a'))
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Not Number")
# except:
#     print("General Error")

# file = open("m.txt",'r')
# print(file.read())
# file.close()
try:
    print(int(2.5))
    print(10/0)
    print("execute this line")
except ValueError:
    print("must be Integer value")
except ZeroDivisionError:
    print("Error")
except:
    print("general state")
