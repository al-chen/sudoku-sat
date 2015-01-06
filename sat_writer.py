def smake(x,y,v):
	"""Return a boolean variable as a string."""
	return "p" + str(x) + str(y) + str(v)

def cluster(x1, x2, y1, y2, f):
	"""Ensure a 3x3 sub-grid contains a number only once."""
	for c1 in range(x1,x2):
		for r1 in range(y1,y2):
			for c2 in range(x1,x2):
				for r2 in range(y1,y2):
					if c1 == c2 and r1 == r2:
						continue
					for v in range(1,10):
						f.write("ASSERT(" + smake(c1,r1,v) + " => NOT " + smake(c2,r2,v) + ");\n")

def line(x, boo, f):
	"""If boo is true, ensures row x contains a number only once.
	If boo is false, ensures column x contains a number only once.
	"""
	if boo: # row x
		for c1 in range(1,10):
			for c2 in range(1,10):
				if c1 == c2:
					continue
				for v in range(1,10):
					f.write("ASSERT(" + smake(c1,x,v) + " => NOT " + smake(c2,x,v) + ");\n")
	else: # column x
		for r1 in range(1,10):
			for r2 in range(1,10):
				if r1 == r2:
					continue
				for v in range(1,10):
					f.write("ASSERT(" + smake(x,r1,v) + " => NOT " + smake(x,r2,v) + ");\n")

def create_stp_input(dic, input_file):
	"""Creates a text file for stp."""
	f = open(input_file + ".txt", 'w')
	# Establish variables
	for i in range(1,10):
		for j in range(1,10):
			for k in range(1,10):
				if i==9 and j==9 and k==9:
					f.write(smake(i,j,k) + " : BOOLEAN;\n")
					break
				f.write(smake(i,j,k) + ", ")

	# Assert variables for points with given, correct values to be true
	# Assert variables for points with wrong values to be false
	for key in dic:
		x, y, value = key[0], key[1], dic[key]
		f.write("ASSERT(" + smake(x,y,value) + ");\n")
		for i in range(1,10):
			if i == value:
				continue
			f.write("ASSERT(NOT " + smake(x,y,i) + ");\n")				

	# All 3x3 sub-grids 
	cluster(1, 4, 1, 4, f)
	cluster(4, 7, 1, 4, f)
	cluster(7, 10, 1, 4, f)
	cluster(1, 4, 4, 7, f)
	cluster(4, 7, 4, 7, f)
	cluster(7, 10, 4, 7, f)
	cluster(1, 4, 7, 10, f)
	cluster(4, 7, 7, 10, f)
	cluster(7, 10, 7, 10, f)

	for x in range(1,10):
		line(x, True, f)
		line(x, False, f)

	for x in range(1,10):
		for y in range(1,10):
			f.write("ASSERT(" + smake(x,y,1) + " OR " + smake(x,y,2) + " OR " + smake(x,y,3) + " OR " + smake(x,y,4) + " OR " + smake(x,y,5) + " OR " + smake(x,y,6) + " OR " + smake(x,y,7) + " OR " + smake(x,y,8) + " OR " + smake(x,y,9) + ");\n")

	f.close()

if __name__ == "__main__":
	# create dictionary of given points and values
	dic = {}
	dic[(6,2)] = 3
	dic[(8,2)] = 8
	dic[(9,2)] = 5
	dic[(3,3)] = 1
	dic[(5,3)] = 2
	dic[(4,4)] = 5
	dic[(6,4)] = 7
	dic[(3,5)] = 4
	dic[(7,5)] = 1
	dic[(2,6)] = 9
	dic[(1,7)] = 5
	dic[(8,7)] = 7
	dic[(9,7)] = 3
	dic[(3,8)] = 2
	dic[(5,8)] = 1
	dic[(5,9)] = 4
	dic[(9,9)] = 9
	create_stp_input(dic, "sat_input")