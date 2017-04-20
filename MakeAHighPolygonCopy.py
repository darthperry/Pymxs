origal = rt.selection[0]
rt.execute("maxOps.cloneNodes $ cloneType:#copy newNodes:&nnl select nnl")
# have to use Maxscript
temp = rt.selection[0]
temp.name = "High_" + origal.name
rt.addmodifier(temp,rt.Turbosmooth(iterations = 2,sepBySmGroups = True))
rt.addmodifier(temp,rt.Turbosmooth(iterations = 1))
