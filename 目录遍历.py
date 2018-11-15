import os
dirpath=input('请输入你要遍历的目录：')
def getdir(dirpath,level=0):
	level+=2
	if not dirpath:
		dirpath=os.getcwd()
	mylist=os.listdir(dirpath)
	for name in mylist:
		print('-'*level+'|'+name)
		name=os.path.join(dirpath,name)
		if os.path.isdir(name):
			getdir(name,level)
getdir(dirpath)
