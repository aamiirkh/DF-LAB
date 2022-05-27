import argparse
import os.path
import os
import filecmp
import hashlib
    			

def CheckDir(dir1, dir2):
    compared = filecmp.dircmp(dir1, dir2)
    if (compared.left_only or compared.right_only or compared.diff_files or compared.funny_files):
        return False
    for subdir in compared.common_dirs:
        if not CheckDir(os.path.join(dir1, subdir), os.path.join(dir2, subdir)):
            return False
    return True


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('d1', help='path of first file')
    parser.add_argument('d2', help='path of second file')
    args = parser.parse_args()
    dir1 = args.d1
    dir2 = args.d2
    
    if os.path.isdir(dir1) and os.path.isdir(dir2):
    	res = CheckDir(dir1, dir2)
    		 			    	
    if (res):
        print("Same")
    else:
    	print("Not Same")
    
