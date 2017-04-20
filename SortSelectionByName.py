import pymxs
rt = pymxs.runtime #so

li = []
lis = []
x = 0
for i in rt.selection:
	li.append(str(i.name))

li.sort()
	
for i in rt.selection:
	lis.append(rt.getnodebyname(li[x]))
	x += 1
	
del li
