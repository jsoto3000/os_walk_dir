import os

dirFile = open('current_dir_tree.txt', 'w')
curFolderName = os.path.abspath('PATH')
dirFile.write('The current folder is ' + curFolderName +'\n')

for folderName, subfolders, filenames in os.walk(curFolderName):

    for subfolder in subfolders:
        dirFile.write('\t' + folderName + ': ' + subfolder + '\n')
        dirFile.write('\n')

        dirFile.write('')

        for filename in filenames:
            dirFile.write('\t\t' + folderName + ': '+ filename + '\n')
            dirFile.write('\n')

            dirFile.write('')

dirFile.close()
