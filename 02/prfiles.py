# import os



# a=20
# m=55
# c=2.36
# f=open("myfile.txt","w")
# f.write(str(a)+'\n')
# f.write(str(m)+'\n')
# f.write(str(c))
# f.close()

# # f=open("myfile.txt","r")
# # x=f.readline()
# # print(int(x))
# # y=int(f.readline())
# # print(y)
# # z=float(f.readline())
# # print(z)
# # f.close()
# f=open("A.txt","a")
# # print(f.read(70))
# # for l in f:
# #     print(l)
# f.write('\n'+'\n')
# p=f.truncate(5)
# print(p)
# print(f.tell())
# f.close()








# # st1='\npythony  languageeeeeeeeee'
# # print(f"length of string: {len(st1)}")
# # Srem=st1.strip()
# # Srem=st1.strip('pe')
# # print(st1)
# # print(f"length of string: {len(Srem)}")
# # print(Srem)
# # lrem=st1.lstrip('\n')
# # print(f"length of string after Lstrip: {len(lrem)}")
# # print(st1)
# # print(lrem)
# # Rrem=st1.rstrip('e')
# # print(f"length of string after Rstrip: {len(Rrem)}")
# # print(Rrem)













# # f=open("myfile.txt")
# # with open("myfile.txt","w") as f:
# #     f.write("")
# # f.close()
# # for l in f:
# #     print(l)
# # f.close()


# # a,b,v=1,5,55.33
# # f=open("myfile.txt","a")
# # f.write("Python Programming\n")
# # # f.write(str(b)+"\n")
# # # f.write(str(v)+'\n')
# # print(f.tell())
# # print(f.truncate(5))
# # print(f.seek(3))
# # # f.close()
# # f=open("myfile.txt","r")
# # print()
# # f.close()














# # str='       Python      Language     '
# # print(str)
# # rem=str.strip()
# # print("strip Function:")
# # print(rem)
# # print(len(str),len(rem))
# # print("***************")
# # str='       Python      Language     '
# # print(str)
# # lrem=str.lstrip()
# # print("Leading strip Function:")
# # print(lrem)
# # print(len(str),len(lrem))
# # print("*"*20)
# # str='       Python      Language     '
# # print(str)
# # Rrem=str.rstrip()
# # print("Leading strip Function:")
# # print(Rrem)
# # print(len(str),len(Rrem))
# # print("*"*20)
# # str='\nPython\nLanguage'
# # print(str)
# # s=str.strip('\n')
# # print(s)
# # print(len(str),len(s))











# # f=open("myfile.txt","a")
# # f.write("helo world\nIT collage")
# # f.write("\nMisrata\t univercity")
# # f.close()

# # f=open("myfile.txt","r")
# # print(f"name of file is: {f.name}")
# # print(f"mode of file is: {f.mode}")
# # print(f"encoding of file is: {f.encoding}")
# # # print(f.read(50))
# # print(f.readline(2))
# # print(f.readline())
# # print(f.readline())
# # f.close()

# # f=open("myfile.txt","w")
# # f.write("1254")
# # f.close()
# # f=open("myfile.txt","r")
# # x=f.read()
# # y=int(x)
# # f.close()
# # print(f"x: \n{type(x)} {x}")
# # print(f"y: \n{type(y)} {y}")
# # f=open("myfile.txt","a")
# # f.write(x.rstrip('-'))
# # f.close()
# # a,b,c=11,54,22
# # f=open("myfile.txt","w")
# # # f.write(a)
# # f.write(str(a))
# # # f.write(b)
# # f.write(str(b)+'\n')
# # f.write(str(c))
# # f.close()


# # mystr = 'Learn\nPython'
# # print(mystr)
# # print(len(mystr))
# # s=mystr.strip('\n')
# # print(s)
# # print(len(s))







# # print (f"the current dir is: {os.getcwd()}")
# # print(f"abs path: {os.path.abspath(__file__)}")
# # x=os.path.abspath(__file__)
# # print(f'dir name is: {os.path.dirname(x)}')

# # myfile=open(r"D:\vscode\Python\newfile.txt","r")
# # myfile=open(r"D:\vscode\Python\newfile.txt")
# # print(f"name of file: {myfile.name}")
# # print(f"mode of file: {myfile.mode}")
# # print(f"file encoding: {myfile.encoding}")
# # print("********************")
# # print(myfile.read())
# # print(myfile.read(8))
# # print(myfile.read())
# # print(myfile.readline())

# # print("content: ")
# # for s in myfile:
# #     print(s)
# #     if s.startswith("*"):
# #         break

# # myfile.close()
# # print("*"*20)
# # f=open("A.txt","w") # Overriding file
# # f.write("FfFlvmal;sdm  \n")
# # f.write("It's very Easy :) ")
# # f.close()

# # f=open("A.txt","a") #Append to file
# # x="\n Information    \t      Tech.  \n"
# # f.write("Misrata Univercity :)" +  x.rstrip("\n"))
# # f.close()

# # f=open("A.txt") #Read from file
# # print(f.read())
# # f.close()