import argparse
import os.path
import os
import filecmp
    			

def CheckDir(dir1, dir2):
    compared = filecmp.dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files or compared.funny_files):
        return False
    for subdir in compared.common_dirs:
        if not CheckDir(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True
    
    
    
def CheckFile(file1, file2):
    if file1 != file2:
    	return False
    else:
    	return True
    	
    	
def Check_Dir_File(file, dir):
	if(os.path.isdir(dir)==True):
		if(os.listdir(dir)):
			entry = os.listdir(dir)
			for entries in entry:
				if file == entries: 
					return True
				else:
					Check_Dir_File(file, dir+'/'+entries)
	return False


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('f1', help='path of first file')
    parser.add_argument('f2', help='path of second file')
    args = parser.parse_args()
    file1 = args.f1
    file2 = args.f2
    
    if os.path.isfile(file1) and os.path.isfile(file2):
    	res = CheckFile(file1, file2)
    	
    elif os.path.isdir(file1) and os.path.isdir(file2):
    	res = CheckDir(file1, file2)
    	
    else:
    	if os.path.isfile(file1) and os.path.isdir(file2):
    		res = Check_Dir_File(file1, file2)
    	else:
    		res = Check_Dir_File(file2, file1)	
    		 			    	
    if (res):
        print("Same")
    else:
    	print("Not Same")
    

