for i in rt.selection:
	if i.modifiers["turbosmooth"] == None:
		print i.name+" add Turbosmooth"
		rt.addmodifier(i,rt.Turbosmooth(iterations = 2))
	else: #i.modifiers["turbosmooth"] != None
		print "ccc"
		i.turbosmooth.iterations = 2