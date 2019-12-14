import os


for dirpath, dirs, files in os.walk("/home/jsoto3000/Documents/js_rj_udacity/js_rj_udacity-master/Python"):	 
	path = dirpath.split('/')
	print ('|', (len(path))*'---', '[',os.path.basename(dirpath),']')
	for f in files:
		print ('|', len(path)*'---', f)
