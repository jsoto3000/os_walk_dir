import os

for folderName, subfolders, filenames in os.walk('/home/jsoto3000/Documents/js_rj_udacity/js_rj_udacity-master/Python'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

print('')
