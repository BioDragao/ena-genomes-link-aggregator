import sys
import hashlib
import os
import functools
import shutil
import json

def size_in_human_form(size):
    #NOTE: 2**10 = 1024
    power = 2**10
    n = 0
    Dic_powerN = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /=  power
        n += 1
    #print("FileSize : " ,size, Dic_powerN[n]+'B')
    return size, Dic_powerN[n]+'B'

def get_local_file_size(filename):
    #print("Filename :", filename)
    try:
        statinfo = os.stat(filename)
        return size_in_human_form(statinfo.st_size)
    except:
        print("Error")


#get_local_file_size("ERR216904_1.fastq.gz")

def md5sum_local_file(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    digest = hash_md5.hexdigest()
    #print("md5sum : ", digest)
    return digest

#md5sum_local_file("ERR216904_1.fastq.gz")

###########


def has_fastq_in_name(string):
    if (string.find("fastq") == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1

def has_aria2_in_name(string):
    if (string.find("aria2") == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1


all_files = os.listdir()
all_fastq_files = list(filter(lambda x:has_fastq_in_name(x), all_files))
all_aria2_files = list(filter(lambda x:has_aria2_in_name(x), all_files))
all_relevant_files = list(set(all_fastq_files) - set(all_aria2_files))



all_1gz_files = []
all_gz_files = []

for x in all_relevant_files:
    x1 = x.split(".")[-2]
    if x1 == "1":
        all_1gz_files.append(x)
    else:
        all_gz_files.append(x)



def copy_file_1gz_to_1gz_files_folder(f):
    shutil.copy(f,"./1gz_files/")

#copy_file_1gz_to_1gz_files_folder("ERR036217_1.fastq.1.gz")


def move_file_1gz_to_1gz_files_folder(f):
    shutil.move(f,"./1gz_files/")

#move_file_1gz_to_1gz_files_folder("ERR036217_1.fastq.1.gz")




#NOTE: This is a list of dicts containing the following information
# {"gz_file_name" :
#  "1gz_file_name" :
#  "md5sum_gz_file" :
#  "md5sum_1gz_file" : }



# d = {"gz_file_name" :  ,
#      "1gz_file_name" : ,
#      "md5sum_gz_file" : md5sum_local_file("ERR216904_2.fastq.gz") ,
#      "md5sum_1gz_file" : md5sum_local_file("ERR216904_2.fastq.1.gz")}


# duplicate_files_list_dict = []

# for f1 in all_gz_files:
#     for f2 in all_1gz_files:
#         if f1.split(".")[0] == f2.split(".")[0]:
#             print(f1, " and ", f2, " are similar")
#             duplicate_files_list_dict.append(
#                 {"gz_file_name" : f1 ,
#                  "1gz_file_name" : f2,
#                  "md5sum_gz_file" : md5sum_local_file(f1) ,
#                  "md5sum_1gz_file" : md5sum_local_file(f2),
#                  "gz_file_size" : get_local_file_size(f1),
#                  "1gz_file_size" : get_local_file_size(f2)})

# with open('duplicate_files_list_dict.json', 'w') as json_file:
#     json.dump(duplicate_files_list_dict, json_file)


with open('duplicate_files_list_dict.json') as f:
  duplicate_files_list_dict = json.load(f)


# DONE: Move the files matching the following criteria to a new folder
# - similar names
# - same digest
# - same size


for l in duplicate_files_list_dict:
    if (l['md5sum_gz_file'] == l['md5sum_1gz_file']) and \
       (l['gz_file_size'] == l['1gz_file_size']) and \
       (l['gz_file_size'] ==  l['1gz_file_size']):
        print("\n##################")
        print(l['gz_file_name'], " and ", l['1gz_file_name'], " are exactly the same!")
        print("@@@@@@@@@@@@@@@@@@")
        print("md5sum of file1 : ", l['md5sum_gz_file'])
        print("md5sum of file2 : ", l['md5sum_1gz_file'])
        print("@@@@@@@@@@@@@@@@@@")
        print("size of file1 : ", l['gz_file_size'])
        print("size of file2 : ", l['1gz_file_size'])
        print("@@@@@@@@@@@@@@@@@@")
        print("Moving ",l['1gz_file_name'], " to 1gz_files folder")
        move_file_1gz_to_1gz_files_folder(l['1gz_file_name'])
        print("##################\n")
    else:
        print("\n\nTHERE IS SOMETHING WRONG WITH ", l['1gz_file_name'], " AND ", l['1gz_file_name'], "\n\n")


