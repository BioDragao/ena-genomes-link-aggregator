import os
import json
import subprocess
import shutil

# links = [
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181795/ERR181795_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181795/ERR181795_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181819/ERR181819_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181819/ERR181819_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181820/ERR181820_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181820/ERR181820_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181831/ERR181831_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181831/ERR181831_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181860/ERR181860_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181860/ERR181860_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181910/ERR181910_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181910/ERR181910_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181920/ERR181920_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181920/ERR181920_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181929/ERR181929_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181929/ERR181929_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181930/ERR181930_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181930/ERR181930_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181933/ERR181933_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181933/ERR181933_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181949/ERR181949_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181949/ERR181949_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181961/ERR181961_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181961/ERR181961_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181963/ERR181963_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181963/ERR181963_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181969/ERR181969_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181969/ERR181969_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181982/ERR181982_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR181/ERR181982/ERR181982_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182008/ERR182008_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182008/ERR182008_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182009/ERR182009_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182009/ERR182009_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182024/ERR182024_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182024/ERR182024_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182042/ERR182042_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182042/ERR182042_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182054/ERR182054_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR182/ERR182054/ERR182054_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190344/ERR190344_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190344/ERR190344_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190345/ERR190345_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190345/ERR190345_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190361/ERR190361_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190361/ERR190361_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190382/ERR190382_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190382/ERR190382_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190389/ERR190389_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR190/ERR190389/ERR190389_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212038/ERR212038_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212038/ERR212038_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212054/ERR212054_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212054/ERR212054_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212066/ERR212066_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212066/ERR212066_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212073/ERR212073_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212073/ERR212073_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212103/ERR212103_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212103/ERR212103_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212109/ERR212109_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212109/ERR212109_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212116/ERR212116_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212116/ERR212116_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212155/ERR212155_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212155/ERR212155_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212160/ERR212160_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212160/ERR212160_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212163/ERR212163_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212163/ERR212163_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212164/ERR212164_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212164/ERR212164_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212166/ERR212166_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR212/ERR212166/ERR212166_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216902/ERR216902_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216902/ERR216902_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216904/ERR216904_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216904/ERR216904_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216940/ERR216940_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216940/ERR216940_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216950/ERR216950_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216950/ERR216950_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216952/ERR216952_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR216/ERR216952/ERR216952_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221562/ERR221562_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221562/ERR221562_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221563/ERR221563_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221563/ERR221563_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221567/ERR221567_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221567/ERR221567_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221580/ERR221580_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221580/ERR221580_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221593/ERR221593_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221593/ERR221593_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221596/ERR221596_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221596/ERR221596_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221608/ERR221608_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR221/ERR221608/ERR221608_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245748/ERR245748_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245748/ERR245748_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245817/ERR245817_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245817/ERR245817_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245820/ERR245820_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245820/ERR245820_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245822/ERR245822_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245822/ERR245822_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245825/ERR245825_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR245/ERR245825/ERR245825_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR983/ERR983237/ERR983237_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR983/ERR983237/ERR983237_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR171/ERR171130/ERR171130_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR171/ERR171130/ERR171130_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR171/ERR171131/ERR171131_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR171/ERR171131/ERR171131_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/008/SRR5709868/SRR5709868_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/008/SRR5709868/SRR5709868_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/003/SRR5709913/SRR5709913_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/003/SRR5709913/SRR5709913_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/007/SRR5709917/SRR5709917_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/007/SRR5709917/SRR5709917_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/004/SRR5709924/SRR5709924_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/004/SRR5709924/SRR5709924_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/007/SRR5709937/SRR5709937_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/007/SRR5709937/SRR5709937_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/001/SRR5709941/SRR5709941_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/001/SRR5709941/SRR5709941_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/005/SRR5709955/SRR5709955_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR570/005/SRR5709955/SRR5709955_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR571/008/SRR5710008/SRR5710008_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR571/008/SRR5710008/SRR5710008_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/002/SRR5065322/SRR5065322_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/002/SRR5065322/SRR5065322_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/006/SRR5065386/SRR5065386_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/006/SRR5065386/SRR5065386_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/007/SRR5067357/SRR5067357_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/007/SRR5067357/SRR5067357_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/007/SRR5067517/SRR5067517_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/007/SRR5067517/SRR5067517_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/006/SRR5067596/SRR5067596_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR506/006/SRR5067596/SRR5067596_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/008/SRR5073518/SRR5073518_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/008/SRR5073518/SRR5073518_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/005/SRR5073705/SRR5073705_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/005/SRR5073705/SRR5073705_2.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/007/SRR5073987/SRR5073987_1.fastq.gz",
#     "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/007/SRR5073987/SRR5073987_2.fastq.gz"
#     ]


# with open("urls_to_be_downloaded.json", 'wb') as outfile:
#     json.dump(links, outfile)

initial_urls_list = []

with open("urls_to_be_downloaded.json") as infile:
     initial_urls_list = json.load(infile)

updated_list_of_pending_urls = initial_urls_list

#NOTE: All of these work fine
# aria2c -iurls.txt -j4
# aria2c ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/005/SRR5073705/SRR5073705_1.fastq.gz
# subprocess.call(["aria2c" , "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR507/005/SRR5073705/SRR5073705_1.fastq.gz"])
# subprocess.call(["/usr/bin/aria2c", "--version"])

for url in initial_urls_list:
    print(url)
    subprocess.call(["aria2c" , url])

    updated_list_of_pending_urls.remove(url)
    with open("updated_list_of_pending_downloads.json", 'w') as outfile:
        json.dump(updated_list_of_pending_urls, outfile)







