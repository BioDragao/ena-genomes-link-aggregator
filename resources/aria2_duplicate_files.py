import sys
import os
import json
import shutil


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

# def move_fastq_and_aria2_to_folder(f):
#     shutil.move(f,"./aria2_files/")


# # def copy_file_1gz_to_1gz_files_folder(f):
# #     shutil.copy(f,"./1gz_files/")


# def copy_fastq_and_aria2_to_folder(f):
#     shutil.copy(f,"./aria2_files/")

# #copy_fastq_and_aria2_to_folder("ERR216904_1.fastq.gz")


all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))
all_aria2_files = list(filter(lambda x:has_aria2_in_name(x), all_files))
all_fastq_files = list(set(filter(lambda x:has_fastq_in_name(x), all_files)) - set(all_aria2_files))


#all_completed_files = list(set(all_fastq_files) - set(all_aria2_files))


# doubtful_files = []

# for f1 in all_aria2_files:
#     for f2 in all_fastq_files:
#         if f1.split(".")[0] == f2.split(".")[0]:
#             print(f2, " has an ", f1, " aria2 file")
#             move_fastq_and_aria2_to_folder(f1)
#             move_fastq_and_aria2_to_folder(f2)
#             #copy_fastq_and_aria2_to_folder(f1)
#             #copy_fastq_and_aria2_to_folder(f2)


###################


#TODO: Need to read the initial << urls.txt >> file and find out which genomes remain to be completed now.

all_genomes_names = []


with open('urls.txt') as urls:
    for num, line in enumerate(urls):
        #print(line)
        all_genomes_names.append((line.split("/")[-1]).strip())


uploaded_genomes = []

with open('ready_to_upload.txt') as uploaded:
    for num, line in enumerate(uploaded):
        #print(line)
        uploaded_genomes.append(line.strip())


genomes_to_be_downloaded = list(set(all_genomes_names) - set(uploaded_genomes))


urls_of_genomes_to_be_downloaded = []

with open('urls.txt') as urls:
    for num, line in enumerate(urls):
        if (line.split("/")[-1]).strip() in genomes_to_be_downloaded:
            #print(line)
            urls_of_genomes_to_be_downloaded.append(line.strip())




