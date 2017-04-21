from pymxs import runtime as rt

def main():
	original = rt.selection[0]
	rt.execute("maxOps.cloneNodes $ cloneType:#copy newNodes:&nnl select nnl")# have to use Maxscript
	temp = rt.selection[0]
	temp.name = "High_" + original.name
	rt.addmodifier(temp,rt.Turbosmooth(iterations = 2,sepBySmGroups = True))
	rt.addmodifier(temp,rt.Turbosmooth(iterations = 1))


if __name__ == "__main__":
	main()