from pymxs import runtime as rt
Temp = []
ListResult = []
x = 0
for i in rt.selection:
   Temp.append(str(i.name))

Temp.sort()
   
for i in rt.selection:
   ListResult.append(rt.getnodebyname(Temp[x]))
   x += 1 #Python has no ++
   
del Temp