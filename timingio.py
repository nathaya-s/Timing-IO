import time
import os
import csv
import random

def writefile(data):
    with open(completeName, "w", newline="") as csvfile:
        wt = csv.writer(csvfile)
        header = ["pid,created_date,factory_id,defect_ratio,defect_box_ratio"]
        wt.writerow(header)
        wt.writerows(data)
    csvfile.close()

def openfile():
    f = open(completeName, "r")
    f.read()

def cal_defect_ratio(x):
    sum_defect_ratio = 0
    for i in x:
        sum_defect_ratio += i[3]
    print("defect ratio average : ", sum_defect_ratio / len(x))
    
def cal_defect_box_ratio(x):
    sum_defect_box_ratio = 0
    for i in x:
        sum_defect_box_ratio += i[4]
    print("defect ratio average : ", sum_defect_box_ratio / len(x))

start = time.time()
save_path = './Timing-IO'
completeName = os.path.join(save_path, "Write_file"+".csv")

data = []
for i in range(0, 50000):
    rand_1 = random.uniform(0.5, 1)
    rand_2 = random.randint(0, 1)
    data.append(["009", "08/11/2563", "CBR1", rand_1, rand_2])
    
writefile(data)
openfile()

writefile_1 = time.time()
cal_defect_ratio(data)
cal_defect_box_ratio(data)
find_avg = time.time()

iotime = writefile_1 - start
cal = find_avg - writefile_1
print("write file : ", iotime)
print("find average  : ", cal)
