import csv
import sys

#Usage python gen_instance.py XXX.csv

path=sys.argv[1]
with open(path) as f:
    reader=csv.reader(f)
    l = [row for row in reader]
num_band=int(l[0][1])
bands=l[1:num_band+1]
times=l[num_band+2:]
band=""
member=""
#10分枠のバンド
ten_band=""

for i in bands:
    band+='band("{0}").\n'.format(i[0])
    if int(i[7])==10:
        ten_band+='ten_band("{0}").\n'.format(i[0])
    for j in i[1:7]:
        if j!='':
            member+='member("{0}", "{1}").\n'.format(i[0],j)
            
print(band)
print(member)
k=1
assign=""
time=""
for i in times:
    time+='time({0}, "{1}").\n'.format(str(k),i[0])
    k+=1
    if i[1]=="休憩":
        assign+='assign("{0}", "休憩").\n'.format(i[0])
        
print(assign)
print(time)
print(ten_band)
