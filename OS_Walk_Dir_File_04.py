import os

dirFile = open('current_dir_tree.txt', 'w')
curFolderName = ('/home/jsoto3000/Documents/js_rj_udacity/js_rj_udacity-master/Python/')
dirFile.write('The current folder is ' + curFolderName +'\n\n')

for dirpath, dirs, files in os.walk(curFolderName):	 
	path = dirpath.split('/')
	dirFile.write ('|' + (len(path))*' ' + '[' + os.path.basename(dirpath) + ']' + '\n')
	for f in files:
		dirFile.write ('|' + len(path)*' ' + f + '\n')

dirFile.close()
