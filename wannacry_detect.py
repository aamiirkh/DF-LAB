import yara
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('f')
parser.add_argument('r')
args=parser.parse_args()
file = args.f
ptr = open(arg.r, 'r').read()
rules = yara.compile(ptr)
print(rules.match(arg.file))
