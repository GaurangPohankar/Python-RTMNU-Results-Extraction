##import os
##
##def createFolder(directory):
##    try:
##        if not os.path.exists(directory):
##            os.makedirs(directory)
##    except OSError:
##        print ('Error: Creating directory. ' +  directory)
##        
##
### Example
##createFolder('./data/')
##
##file = open("copy.txt", "w") 
##file.write("Your text goes here") 
##file.close()


import os.path

save_path = 'C:/example/'

name_of_file = raw_input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".txt")         

file1 = open(completeName, "w")

toFile = raw_input("Write what you want into the field")

file1.write(toFile)

file1.close()
