file=None

try:     # Try code and Test Error
    
    fname=input("Enter the Name of File: ").strip()
    file = open(fname,'r') #open("A.txt",'r')
    print(file.read())
    file.close()
except FileNotFoundError:  # Handle the Error if found in try
    print("the of file Error..")


print("End of Program")