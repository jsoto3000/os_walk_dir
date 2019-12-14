import os

dirFile = open('current_dir_tree.txt', 'w')
curFolderName = os.path.abspath('/home/jsoto3000/Documents/js_rj_udacity/js_rj_udacity-master/Python')
dirFile.write('The current folder is ' + curFolderName +'\n\n')

for folderNames, subfolders, filenames in os.walk(curFolderName):

    for subfolder in subfolders:
        dirFile.write('\t' + subfolder + '\n')
        dirFile.write('\n')

        dirFile.write('')
            
        for filename in filenames:
            dirFile.write('\t\t' + filename + '\n')
            dirFile.write('\n')

            dirFile.write('')

dirFile.close()
