x = input("Enter 1st Numeric Value: ")
y = input("Enter 2nd Numeric Value: ")
z=None
print(type(z))
print(z)
try:     # Try code and Test Error
    x = int(x)
    y = int(y)
    z = x/y
except ValueError:  # Handle the Error if found in try
    print(f"must be Enter number.. {x} or {y} is not Number{z}")
except ZeroDivisionError:
    print(f"the 2nd value is {y}, must be not equal to zero")
else:    # If not Found Error in Try
    print(f"Good values; the Result of operation is {z}\n")
finally: # Execute where's happen
    print("End of Try Exception.")

print("End of Program")