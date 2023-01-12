
print("function takes a list and returns a new list with unique elements")
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

myList=[8,8,1,2,3,3,3,3,4,5]
print(f"The List is: {myList}")
print("the list after remove duplicated values:")
print(unique_list(myList)) 

