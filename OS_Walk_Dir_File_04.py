import os

dirFile = open('current_dir_tree.txt', 'w')
curFolderName = ('PATH')
dirFile.write('The current folder is ' + curFolderName +'\n\n')

for dirpath, dirs, files in os.walk(curFolderName):
	path = dirpath.split('/')
	dirFile.write ('|' + (len(path))*' ' + '[' + os.path.basename(dirpath) + ']' + '\n')
	for f in files:
		dirFile.write ('|' + len(path)*' ' + f + '\n')

dirFile.close()
