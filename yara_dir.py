import argparse 
import os   
import yara

def dir_search(file, rule):
	if(os.path.isdir(file)):
		directory = os.listdir(file)
		for directories in directory:
			dir_search(file+"/"+directories, rule)
	else:
		if(rule.match(file)):
			print("Rule Matched = "+ file)


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path',help='Add the path you want the rules to match')
    parser.add_argument('-r',help='yara rule here.')
    arg = parser.parse_args()
    testing = arg.path
    rules=yara.compile(filepath=arg.r)
    dir_search(testing, rules)
