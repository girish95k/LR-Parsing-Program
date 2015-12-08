f=open("lr.py","r")
g=open("new.py","w")
for line in f:
	g.write(" "*4+line)
f.close()
g.close()