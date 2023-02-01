#باستخدام الدوال؛ كون واطبع قائمة بمربع القيم من 1 إلى 20
print("")
def printValues():
	l = list()
	for i in range(1,21):
		l.append(i**2) # i^2
	print(l)
		
printValues()

