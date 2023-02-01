
print("multiplication the elements of List")
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  

myList=[8, 2, 3, -1, 7]
print(multiply(myList))
