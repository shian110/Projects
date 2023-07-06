#Usage python TTdecode.py XX.txt YY.csv(出力)

import sys
import re
import csv
path=sys.argv[1]
path2=sys.argv[2]

with open(path) as f:
    low=f.read()
    assign=re.findall("assign\(.*?\)",low)
    member=re.findall("member\(.*?\)",low)
assignlist=[]
memberlist=[]
for i in assign:
    assignlist.append([(re.findall('".*?"',i))[0][1:-1],(re.findall('".*?"',i))[1][1:-1]])
for i in member:
    memberlist.append([(re.findall('".*?"',i))[0][1:-1],(re.findall('".*?"',i))[1][1:-1]])

assignlist.sort()
writelist=[]
for i in assignlist:
    t=[]
    t.append(i[0])
    t.append(i[1])
    for j in memberlist:
        if i[1]==j[0]:
            t.append(j[1])
    writelist.append(t)
with open(path2,"w",encoding="utf_8_sig") as f:
    writer=csv.writer(f)
    writer.writerow(["時間割","バンド","メンバー"])
    
    for i in writelist:
        writer.writerow(i)
