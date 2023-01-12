x = input("Enter 1st Numeric Value: ")
y = input("Enter 2nd Numeric Value: ")
z=None #null int other Language
try:     # Try code and Test Error
    x = int(x)
    y = int(y)
    z = x/y
except ValueError:
    print("Not define variable")
except:  # Handle the Error if found in try
    print(f"must be Enter number.. {x} or {y} is not Number ")
else:    # If not Found Error in Try
    print(f"Good values; the Result of operation is {z}\n")
finally: # Execute where's happen
    print("End of Try Exception.")

print("End of Program")