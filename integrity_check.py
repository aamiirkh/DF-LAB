import time
import tarfile
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('image')
parser.add_argument('-b')
arg=parser.parse_args()
source=open(arg.image,'rb')
bytes=b'x00'
md5hash = hashlib.md5()
while bytes:
	bytes=source.read(arg.b)
	md5hash = hashlib.md5()
	md5hash.update(bytes)
print(md5hash.hexdigest())
source.close()
