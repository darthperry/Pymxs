from pymxs import runtime as rt

 # User should get the name by them defined

def SortByName():
	ListResult = []
	Temp = []
	x = 0
	for i in rt.selection:
		Temp.append(str(i.name))

	Temp.sort()
	   
	for i in rt.selection:
		ListResult.append(rt.getnodebyname(Temp[x]))
		x += 1 #Python has no ++
	print ListResult    
	return ListResult	
	
def SortByVolume():
	ListResult = []
	Temp = []
	x = 0
	def Volume(i):
		volume = (i.max[0]-i.min[0])*(i.max[1]-i.min[1])*(i.max[2]-i.min[2])
		#calculate volmue by BoundingBox
		return volume
		
	for i in rt.selection:
		result = [Volume(i),str(i.name)]		
		Temp.append(result)

	Temp.sort()
		   
	for i in rt.selection:
		ListResult.append(rt.getnodebyname(Temp[x][1]))
		x += 1 #Python has no ++
	print ListResult   
	return ListResult	
	
def SortByPolycount():
	Pass
	
def main():
	Pass 
	
if __name__ == "__main__":
	main()