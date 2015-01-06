f = open("output.txt")
count = 0
dic = {}
while True:
	r = f.readline()
	if r == "":
		break
	if "TRUE" not in r:
		continue
	idx = r.find("p")
	col = r[idx+1]
	row = r[idx+2]
	val = r[idx+3]
	dic[(col,row)] = val
	# print("(" + str(col) + "," + str(row) + "):" + str(val))
	count+=1
for key in sorted(dic, key=lambda x: (x[1],x[0])):
	print("%s: %s" % (key, dic[key]))
# print("TOTAL: " + str(count))