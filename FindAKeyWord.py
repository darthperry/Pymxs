from pymxs import runtime as rt
#Must have object selection
for i in rt.selection:
	if i.modifiers["turbosmooth"] == None:
		print i.name+" add Turbosmooth"
		rt.addmodifier(i,rt.Turbosmooth(iterations = 2))
	else: #i.modifiers["turbosmooth"] != None
		print "ccc"
		i.turbosmooth.iterations = 2

# It is a exsample for test how pymxs find a keyword
