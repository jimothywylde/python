y = "global!"
def globalScope():
	global x
	x = "local!"
globalScope()
print(x)