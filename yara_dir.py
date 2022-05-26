import argparse 
import os   
import yara

def dir_search(file, rule):
    if(os.path.isdir(file)):
        directory = os.listdir(file)
        for directories in directory:
            file += "/" + directories
            dir_search(file, rule)
    else:
        if(rule.match(file)):
            print("Rule Matched.")
        else:
            print("Rule Not Matched.")


if __name__=="__main__":
    parser=argparse.ArgumentParser() 
    parser.add_argument('-f', help = 'argument for file')
    parser.add_argument('-r', help = 'argument for rule file')
    args = parser.parse_args()
    dir_search(args.f, yara.compile(args.r))
