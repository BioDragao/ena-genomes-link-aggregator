# cmp --silent ./ERR036201_1.fastq.gz ./ERR036201_1.fastq.1.gz || echo "files are different"
# cmp --silent ./ERR036201_1.fastq.gz ./ERR036201_1.fastq.1.gz && echo '### SUCCESS: Files Are Identical! ###' || echo '### WARNING: Files Are Different! ###'


## TODO:
## - Compare the two files, two of which are downloaded and differ by <.1.gz> in their name. Compare by < md5sum > and < cmp >
## - Pick only one of these files and move to a different folder
## - Compare with the < urls.txt > which ones have been downloaded and which ones are remaining
## - Compare the size of file downloaded with the size of the file on the remote


##


import os

list_of_all_files = os.listdir()

#############
# Python program to find MD5 hash value of a file
import hashlib

filename = input("Enter the file name: ")
md5_hash = hashlib.md5()
with open(filename,"rb") as f:
    # Read and update hash in chunks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        md5_hash.update(byte_block)
    print(md5_hash.hexdigest())
