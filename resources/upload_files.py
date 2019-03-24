import os
import subprocess


#######
# SCRATCH

# all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


# for f in all_files:
#     subprocess.call(["rclone","copy", f , "onedrive-abhi:ena-genomes", "-vv"])

#rclone copy ERR036201_1.fastq.gz onedrive-abhi:ena-genomes -vv


#######



#rclone copy ERR036201_1.fastq.gz onedrive-abhi:ena-genomes -vv

def has_fastq_in_name(string):
    if (string.find("fastq") == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))
all_fastq_files = list(filter(lambda x:has_fastq_in_name(x), all_files))


for f in all_files:
    subprocess.call(["rclone","copy", f , "onedrive-abhi:ena-genomes", "-vv"])
