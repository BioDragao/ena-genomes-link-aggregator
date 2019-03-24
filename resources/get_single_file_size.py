# NOTE: http://zetcode.com/python/ftp/

import ftplib
import sys
import hashlib



def size_in_human_form(size):
    #2**10 = 1024
    power = 2**10
    n = 0
    Dic_powerN = {0 : '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /=  power
        n += 1
    print("FileSize : " ,size, Dic_powerN[n]+'B')
    return size, Dic_powerN[n]+'B'

def getFileSize(ftp,filename):
    try:
        size = ftp.size(filename)
        print("Filename :", filename)
        #print("FileSize :" ,size)
        return size
    except:
        print("Error")




def get_ftp_md5(ftp, remote_path):
    m = hashlib.md5()
    ftp.retrbinary('RETR %s' % remote_path, m.update)
    return m.hexdigest()

def md5sum_local_file(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()




ftp = ftplib.FTP("ftp.sra.ebi.ac.uk")

ftp.login()

#ftp.sendcmd('TYPE I')

# for a single genome file
#single_file_link = "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR442/007/SRR4423177/SRR4423177_1.fastq.gz"
#print(single_file_link)
#single_file_location = "/" + "/".join(single_file_link.split("/")[3:])
#print(single_file_location)
#single_file_name = single_file_link.split("/")[-1]
#print(single_file_name)
ftp.cwd("/vol1/fastq/SRR442/007/SRR4423177/")
#fileSize = getFileSize(ftp,"SRR4423177_1.fastq.gz")

size_in_human_form(fileSize)


## Native file size on local disk
# import os
# statinfo = os.stat('SRR4423177_1.fastq.gz')
# statinfo
# statinfo.st_size

## Get md5 hash of an ftp file

# ERR216904_2.fastq.gz  - has a size of ~50 MB
# ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216904/ERR216904_1.fastq.gz

# NOTE: This works!
get_ftp_md5(ftp, "/vol1/fastq/ERR216/ERR216904/ERR216904_1.fastq.gz")


#get_ftp_md5(ftp, single_file_location)

ftp.quit()
