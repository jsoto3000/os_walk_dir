import os


for dirpath, dirs, files in os.walk('PATH'):	 
	path = dirpath.split('/')
	print ('|', (len(path))*'---', '[',os.path.basename(dirpath),']')
	for f in files:
		print ('|', len(path)*'---', f)
