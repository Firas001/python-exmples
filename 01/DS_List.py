mytuple=(1,2,6,5,8,1,0,6,8)
mystring="ali"
print(f"type of Seq. is {type(mytuple)} and the Elements are: {mytuple}")
print(mystring)
mylist=list(mytuple)
print(f"type of Seq. is {type(mylist)} and the Elements are: {mylist}")
mylist2=list(mystring)
print(f"type of Seq. is {type(mylist2)} and the Elements are: {mylist2}")

# print(mylist2 * 10)
print(mylist)
print(mylist[2])
mylist[2]=11
print(mylist)
l=len(mylist)
print(l)
print(mylist[len(mylist)-1])
print(mylist[l-1])
print(mylist[:])#whole list
print(mylist[3:])#start value 5 to end
print(mylist[:6])#start zero to position(index) 6 is not included
print(mylist[3:8])
print(mylist[::])#mylist[0:len(mylist):1]
print(mylist[::2])
print(2 in mylist)
print(5 in mylist)
print(2 not in mylist)
print(mylist)
mylist.append(100)
print(mylist)
x=25 #input
if x not in mylist:
    mylist.append(x)
print(mylist)
print(mylist.index(1))
mylist4=['a','b,','c']
print(mylist)
mylist.insert(3,[2,5,8])
mylist.insert(6,mylist4)
print(mylist)
print(mylist[3]) #[2, 5, 8]
print(mylist[3][0]) #2
print(mylist[3][1]) #5
print(mylist[3][2]) #8
print(mylist[6])
print(mylist[6][0]) #2
print(mylist[6][1]) #5
print(mylist[6][2]) #8






# mylist=[100,True, "A",5.6]
# print(mylist)
# mylist.append(5)
# print(mylist)
# mylist.append(10)
# print(mylist)
# list2=[5,10,25]
# mylist.append(list2)
# print(mylist)
# mylist.append("F")
# print(mylist)
# print(mylist[6])
# print(mylist[6][1])
# print(mylist[6][0])
# print(mylist[6][2])
# mylist.append(10)
# print(mylist)
# print(mylist.index(list2))
# # print(mylist.index("A"))
# print(f"length of list: {len(mylist)}")
# print(mylist)
# mylist.insert(3,4)
# print(mylist)
# print(f"length of list: {len(mylist)}")
# mylist.insert(0,33)
# print(mylist)
# mylist.insert(9,78)
# print(mylist)
# # print(list2.sort(reverse=True))
# list3=[55,0,5,5,10,25,2]
# # list3.sort(reverse=True)
# print(list3)
# # list3.reverse()
# print(list3)
# # list3.remove(5)
# # del  list3[1][0]
# print(list3)
# list3[1]=1
# print(list3)
# list3[1]='n'
# print(list3)
# # print(max(list3))
# # print(min(list3))











# x=[1,2,3,10,2,12]
# print(x)

# x.remove(2) #also: x.remove(x[1])
# print(x)
# print(max(x))
# x.reverse()
# print(x)