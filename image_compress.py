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
sha256hash = hashlib.sha256()
while bytes:
	bytes=source.read(arg.b)
	sha256hash = hashlib.sha256(str(bytes).encode('utf-8'))
	sha256hash.update(bytes)
sha256hash.update(str(time.time()).encode())
print(sha256hash.hexdigest())
source.close()
