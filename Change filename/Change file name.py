import os
def rename_files():
    #get file names in a list from directory
    file_list = os.listdir(r'C:\Users\Nanu\Desktop\Programming Foundations with Python ud036\Change filename\prank')
    #print (file_list)
    saved_path = os.getcwd()
    os.chdir(r'C:\Users\Nanu\Desktop\Programming Foundations with Python ud036\Change filename\prank')
    print ('current working directory is '+ saved_path) 
    for file_name in file_list:
        print ('Old name -'+file_name)
        print ('New name -'+file_name.translate(None, '0123456789'))
        os.rename(file_name,file_name.translate(None, '0123456789'))
    os.chdir(saved_path)
rename_files()
