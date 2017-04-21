from pymxs import runtime as rt

ListResult = [] # User should get the name by them defined

def main():
	Temp = []
	x = 0
	for i in rt.selection:
		Temp.append(str(i.name))

	Temp.sort()
	   
	for i in rt.selection:
		ListResult.append(rt.getnodebyname(Temp[x]))
		x += 1 #Python has no ++
	   
	return ListResult	
	
if __name__ == "__main__":
	main()