# myset={1,2,3,5,5,"a","z","z"}
# myset={1,2,3,5}
# print(myset)
# myset.add(22)
# print(myset)
# myset.update()
# myset.clear()
# print(myset)
# myset.remove(5)
# print(myset)
# myset.discard('s')
# print(myset)
# myset.discard('z')
# print(myset)
# myset={1,2,3,5}
# print(myset)
# myset2=set()
# for item in myset:
#     s=item*2
#     myset2.add(s)


# print(myset2)
# print(30 not in myset)

# list1=["a","B","C","a",1,3,5.02,1]
# print(list1)
# x=set(list1)
# print(x)
# T=("ahmed","Ali","IT",100,True,True)
# print(f"{type(T)} , Tuple is:{T}")

# y=set(T)
# print(f"{type(y)} ,  is:{y}")
# z=set("ahmed ali m")
# print(z)
# print(len(x))

# print(len(list1))

# setA={1,2,'x','y'}
# setB={True,False,100,3.14,5.6,0}
# print(setA)
# print(setB)
#Union |
# print(setA.union(setB))
# print(setA)
# setU=setA.union(setB)
# print(setU)
# print(setA | setB) # | => union
# print(setA)
# setA.update(setB)
# print(f"setA UsetB with update() is {setA}")
# intersection &
# setC={1,2,'x','y',100,False,False}
# setD={False,100,3.14,5.6,2}
# print(setC)
# print(setD)
# print(setC.intersection(setD))
# print(setC)
# setC.intersection_update(setD)
# print(setC)
# print(setC)
# print(setD)
# # setC.intersection_update(setD)
# print(setC)

# setD.intersection_update(setC)
# print(setD)

#Difference -
# setE={1,2,'x','y',100,False}
# setF={False,100,3.14,5.6,2}
# print(setE.difference(setF))#E-F
# print(setE - setF)
# print(setF.difference(setE))#F-E

#SymmetricDifference
# setJ={1,2,'x','y',100,False}
# setH={False,100,3.14,5.6,2}
# print(setJ.symmetric_difference(setH)) # ^ operator
# print(setJ ^ setH)
# setJ={1,2,'x','y',100,False,3,10}
# setH={False,100,3,11}
# print(setJ.issuperset(setH)) #setJ >= setH
# print(setJ >= setH)
# print(setH.issubset(setJ))#setH <= setJ


# setC={1,2,'x','y',100,False,False}
# myset=set()#EmptySet
# print(type(myset))
# print(myset)
# print(len(setC))
# print(setC)
# setC.add(3)
# print(setC)
# setC.add((2,5,8))
# print(setC)
# setC.add("Asma")
# x=set('Asma')
# print(setC)
# print(x)
# print(type(x))
# d={"k1":3,"k2":5}
# setDe=set(d)#convert from dictionary into set
# print(setDe)
# setDe.discard("k1")
# print(setDe)
# setDe.clear()
# print(setDe)

